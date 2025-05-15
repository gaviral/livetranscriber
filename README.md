# livetranscriber

A zero-dependency **single-file** helper that streams microphone audio to Deepgram for real-time speech-to-text. This is available as a package on PyPI.

## Features

*   **Simple API** - single `LiveTranscriber` class.
*   **Configurable** - every Deepgram *LiveOptions* parameter can be overridden via keyword arguments; sensible Nova-3 defaults are provided.
*   **Mandatory callback** - forces the calling code to supply a function that will be invoked for every *final* transcript chunk (empty / interim chunks are ignored).
*   **Output capture** - optional `output_path` writes each final transcript line to disk.
*   **Pause / resume** - you may call `pause` or `resume` from your callback.
*   **Graceful shutdown** - Ctrl-C or `stop` shuts everything down and releases resources.

## Installation

Install the package directly from PyPI using pip:

```bash
pip install livetranscriber
```

Alternatively, if you are working with the source code or a specific requirements file, you can install the dependencies listed in `requirements.txt`:

```
deepgram-sdk>=4,<5
numpy>=1.24  # build-time requirement of sounddevice
sounddevice>=0.4
```

Install with `uv` (preferred) or plain `pip`:

```bash
uv venv .venv && source .venv/bin/activate
uv pip install -r requirements.txt
```
or
```bash
pip install -r requirements.txt
```

2.  **Python Version:**

    Python 3.11 is required.

## Environment Setup

Export your Deepgram API key (see https://console.deepgram.com). For persistent access, add the following line to your shell profile file (e.g., `~/.zshrc`, `~/.bashrc`, or `~/.profile`) and restart your terminal or source the file:

```bash
export DEEPGRAM_API_KEY="dg_…"
```

## Example Usage

Here is a minimal example to get you started:

```python
from livetranscriber import LiveTranscriber

def simple_callback(text: str):
    """A simple callback that prints the transcript."""
    print("NEW >", text)

# Instantiate with the mandatory callback
tr = LiveTranscriber(callback=simple_callback)

try:
    print("Starting transcription. Press Ctrl+C to stop.")
    tr.run() # Blocks until stop() is called or Ctrl-C is pressed
except KeyboardInterrupt:
    print("\nCtrl+C detected. Stopping.")
finally:
    print("Transcription ended.")

Here is a more comprehensive example demonstrating various features:

```