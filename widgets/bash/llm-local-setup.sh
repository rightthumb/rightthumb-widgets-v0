#!/bin/bash
set -e

# === Help Menu ===
if [[ $# -eq 0 || "$1" == "--help" || "$1" == "-h" ]]; then
    echo ""
    echo "GPT Local Setup: Self-Hosted Model Installer"
    echo ""
    echo "Usage:"
    echo "  ./gpt-local-setup.sh [--code] [--llm] [--image] [--audio] [--video]"
    echo ""
    echo "Options:"
    echo "  --code           Setup an open-source code model"
    echo "  --llm            Setup a general-purpose language model"
    echo "  --image          Setup an image generation model"
    echo "  --audio          Setup a speech/audio model"
    echo "  --video          Setup a video model"
    echo ""
    exit 0
fi

# === Defaults ===
MODE=""
MODEL=""
TRANSFORMERS_CACHE="./model-cache"

# === Model dictionaries ===
declare -A CODE_MODELS=(
    ["wizardcoder"]="WizardLM/WizardCoder-Python-7B-V1.0"
    ["codellama7b"]="codellama/CodeLlama-7b-Python-hf"
    ["starcoder"]="bigcode/starcoder"
    ["granite8b"]="ibm-granite/granite-code-8b"
    ["deepseekcoder"]="deepseek-ai/deepseek-coder-6.7b-instruct"
    ["codestral"]="mistralai/Codestral-22B"
)

declare -A LLM_MODELS=(
    ["falcon7b"]="tiiuae/falcon-7b-instruct"
    ["mistral7b"]="mistralai/Mistral-7B-Instruct-v0.1"
    ["zephyr7b"]="HuggingFaceH4/zephyr-7b-beta"
    ["llama3-8b"]="meta-llama/Meta-Llama-3-8B-Instruct"
    ["phi-2"]="microsoft/phi-2"
    ["stablelm2"]="stabilityai/stablelm-2-1_6b"
    ["bloomz-7b1"]="bigscience/bloomz-7b1"
    ["mixtral"]="mistralai/Mixtral-8x7B-Instruct-v0.1"
)

declare -A IMAGE_MODELS=(
    ["sdxl"]="stabilityai/stable-diffusion-xl-base-1.0"
    ["sdv1-4"]="CompVis/stable-diffusion-v1-4"
)

declare -A AUDIO_MODELS=(
    ["whisper-large"]="openai/whisper-large-v3"
    ["distil-medium"]="distil-whisper/medium.en"
)

declare -A VIDEO_MODELS=(
    ["animate-anyone"]="AlibabaResearch/animate-anyone"
    ["mask2former"]="facebook/mask2former"
)

# === Parse args ===
while [[ $# -gt 0 ]]; do
    case "$1" in
        --code)
            MODE="code"
            shift
            ;;
        --llm)
            MODE="llm"
            shift
            ;;
        --image)
            MODE="image"
            shift
            ;;
        --audio)
            MODE="audio"
            shift
            ;;
        --video)
            MODE="video"
            shift
            ;;
        *)
            echo "❌ Unknown argument: $1"
            exit 1
            ;;
    esac
done

# === Select model ===
if [[ -z "$MODE" ]]; then
    echo "❌ You must specify a mode: --code, --llm, --image, --audio, or --video"
    exit 1
fi

choose_model() {
    declare -n models=$1
    echo -e "\n=== Available Models ($MODE) ==="
    for key in "${!models[@]}"; do
        echo "  [$key] ${models[$key]}"
    done
    echo -n "Enter the key of the model to use: "
    read model_key
    MODEL="${models[$model_key]}"
    if [[ -z "$MODEL" ]]; then
        echo "❌ Invalid model key."
        exit 1
    fi
}

case "$MODE" in
    code)
        choose_model CODE_MODELS
        ;;
    llm)
        choose_model LLM_MODELS
        ;;
    image)
        choose_model IMAGE_MODELS
        ;;
    audio)
        choose_model AUDIO_MODELS
        ;;
    video)
        choose_model VIDEO_MODELS
        ;;
esac

echo -e "\n=== Selected model: $MODEL ==="

# === Install dependencies ===
echo "\n=== Installing Python + pip + venv ==="
if command -v apt &>/dev/null; then
    sudo apt update
    sudo apt install -y python3 python3-venv git curl
elif command -v brew &>/dev/null; then
    brew install python3 git
else
    echo "❌ Unsupported OS. Install Python 3.9+, pip, and venv manually."
    exit 1
fi

# === Setup Python environment ===
echo "\n=== Creating virtual environment ==="
mkdir -p ~/gptlocal && cd ~/gptlocal
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

echo "\n=== Installing required libraries ==="
pip install torch transformers accelerate diffusers librosa torchvision

# === Write Python inference script ===
echo "\n=== Writing Python script ==="
export TRANSFORMERS_CACHE

cat <<EOF > gpt_infer.py
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

model_name = "$MODEL"

if "$MODE" in ["llm", "code"]:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
    prompt = "Write a bash script that backs up /home to /backup with a timestamp." if "$MODE" == "code" else "What is the capital of Japan?"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_new_tokens=200)
    print(tokenizer.decode(output[0], skip_special_tokens=True))
else:
    print(f"Setup for {model_name} complete. Run your specialized script for inference.")
EOF

# === Run a test ===
echo "\n=== Running query ==="
python gpt_infer.py

# === Show Python code ===
echo "\n=== Python code used ==="
cat gpt_infer.py

# === Done ===
echo "\n✅ Setup complete!"
