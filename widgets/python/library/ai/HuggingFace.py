import os
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    pipeline,
    AutoProcessor,
    AutoModelForSpeechSeq2Seq,
    AutoModelForVision2Seq,
)

class HuggingFaceGPT:
    """💡 Hugging Face Assistant class supporting chat, vision, audio, TTS, and embeddings."""

    def __init__(self, model="mistralai/Mistral-7B-Instruct-v0.1", token_mode="m"):
        self.model_name = model
        self.device = 0 if torch.cuda.is_available() else -1
        self.tokenizer = AutoTokenizer.from_pretrained(model)
        self.model = AutoModelForCausalLM.from_pretrained(model, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32).to(self.device)
        self.token_limit = self._resolve_token_limit(token_mode)
        self.messages = []

    def _resolve_token_limit(self, mode):
        mode = mode.lower()[0]
        return {
            "t": 128,
            "s": 512,
            "m": 1024,
            "l": 2048,
            "h": 4096,
            "x": 8192,
        }.get(mode, 1024)

    def set_model(self, model):
        """🔁 Change the chat model dynamically."""
        self.model_name = model
        self.tokenizer = AutoTokenizer.from_pretrained(model)
        self.model = AutoModelForCausalLM.from_pretrained(model).to(self.device)

    def reset_conversation(self):
        """🔄 Reset chat history."""
        self.messages = []

    def chat(self, prompt, system_prompt="You are a helpful assistant."):
        """💬 Stateful conversation with simulated chat history."""
        self.messages.append({"role": "user", "content": prompt})
        history = f"{system_prompt}\n"
        for msg in self.messages:
            history += f"{msg['role'].capitalize()}: {msg['content']}\n"

        inputs = self.tokenizer(history, return_tensors="pt", truncation=True, max_length=self.token_limit).to(self.device)
        output = self.model.generate(**inputs, max_new_tokens=256)
        result = self.tokenizer.decode(output[0], skip_special_tokens=True)
        response = result.split("Assistant:")[-1].strip()
        self.messages.append({"role": "assistant", "content": response})
        return response

    def prompt(self, prompt):
        """⚡ One-shot stateless prompt (no history)."""
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        output = self.model.generate(**inputs, max_new_tokens=256)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def vision(self, image_path):
        """🖼️ Image captioning or analysis (requires BLIP2/GIT model)."""
        processor = AutoProcessor.from_pretrained(self.model_name)
        model = AutoModelForVision2Seq.from_pretrained(self.model_name).to(self.device)
        from PIL import Image
        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt").to(self.device)
        output = model.generate(**inputs)
        return processor.decode(output[0], skip_special_tokens=True)

    def transcribe(self, audio_path):
        """📝 Transcribe audio to text using Whisper."""
        whisper = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=self.device)
        return whisper(audio_path)["text"]

    def translate(self, audio_path):
        """🌍 Translate non-English audio to English using Whisper."""
        whisper = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=self.device)
        return whisper(audio_path, generate_kwargs={"task": "translate"})["text"]

    def speech(self, text, output_file="speech.wav"):
        """🔊 Text-to-speech using ESPNet VITS model."""
        tts = pipeline("text-to-speech", model="espnet/kan-bayashi_ljspeech_vits", device=self.device)
        audio = tts(text)
        with open(output_file, "wb") as f:
            f.write(audio["wav"])
        return output_file

    def embed(self, text):
        """📌 Get vector embedding using sentence-transformers."""
        embedder = pipeline("feature-extraction", model="sentence-transformers/all-MiniLM-L6-v2", device=self.device)
        return embedder(text)[0]

    def list_supported_models(self):
        """📘 Return supported models by type."""
        return {
            "chat": [
                "mistralai/Mistral-7B-Instruct-v0.1",
                "NousResearch/Nous-Hermes-2-Mistral-7B",
                "meta-llama/Llama-2-7b-chat-hf",
                "openchat/openchat-3.5-0106",
                "HuggingFaceH4/zephyr-7b-beta",
            ],
            "vision": [
                "Salesforce/blip-image-captioning-base",
                "Salesforce/blip2-opt-2.7b",
                "microsoft/git-large-r-textcaps",
            ],
            "tts": [
                "espnet/kan-bayashi_ljspeech_vits"
            ],
            "audio": [
                "openai/whisper-base",
                "openai/whisper-small",
                "openai/whisper-medium",
            ],
            "embedding": [
                "sentence-transformers/all-MiniLM-L6-v2",
                "sentence-transformers/all-mpnet-base-v2",
            ]
        }
