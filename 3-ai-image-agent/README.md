# Welcome!

In this workshop, we'll dig into the image capabilities of the Gemma series.

We'll:
- Extract structured information from images (e.g. OCR on receipts)
- Classify and count objects using LLMs
- Route behavior based on image content
- Prototype image-to-action workflows (e.g. "if dog, then...")

All running **locally** using **Gemma 4** through **Ollama** -- with no cloud dependencies and no unnecessary complexity.

This workshop was inspired in part by a talk given by **Ravin Kumar** during [Hugo Bowne-Anderson's course, *Building LLM-Powered Applications for Data Scientists and Software Engineers*](https://maven.com/s/course/d56067f338).

---

## What You'll Build

The workshop is divided into three progressive phases:

---

### Phase 0: Get started with image workflows locally

You'll start by setting up a simple but complete local application:
- Connect to a local Gemma 4 model using Ollama.
- Send basic prompts and receive responses.
- Build a basic Gradio UI to interact with the model that takes in images.

---

### Phase 1: Various image capabilities of Gemma

After a basic prompting we'll show various image capabilities:
- Object recognition
- Counting
- OCR

---

### Phase 2: Connect everything together with Gradio

Finally, you'll connect the pieces into a complete system:
- Add all this to Gradio
- Make the image input seamless for users
- Use the LLM to provide routed responses

---

## Recording

This workshop was live-streamed on YouTube. Each notebook has the corresponding section linked at the top.

- [Full stream](https://youtube.com/live/FNlM7lSt8Uk?feature=share)
- Part 1 (Ollama Basics): [3:51](https://www.youtube.com/live/FNlM7lSt8Uk?t=231)
- Part 2 (Basic Image Calls): [22:09](https://www.youtube.com/live/FNlM7lSt8Uk?t=1329)
- Part 3 (Model Routing): [52:06](https://www.youtube.com/live/FNlM7lSt8Uk?t=3126)

---

## Getting Started

To run this workshop locally, you'll need **Ollama** and a working **Python 3.9+ environment**.

---

### 1. Install Ollama

Download and install Ollama from [https://ollama.com/](https://ollama.com/).

Then pull the required models:

```bash
ollama pull gemma4:latest
```

---

### 2. Set up your Python environment

We recommend using `uv` for managing dependencies.

```bash
pip install uv
uv venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

---

### 3. Running the Materials

- **Notebooks** are located in the `notebooks/` folder.
- **Gradio apps** and other small scripts are in the `apps/` folder.

Start with `notebooks/0-ollama-basics.ipynb` and work through them in order.

---

## Quick Note on Hardware

- You should have at least **16GB of RAM** to run Gemma 4 comfortably.
- Model downloads can be large (~10GB).

Running locally is part of the hands-on experience: you'll encounter real-world constraints and learn how to work with them.
