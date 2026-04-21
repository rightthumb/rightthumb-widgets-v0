#!/bin/bash
set -e

echo "=== Installing dependencies ==="

# Detect package manager or existing Python
if command -v apt &>/dev/null; then
	sudo apt update
	sudo apt install -y python3 python3-venv python3-pip git curl
elif command -v brew &>/dev/null; then
	brew install python3 git
elif command -v python3 &>/dev/null; then
	echo "✅ Python 3 already installed: $(python3 --version)"
	echo "⚡ Skipping package manager installation."
else
	echo "❌ No supported package manager found and Python 3 missing."
	exit 1
fi

echo "=== Creating Python virtual environment ==="
mkdir -p ~/ai-project-bot && cd ~/ai-project-bot
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

echo "=== Installing required Python libraries ==="
pip install transformers accelerate duckdb huggingface-hub
pip install torch --index-url https://download.pytorch.org/whl/cpu

echo "=== Saving AIBot Python file ==="
cat <<EOF > bot.py
<INSERT PYTHON CODE HERE>
EOF

echo "=== Running AIBot for test project ==="
python3 bot.py