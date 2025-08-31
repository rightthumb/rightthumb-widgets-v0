import os
import openai # type: ignore
import base64

try: import _rightThumb._base3 as _ # type: ignore
except: pass

class GPT: # GPT Assistant: class for interacting with OpenAI's GPT models
    def __init__(self, api_key=None, model="gpt-4o", token_mode="m"):
        try:     key = _.fig['openai'] if 'openai' in _.fig else False
        except:  key = False
        self.api_key = api_key or key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key not set. Set OPENAI_API_KEY or pass it to the constructor.")
        openai.api_key = self.api_key

        self.model = model
        self.messages = []
        self.token_limit = self._resolve_token_limit(token_mode)

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
        self.model = model

    def reset_conversation(self):
        self.messages = []

    def chat(self, prompt, system_prompt="You are a helpful assistant.", temperature=0.7):
        if not self.messages:
            self.messages.append({"role": "system", "content": system_prompt})
        self.messages.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=temperature,
            max_tokens=self.token_limit,
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def prompt(self, prompt, system_prompt="You are a helpful assistant.", temperature=0.7):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=self.token_limit,
        )
        return response.choices[0].message.content

    def vision(self, prompt, image_path):
        with open(image_path, "rb") as f:
            b64_image = base64.b64encode(f.read()).decode("utf-8")

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_image}"}}
                ]
            }],
            max_tokens=self.token_limit,
        )
        return response.choices[0].message.content

    def transcribe(self, audio_path):
        with open(audio_path, "rb") as f:
            result = openai.Audio.transcribe("whisper-1", f)
        return result['text']

    def translate(self, audio_path):
        with open(audio_path, "rb") as f:
            result = openai.Audio.translate("whisper-1", f)
        return result['text']

    def speech(self, text, voice="alloy", output_file="speech.mp3"):
        response = openai.Audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )
        with open(output_file, "wb") as f:
            f.write(response.content)
        return output_file

    def embed(self, text):
        response = openai.Embedding.create(
            input=[text],
            model="text-embedding-3-small"
        )
        return response['data'][0]['embedding']

    def list_supported_models(self):
        """
        Returns a dictionary of supported models categorized by type.
        """
        return {
            "chat": [
                "gpt-4o",              # Chat + vision + audio input
                "gpt-4-turbo",         # Chat + tools (functions/files)
                "gpt-3.5-turbo",       # Chat only
            ],
            "vision": [
                "gpt-4o",              # Only GPT-4o supports vision
            ],
            "tts": [
                "tts-1",               # Base model
                "tts-1-hd",            # High-definition model
            ],
            "voices": [
                "alloy", "echo", "fable", "onyx", "nova", "shimmer"
            ],
            "audio": [
                "whisper-1",           # Used for both transcribe and translate
            ],
            "embedding": [
                "text-embedding-3-small",
                "text-embedding-3-large",
            ]
        }
