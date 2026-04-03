# Welcome!

In this workshop, you'll build a lightweight AI agent from scratch --  
one that can recognize when it needs external information, call a tool to get it, and continue the conversation based on real results.

You'll see how modern LLMs can:
- Detect when a tool call is needed.
- Call those tools automatically.
- Dynamically adjust their behavior based on new information.

All running **locally** using **Gemma 4** through **Ollama** -- with no cloud dependencies and no unnecessary complexity.

Later, we'll extend this by using the **Model Context Protocol (MCP)** to let models dynamically discover and use tools at runtime.

This workshop was inspired in part by a talk given by **Ravin Kumar** during [Hugo Bowne-Anderson's course, *Building LLM-Powered Applications for Data Scientists and Software Engineers*](https://maven.com/s/course/d56067f338).

---

## What You'll Build

The workshop is divided into three progressive phases:

---

### Phase 0: Building a Basic LLM App Locally

You'll start by setting up a simple but complete local application:
- Connect to a local Gemma 4 model using Ollama.
- Send basic prompts and receive responses.
- Build a basic Gradio UI to interact with the model.
- Log prompts and responses into a SQLite database for observability.

This gives you a working foundation before we introduce tool use and agentic behavior.

---

### Phase 1: Basic Agent with Manual Tool Calling

After building the base app, you'll create your first real agent:
- Use system prompts to teach the model when to suggest calling a function.
- Parse the model's outputs to detect when a tool call is needed.
- Call the appropriate Python function.
- Optionally reinject the tool result back into the model to generate a better final user-facing response.

You'll also build a simple Gradio app that shows:
- What the user sees.
- What happened under the hood (tool calls and tool results).

---

### Phase 2: Discoverable Tools with the Model Context Protocol (MCP)

Finally, you'll move from hardcoded tool lists to a dynamic system:
- Run a simple MCP server that exposes available tools.
- Let the agent discover tools at runtime without needing to be explicitly told in advance.
- Understand how MCP changes the architecture of agent systems.

---

## Recording

This workshop was live-streamed on YouTube. Each notebook has the corresponding section linked at the top.

- [Full stream](https://youtube.com/live/-IWstEStqok?feature=share)
- Part 1 (AI Agent MVP): [5:30](https://www.youtube.com/live/-IWstEStqok?t=330)
- Part 2 (Basic Function Calls): [34:48](https://www.youtube.com/live/-IWstEStqok?t=2088)
- Part 3 (MCP): [1:26:20](https://www.youtube.com/live/-IWstEStqok?t=5180) -- code in `apps/`, link embedded at the end of notebook 2

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

Start with `notebooks/1-ai-app-mvp.ipynb` and work through them in order.

---

## Quick Note on Hardware

- You should have at least **16GB of RAM** to run Gemma 4 comfortably.
- Model downloads can be large (~10GB).

Running locally is part of the hands-on experience: you'll encounter real-world constraints and learn how to work with them.
