@echo off

cd ..
uv pip install -e .
uv run main.py

echo uv setup concluded.