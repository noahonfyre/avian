@echo off

cd ..
python -m pip install uv
python -m uv pip install -e .
python -m uv run main.py

echo uv setup concluded.