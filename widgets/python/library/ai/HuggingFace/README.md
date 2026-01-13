# Hugging Face GPT Assistant: class for interacting with HF models (chat, vision, audio, embeddings)

## Usage documentation

### 🧠 Initialize the Assistant

~~~python
from huggingface_gpt import HuggingFaceGPT

# Create an assistant with default model and medium token limit
gpt = HuggingFaceGPT(token_mode="m")  # t, s, m, l, h, x (tiny to max)
~~~

___

### 💬 Chat (Persistent Conversation)

~~~python
# Maintains context across multiple prompts
response = gpt.chat("What are the pros and cons of nuclear energy?")
print(response)

# Continue conversation
followup = gpt.chat("Can you give a real-world example?")
print(followup)
~~~

___

### 🧹 One-shot Chat (Stateless)

~~~python
# Send a single prompt without conversation memory
print(gpt.prompt("Summarize 'The Great Gatsby' in 2 sentences."))
~~~

___

### 📷 Vision (Image Captioning)

~~~python
# Analyze image using BLIP/GIT/BLIP2
caption = gpt.vision("cat.jpg")
print(caption)
~~~

___

### 🎙️ Transcribe Audio

~~~python
# Transcribe spoken words in audio to text using Whisper
text = gpt.transcribe("recording.mp3")
print(text)
~~~

___

### 🌍 Translate Audio to English

~~~python
# Translate non-English audio to English
english = gpt.translate("spanish_clip.mp3")
print(english)
~~~

___

### 🔊 Text-to-Speech

~~~python
# Generate spoken WAV file from text
output = gpt.speech("Welcome to the AI assistant demo.", output_file="demo.wav")
print(f"Saved to: {output}")
~~~

___

### 🔢 Embedding Vector

~~~python
# Get high-dimensional vector representation of text
vector = gpt.embed("Artificial intelligence is transforming the world.")
print(vector[:5])  # Preview first 5 dimensions
~~~

___

### 🔄 Reset Conversation

~~~python
# Clear all memory from current conversation
gpt.reset_conversation()
~~~

___

### ⚙️ Change Model on the Fly

~~~python
# Switch between supported Hugging Face models
gpt.set_model("mistralai/Mistral-7B-Instruct-v0.1")
gpt.set_model("NousResearch/Nous-Hermes-2-Mistral-7B")
gpt.set_model("meta-llama/Llama-2-7b-chat-hf")
gpt.set_model("Salesforce/blip2-opt-2.7b")
gpt.set_model("openai/whisper-base")
gpt.set_model("espnet/kan-bayashi_ljspeech_vits")
gpt.set_model("sentence-transformers/all-MiniLM-L6-v2")
~~~

___
___

#### 🧠 Model Usage Key

~~~yaml
chat:
  - mistralai/Mistral-7B-Instruct-v0.1       # Chat
  - NousResearch/Nous-Hermes-2-Mistral-7B    # Chat
  - meta-llama/Llama-2-7b-chat-hf            # Chat

vision:
  - Salesforce/blip-image-captioning-base    # Basic captioning
  - Salesforce/blip2-opt-2.7b                # Advanced vision + language
  - microsoft/git-large-r-textcaps           # Rich image-to-text

tts:
  - espnet/kan-bayashi_ljspeech_vits         # TTS model (wav)

audio:
  - openai/whisper-base                      # Transcription + translation
  - openai/whisper-small
  - openai/whisper-medium

embedding:
  - sentence-transformers/all-MiniLM-L6-v2   # Fast, lightweight
  - sentence-transformers/all-mpnet-base-v2  # High accuracy
~~~

___
___

## 🧠 gpt.set\_model({model})

* **Chat**
* **Vision**
* **Text-to-Speech (TTS)**
* **Transcription/Translation (Whisper)**
* **Embeddings**

___

### 🧠 Chat (for `chat()` / `prompt()`)

~~~python
gpt.set_model("mistralai/Mistral-7B-Instruct-v0.1")
gpt.set_model("NousResearch/Nous-Hermes-2-Mistral-7B")
gpt.set_model("meta-llama/Llama-2-7b-chat-hf")
~~~

___

### 📷 Vision

~~~python
gpt.set_model("Salesforce/blip2-opt-2.7b")
gpt.set_model("microsoft/git-large-r-textcaps")
~~~

___

### 🎙️ Whisper for Transcription/Translation

~~~python
gpt.set_model("openai/whisper-base")
~~~

___

### 🔊 TTS (Text-to-Speech)

~~~python
gpt.set_model("espnet/kan-bayashi_ljspeech_vits")
~~~

___

### 🔢 Embeddings

~~~python
gpt.set_model("sentence-transformers/all-MiniLM-L6-v2")
gpt.set_model("sentence-transformers/all-mpnet-base-v2")
~~~
