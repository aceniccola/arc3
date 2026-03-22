print('start ............................\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
from arc_agi import Arcade, OperationMode
from arcengine import GameAction

print('true start ............................\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

arc = Arcade(operation_mode=OperationMode.OFFLINE)


env = arc.make("ls20")
print('env created ............................\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print(env.info.default_fps)
print(env.include_frame_data)
print('env info ............................\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
obs = env.observation_space
if obs:
    print(f"Game state: {obs.state}")
    print(f"Levels completed: {obs.levels_completed}")
print('envs ............................\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


# See available actions
print(env.action_space)


print('action space ............................\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
# Take an action
obs = env.step(GameAction.ACTION1)
print(f'action taken ............................{obs.frame[0][0]}\n {obs.frame[0][1]}\n {obs.frame[0][2]}\n {obs.frame[0][3]}\n {obs.frame[0][4]}\n {obs.frame[0][5]}\n {obs.frame[0][6]}\n {obs.frame[0][7]}\n {obs.frame[0][8]}\n {obs.frame[0][9]}\n {obs.frame[0][10]}\n {obs.frame[0][11]}\n {obs.frame[0][12]}\n {obs.frame[0][13]}\n {obs.frame[0][14]}\n {obs.frame[0][15]}\n {obs.frame[0][16]}\n {obs.frame[0][17]}\n {obs.frame[0][18]}\n {obs.frame[0][19]}\n {obs.frame[0][20]}\n {obs.frame[0][21]}\n {obs.frame[0][22]}\n {obs.frame[0][23]}\n {obs.frame[0][24]}\n {obs.frame[0][25]}\n {obs.frame[0][26]}\n {obs.frame[0][27]}\n {obs.frame[0][28]}\n {obs.frame[0][29]}\n {obs.frame[0][30]}\n {obs.frame[0][31]}\n {obs.frame[0][32]}\n {obs.frame[0][33]}\n {obs.frame[0][34]}\n {obs.frame[0][35]}\n {obs.frame[0][36]}\n {obs.frame[0][37]}\n {obs.frame[0][38]}\n {obs.frame[0][39]}\n {obs.frame[0][40]}\n {obs.frame[0][41]}\n {obs.frame[0][42]}\n {obs.frame[0][43]}\n {obs.frame[0][44]}\n {obs.frame[0][45]}\n {obs.frame[0][46]}\n {obs.frame[0][47]}\n {obs.frame[0][48]}\n {obs.frame[0][49]}\n {obs.frame[0][50]}\n {obs.frame[0][51]}\n {obs.frame[0][52]}\n {obs.frame[0][53]}\n {obs.frame[0][54]}\n {obs.frame[0][55]}\n {obs.frame[0][56]}\n {obs.frame[0][57]}\n {obs.frame[0][58]}\n {obs.frame[0][59]}\n {obs.frame[0][60]}\n {obs.frame[0][61]}\n {obs.frame[0][62]}\n {obs.frame[0][63]}\n')
obs
obs = env.observation_space
if obs:
    print(f"Game state: {obs}")
    print(f"Levels completed: {obs.levels_completed}")
obs = env.step(GameAction.ACTION5)
print(f'action taken ............................{obs.frame[0][0]}\n {obs.frame[0][1]}\n {obs.frame[0][2]}\n {obs.frame[0][3]}\n {obs.frame[0][4]}\n {obs.frame[0][5]}\n {obs.frame[0][6]}\n {obs.frame[0][7]}\n {obs.frame[0][8]}\n {obs.frame[0][9]}\n {obs.frame[0][10]}\n {obs.frame[0][11]}\n {obs.frame[0][12]}\n {obs.frame[0][13]}\n {obs.frame[0][14]}\n {obs.frame[0][15]}\n {obs.frame[0][16]}\n {obs.frame[0][17]}\n {obs.frame[0][18]}\n {obs.frame[0][19]}\n {obs.frame[0][20]}\n {obs.frame[0][21]}\n {obs.frame[0][22]}\n {obs.frame[0][23]}\n {obs.frame[0][24]}\n {obs.frame[0][25]}\n {obs.frame[0][26]}\n {obs.frame[0][27]}\n {obs.frame[0][28]}\n {obs.frame[0][29]}\n {obs.frame[0][30]}\n {obs.frame[0][31]}\n {obs.frame[0][32]}\n {obs.frame[0][33]}\n {obs.frame[0][34]}\n {obs.frame[0][35]}\n {obs.frame[0][36]}\n {obs.frame[0][37]}\n {obs.frame[0][38]}\n {obs.frame[0][39]}\n {obs.frame[0][40]}\n {obs.frame[0][41]}\n {obs.frame[0][42]}\n {obs.frame[0][43]}\n {obs.frame[0][44]}\n {obs.frame[0][45]}\n {obs.frame[0][46]}\n {obs.frame[0][47]}\n {obs.frame[0][48]}\n {obs.frame[0][49]}\n {obs.frame[0][50]}\n {obs.frame[0][51]}\n {obs.frame[0][52]}\n {obs.frame[0][53]}\n {obs.frame[0][54]}\n {obs.frame[0][55]}\n {obs.frame[0][56]}\n {obs.frame[0][57]}\n {obs.frame[0][58]}\n {obs.frame[0][59]}\n {obs.frame[0][60]}\n {obs.frame[0][61]}\n {obs.frame[0][62]}\n {obs.frame[0][63]}\n')
obs
obs = env.observation_space
if obs:
    print(f"Game state: {obs}")
    print(f"Levels completed: {obs.levels_completed}")
obs = env.step(GameAction.ACTION1)
print(f'action taken ............................{obs.frame[0][0]}\n {obs.frame[0][1]}\n {obs.frame[0][2]}\n {obs.frame[0][3]}\n {obs.frame[0][4]}\n {obs.frame[0][5]}\n {obs.frame[0][6]}\n {obs.frame[0][7]}\n {obs.frame[0][8]}\n {obs.frame[0][9]}\n {obs.frame[0][10]}\n {obs.frame[0][11]}\n {obs.frame[0][12]}\n {obs.frame[0][13]}\n {obs.frame[0][14]}\n {obs.frame[0][15]}\n {obs.frame[0][16]}\n {obs.frame[0][17]}\n {obs.frame[0][18]}\n {obs.frame[0][19]}\n {obs.frame[0][20]}\n {obs.frame[0][21]}\n {obs.frame[0][22]}\n {obs.frame[0][23]}\n {obs.frame[0][24]}\n {obs.frame[0][25]}\n {obs.frame[0][26]}\n {obs.frame[0][27]}\n {obs.frame[0][28]}\n {obs.frame[0][29]}\n {obs.frame[0][30]}\n {obs.frame[0][31]}\n {obs.frame[0][32]}\n {obs.frame[0][33]}\n {obs.frame[0][34]}\n {obs.frame[0][35]}\n {obs.frame[0][36]}\n {obs.frame[0][37]}\n {obs.frame[0][38]}\n {obs.frame[0][39]}\n {obs.frame[0][40]}\n {obs.frame[0][41]}\n {obs.frame[0][42]}\n {obs.frame[0][43]}\n {obs.frame[0][44]}\n {obs.frame[0][45]}\n {obs.frame[0][46]}\n {obs.frame[0][47]}\n {obs.frame[0][48]}\n {obs.frame[0][49]}\n {obs.frame[0][50]}\n {obs.frame[0][51]}\n {obs.frame[0][52]}\n {obs.frame[0][53]}\n {obs.frame[0][54]}\n {obs.frame[0][55]}\n {obs.frame[0][56]}\n {obs.frame[0][57]}\n {obs.frame[0][58]}\n {obs.frame[0][59]}\n {obs.frame[0][60]}\n {obs.frame[0][61]}\n {obs.frame[0][62]}\n {obs.frame[0][63]}\n')
obs = env.observation_space
if obs:
    print(f"Game state: {obs}")
    print(f"Levels completed: {obs.levels_completed}")

# Check your scorecard
#print(arc.get_scorecard())