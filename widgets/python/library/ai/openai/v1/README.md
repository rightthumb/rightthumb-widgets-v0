# GPT Assistant: class for interacting with OpenAI's GPT models

## Usage documentation

### 🧠 Initialize the Assistant

~~~python
from library.ai.gpt import  GPT

# Create an assistant with default GPT-4o model and medium token limit
gpt = GPT(token_mode="m")  # t, s, m, l, h, x (tiny to max)
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

### 📷 Vision (Image + Prompt)

~~~python
# Analyze image using GPT-4o vision
desc = gpt.vision("What's in this image?", "cat.jpg")
print(desc)
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

### 🗣️ Text-to-Speech

~~~python
# Generate spoken MP3 file from text
output = gpt.speech("Welcome to the AI assistant demo.", voice="nova", output_file="demo.mp3")
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
# Available models

gpt.set_model("gpt-4o")              # Best for everything (text, vision, audio)
gpt.set_model("gpt-4-turbo")         # Fast, cost-effective GPT-4
gpt.set_model("gpt-3.5-turbo")       # Budget GPT-3.5
gpt.set_model("gpt-4o")              # Supports tools (functions, vision, files)
gpt.set_model("gpt-4-turbo")         # Supports tools (functions, files)
gpt.set_model("whisper-1")           # Speech-to-text and translation
gpt.set_model("tts-1")               # Base voice model
gpt.set_model("tts-1-hd")            # High-definition voice model
gpt.set_model("text-embedding-3-small")   # Fast, lower-cost
gpt.set_model("text-embedding-3-large")   # More accurate

# Explanation of how to use these below
~~~

___
___

#### 🧠 Model Usage Key

~~~yaml
chat:
  - gpt-4o              # Chat + vision + audio input
  - gpt-4-turbo         # Chat + tools (functions/files)
  - gpt-3.5-turbo       # Chat only

vision:
  - gpt-4o              # Only GPT-4o supports vision

tts:
  - tts-1               # Base model
  - tts-1-hd            # High-definition model

voices:
  - alloy
  - echo
  - fable
  - onyx
  - nova
  - shimmer

audio:
  - whisper-1           # Used for both transcribe and translate

embedding:
  - text-embedding-3-small
  - text-embedding-3-large
~~~

___
___

## 🧠 gpt.set_model({model})

* **Chat**
* **Vision**
* **Text-to-Speech (TTS)**
* **Transcription/Translation (Whisper)**
* **Embeddings**

___

### 🧠 Chat & Vision (for `chat()` / `prompt()` / `vision()`)

~~~python
gpt.set_model("gpt-4o")               # Best for everything (text, vision, audio)
gpt.set_model("gpt-4-turbo")         # Fast, cost-effective GPT-4
gpt.set_model("gpt-3.5-turbo")       # Budget GPT-3.5
~~~

> ✅ `gpt-4o` supports vision and audio-based inputs
> 🚫 `gpt-3.5-turbo` does **not** support image/audio

___

### 🧠 Chat With Tools (functions, retrieval, etc.)

~~~python
gpt.set_model("gpt-4o")              # Supports tools (functions, vision, files)
gpt.set_model("gpt-4-turbo")         # Supports tools (functions, files)
~~~

> ⚠️ These are dynamically routed via `ChatCompletion.create()`, so no change in format needed—just model name.

___

### 🎧 Whisper for Transcription/Translation

~~~python
# Only for gpt.transcribe() and gpt.translate()
gpt.set_model("whisper-1")           # Speech-to-text and translation
~~~

___

### 🗣️ TTS (Text-to-Speech)

~~~python
# Only for gpt.speech()
gpt.set_model("tts-1")               # Base voice model
gpt.set_model("tts-1-hd")            # High-definition voice model
~~~

> Voice options include: `"alloy"`, `"echo"`, `"fable"`, `"onyx"`, `"nova"`, `"shimmer"`

___

### 🔢 Embeddings

~~~python
# Only for gpt.embed()
gpt.set_model("text-embedding-3-small")   # Fast, lower-cost
gpt.set_model("text-embedding-3-large")   # More accurate
~~~
