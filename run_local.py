import os
import sys
import logging
from custom_agents.action import Action

sys.path.append(os.path.join(os.path.dirname(__file__), 'ARC-AGI-3-Agents'))
sys.path.append(os.path.dirname(__file__))

import arc_agi
from arcengine import GameAction as EngineAction
import importlib.util
import types
from concurrent.futures import ThreadPoolExecutor

# Pre-load agents submodules directly to skip agents/__init__.py template imports
_agents_dir = os.path.join(os.path.dirname(__file__), "ARC-AGI-3-Agents", "agents")
_agents_pkg = types.ModuleType("agents")
_agents_pkg.__path__ = [_agents_dir]
_agents_pkg.__package__ = "agents"
sys.modules["agents"] = _agents_pkg

for _name in ("structs", "recorder", "tracing", "agent"):
    _spec = importlib.util.spec_from_file_location(
        f"agents.{_name}", os.path.join(_agents_dir, f"{_name}.py"),
        submodule_search_locations=[],
    )
    _mod = importlib.util.module_from_spec(_spec)
    sys.modules[f"agents.{_name}"] = _mod
    setattr(_agents_pkg, _name, _mod)
    _spec.loader.exec_module(_mod)

FrameData = sys.modules["agents.structs"].FrameData
GameAction = sys.modules["agents.structs"].GameAction
GameState = sys.modules["agents.structs"].GameState

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")


def obs_to_frame_data(obs):
    available = []
    for a in obs.available_actions:
        try:
            available.append(GameAction.from_id(a))
        except ValueError:
            pass
    return FrameData(
        game_id=obs.game_id,
        frame=obs.frame,
        state=GameState(obs.state.value),
        score=obs.levels_completed,
        available_actions=available,
        guid=obs.guid,
        full_reset=obs.full_reset,
    )


def execute_action(env, action):
    if action == GameAction.RESET:
        return env.reset()
    engine_action = EngineAction[action.name]
    data = {}
    if action.is_complex():
        data = {"x": int(action.action_data.x), "y": int(action.action_data.y)}
    return env.step(engine_action, data=data)


def run_game(arc, game_id):
    env = arc.make(game_id)
    agent = Action(
        card_id="local", game_id=game_id, agent_name="action",
        ROOT_URL="", record=False,
    )
    obs = env.reset()
    frame = obs_to_frame_data(obs)
    agent.frames = [frame]

    while not agent.is_done(agent.frames, agent.frames[-1]):
        action = agent.choose_action(agent.frames, agent.frames[-1])
        obs = execute_action(env, action)
        if obs:
            frame = obs_to_frame_data(obs)
            agent.frames.append(frame)
            logger.info(f"{game_id} - {action.name}: count {agent.action_counter}, score {frame.score}")
        agent.action_counter += 1

    logger.info(f"{game_id} finished - score: {agent.frames[-1].score}")

def main():
    arc = arc_agi.Arcade()
    games = [g.game_id for g in arc.get_environments()]
    logger.info(f"Games: {games}")

    with ThreadPoolExecutor(max_workers=5) as pool:
        pool.map(lambda g: run_game(arc, g), games)

    scorecard = arc.get_scorecard()
    if scorecard:
        logger.info(f"Final scorecard: {scorecard}")


if __name__ == "__main__":
    main()
