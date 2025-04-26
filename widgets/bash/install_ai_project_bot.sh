#!/bin/bash
set -e

echo "=== Installing dependencies ==="

# Detect package manager
if command -v apt &>/dev/null; then
	sudo apt update
	sudo apt install -y python3 python3-venv python3-pip git curl
elif command -v brew &>/dev/null; then
	brew install python3 git
else
	echo "❌ Unsupported OS. Please install Python 3.9+, pip, and venv manually."
	exit 1
fi

echo "=== Creating Python virtual environment ==="
mkdir -p ~/ai-project-bot && cd ~/ai-project-bot
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

echo "=== Installing required Python libraries ==="
pip install torch transformers accelerate duckdb huggingface-hub

echo "=== Saving AIBot Python file ==="
cat <<EOF > bot.py
<INSERT PYTHON CODE HERE>
EOF

echo "=== Running AIBot for test project ==="
python3 bot.py