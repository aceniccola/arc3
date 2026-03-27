action:
	uv run ARC-AGI-3-Agents/main.py --agent=action

local:
	python run_local.py

install:
	uv venv
	cd ARC-AGI-3-Agents && UV_PROJECT_ENVIRONMENT=venv uv sync --all-extras
	uv pip install -r requirements.txt

tensorboard:
	.venv/bin/tensorboard --logdir=runs --port=6006

clean:
	rm -r ./runs