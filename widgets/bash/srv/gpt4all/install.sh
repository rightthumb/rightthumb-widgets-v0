#!/bin/bash

set -e

# === CONFIG ===
MODEL_NAME="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
MODEL_URL="https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/${MODEL_NAME}"
MODEL_DIR="$HOME/gpt4all/models"
LLAMA_DIR="$HOME/llama.cpp"

# === Pip ===
pip3 install --upgrade pip
pip3 install gpt4all
pip3 install llama-cpp-python
pip3 install huggingface-hub
pip3 install --upgrade gpt4all
pip3 install --upgrade llama-cpp-python
pip3 install --upgrade huggingface-hub


# === DETECT OS AND INSTALL DEPENDENCIES ===
echo "\n🧠 Detecting OS and installing dependencies..."
if [ -f /etc/redhat-release ]; then
    echo "📦 RHEL/AlmaLinux detected"
    sudo dnf install -y git gcc gcc-c++ make cmake wget unzip libuv libuv-devel curl-devel
elif [ -f /etc/debian_version ]; then
    echo "📦 Debian/Ubuntu detected"
    sudo apt update
    sudo apt install -y build-essential cmake git wget unzip libcurl4-openssl-dev
elif [ -f /etc/arch-release ]; then
    echo "📦 Arch Linux detected"
    sudo pacman -Sy --noconfirm base-devel cmake git wget curl
else
    echo "❌ Unsupported OS"
    exit 1
fi

# === DOWNLOAD MODEL ===
echo "\n📁 Preparing model directory..."
mkdir -p "$MODEL_DIR"
cd "$MODEL_DIR"

if [ ! -f "$MODEL_NAME" ]; then
    echo "⬇️ Downloading TinyLlama model from Hugging Face..."
    wget -O "$MODEL_NAME" "$MODEL_URL" || {
        echo "❌ Failed to download model. Check URL or use huggingface-cli manually.";
        exit 1;
    }
else
    echo "✅ Model already present: $MODEL_NAME"
fi

# === CLONE AND BUILD LLAMA.CPP ===
echo "\n🐑 Cloning llama.cpp if not already present..."
cd ~
if [ ! -d "$LLAMA_DIR" ]; then
    git clone https://github.com/ggerganov/llama.cpp.git
fi
cd "$LLAMA_DIR"
mkdir -p build && cd build

echo "🔨 Building llama.cpp (CPU-only, no server)..."
cmake .. -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF
cmake --build . --config Release -j$(nproc)

# === TEST CHAT ===
echo "\n💬 Launching chat..."
CHAT_BIN="$LLAMA_DIR/build/bin/chat"
if [ -f "$CHAT_BIN" ]; then
    "$CHAT_BIN" -m "$MODEL_DIR/$MODEL_NAME"
else
    echo "❌ Chat binary not found. Try running: cmake --build . --target chat"
fi

# === OPTIONAL: ADD SHORTCUT ===
echo "\n🔗 Creating gpt4chat shortcut..."
echo -e "#!/bin/bash\n$CHAT_BIN -m $MODEL_DIR/$MODEL_NAME \"\$@\"" | sudo tee /usr/local/bin/gpt4chat >/dev/null
sudo chmod +x /usr/local/bin/gpt4chat

echo "\n🎉 All done! Launch chat anytime with: gpt4chat"

# /root/llama.cpp/build/bin/llama-cli   -m /root/gpt4all/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf   -p "Hello, who are you?"   -n 128 -t 8