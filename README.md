# Gemma 4 Workshops

Three hands-on workshops for building AI products locally with [Gemma 4](https://ollama.com/library/gemma4) via [Ollama](https://ollama.com/). Built by [Ravin Kumar](https://canyon289.github.io/) (Google DeepMind) and [Hugo Bowne-Anderson](https://hugobowne.substack.com/) (Vanishing Gradients).

Everything runs locally and privately on your own machine: no cloud dependencies required.

If you find this helpful, please star the repository and share it with a friend. For more independent AI education like this, [subscribe to our Substack](https://hugobowne.substack.com/).

We're planning to expand this material and run more workshops on local LLMs and building AI products with them. If you want to be first to hear about it, [let us know what you're interested in here](https://tally.so/r/EkLjyA).

These are updated versions of the original workshops (recorded with Gemma 2/3), now migrated to Gemma 4.

**Note:** You may notice that the first part of each workshop (setting up Ollama, building a Gradio UI, logging to SQLite) is similar across all three. This is intentional: each workshop is designed to be self-contained, so you can jump straight into Workshop 2 or 3 without needing to complete the earlier ones.

Beyond the migration to Gemma 4, we've also started adding new material that takes advantage of Gemma 4's capabilities, including thinking mode in Workshops 1 and 2, and native function calling/tool calling in Workshops 2 and 3. We'll also be adding audio processing capabilities once support lands in Ollama (or we find another way to do it locally). Let us know what else you'd like to see!

> **Original workshop recordings and blog post:** [Build AI Products Locally: 10 Hours of Free Workshops](https://hugobowne.substack.com/p/build-ai-products-locally-10-hours)

## Workshops

### Workshop 1: Building AI Apps for Real-World Use Cases
**Directory:** `1-ai-app-basics/`  
**Recording:** https://youtube.com/live/9zM_93mYdu8  
**Original repo:** https://github.com/canyon289/ai_app_basics

*Build your first local AI app end-to-end: model, data, front-end, database, evaluation, and optimization.*

#### 1. Building the MVP AI System

You'll start by building a complete AI system from scratch:

- Build a **zero-shot classification system** that predicts whether a sports team is from the US or Australia
- Integrate models, data, and a **Gradio front-end** and **SQLite database** for logging and observability
- Core model is Gemma 4, **running locally via Ollama**

#### 2. Vibe-Based Evaluation

**Before systematic evaluation**, you'll test things informally (with "vibes"):

- Try different prompts and see how the model responds
- Compare **local models against frontier models** like Gemini via Google AI Studio
- This is how LLM practitioners often start: **iterate, tweak, and experiment**

#### 3. Repeatable Evaluations with an Eval Harness

Once you have a feel for the model's behavior, you'll move to **repeatable, systematic evaluation**:

- Introduce an **evaluation harness**, a structured script for testing model performance
- **Programmatically test** the model across different datasets, starting with team names and expanding to real-world examples (e.g., news articles)
- Handle **ambiguous cases** (e.g., "Saints" exists in both US and Australian sports)

#### 4. Optimization

With a solid evaluation process in place, you'll optimize and refine the system:

- Try **different models** and compare performance using the eval harness
- Explore **model quantization** (Float32 to Int4) and its trade-offs for speed, cost, and output quality
- Learn rules of thumb for model selection: **start big, vibe check, then downsize**

Each notebook opens with an embedded YouTube player queued to the right section of the recording.


### Workshop 2: Building AI Agents with Gemma 4
**Directory:** `2-ai-agent-basics/`  
**Recording:** https://youtube.com/live/-IWstEStqok  
**Original repo:** https://github.com/canyon289/ai_agent_basics

*Build a local AI agent from scratch, from manual tool calling to discoverable tools with MCP.*

#### Phase 0: Building a Basic LLM App Locally

You'll start by setting up a simple but complete local application:

- Connect to a **local Gemma 4 model** using Ollama
- Send basic prompts and receive responses
- Build a basic **Gradio UI** to interact with the model
- Log prompts and responses into a **SQLite database** for observability
- This gives you a working foundation before introducing **tool use and agentic behavior**

#### Phase 1: Basic Agent with Manual Tool Calling

After building the base app, you'll create your first real agent:

- Use **system prompts** to teach the model when to suggest calling a function
- **Parse the model's outputs** to detect when a tool call is needed
- Call the appropriate Python function
- **Reinject the tool result** back into the model to generate a better final user-facing response
- Build a Gradio app that shows both what the user sees and **what happened under the hood**
- Discuss when to **fine-tune for function calling** and how to evaluate tool calls as binary classification

#### Phase 2: MCP and Dynamic Tool Discovery

Finally, you'll move from hardcoded tool lists to a dynamic system:

- Run a simple **MCP server** that exposes available tools
- Let the agent **discover tools at runtime** without needing to be explicitly told in advance
- Compare **local Gemma against hosted Gemini 2.5** via AI Studio for the same MCP tasks

Each notebook opens with an embedded YouTube player queued to the right section of the recording. The MCP section has no dedicated notebook; its code lives in `apps/` and the video link is embedded at the end of notebook 2.


### Workshop 3: From Images to Agents: Building Multimodal AI Workflows
**Directory:** `3-ai-image-agent/`  
**Recording:** https://youtube.com/live/FNlM7lSt8Uk  
**Original repo:** https://github.com/canyon289/ai_image_agent

*Teach a local LLM to see and act on images, then wire it into an agent.*

#### 1. Setting Up a Multimodal App

You'll set up a **local multimodal application**:

- Connect to a **local Gemma 4 model** using **Ollama**
- Send **basic prompts** and receive responses
- Build a **basic Gradio UI** to interact with the model that takes in images

#### 2. Image Understanding

After basic prompting, you'll explore Gemma's image capabilities:

- **Object recognition** and image classification (including a live **hot dog/not hot dog** classifier)
- **Counting** objects in images
- **OCR** on receipts and documents
- How **vision models compare to traditional dedicated OCR** and CNN pipelines

#### 3. Image-to-Action Workflows

Finally, you'll go beyond chat interfaces and build a **non-chat image workflow**:

- Classify an image, then **take an action** based on the result (write to file, send a message, trigger a function)
- Build a live **hot dog/not hot dog classifier** with audience-submitted images and an eval harness
- Wire it all into **Gradio** with seamless image input

Each notebook opens with an embedded YouTube player queued to the right section of the recording.


## Prerequisites

- **Hardware:** 16GB RAM minimum recommended
- **Ollama:** Download from [ollama.com](https://ollama.com/), then pull the model:
  ```bash
  ollama pull gemma4:latest
  ```
  Note: the model download is ~10GB.

- **Python 3.12+** with [uv](https://github.com/astral-sh/uv):
  ```bash
  pip install uv
  uv venv
  source .venv/bin/activate   # macOS/Linux
  # .venv\Scripts\activate    # Windows
  uv pip install -r requirements.txt
  ```
  Or install from the root `pyproject.toml` to get all dependencies at once:
  ```bash
  uv sync
  ```

Each workshop directory has its own `README.md` with setup steps specific to that workshop.

---

## Related Workshops (Colab-based)

Two additional workshops in this series are Colab-based and not included in this repo:

### Workshop 4: Fine-Tuning Open-Weight Language Models
**Recording:** https://youtube.com/live/jx4Ts-yoy2w  
**Notebooks:** [Colab 1](https://colab.research.google.com/drive/1J2i45upTf-S3uvPetrpenvME-MRKfOq5?usp=sharing), [Colab 2](https://colab.research.google.com/drive/1gDwOhRFTpljxClx1p6oEEpOFUnrigqgv?usp=sharing), [Colab 3](https://colab.research.google.com/drive/17ymVtMtyzYlIc3k8ACtoEaFXUATUvObJ?usp=sharing)

*Train a model to do what you want: classification, style transfer, and the deep learning essentials along the way.*

This workshop is broken down into three hands-on Colab notebooks. Start with the first and work your way through!

#### 1. Baselines and Prompting

You'll set up the environment and get a feel for the base model, Gemma-270M. Test its out-of-the-box capabilities on two tasks using only prompting, establishing a baseline and seeing where it falls short. This notebook answers the question: *Why do we need to fine-tune?*

- **Setup**: Load the model in Colab and connect to a free GPU
- **Prompting**: Test the model on two tasks:
  1. **Football Classification**: Can it tell Australian (AFL) from American (NFL) teams?
  2. **Alien Speech**: Can it role-play as a quirky alien NPC from a video game?
- **Baseline**: See the limits of prompting and learn when to system prompt vs when to fine-tune

#### 2. Fine-Tuning for Classification

Your first fine-tune. You'll focus on the structured **football classification** task and learn the complete workflow: preparing a dataset (90% of the work), running the training loop, and evaluating the results with hard numbers.

- **Data Prep**: Convert a simple list of teams into a conversational training dataset
- **Training**: Use the Hugging Face SFTTrainer to fine-tune the model
- **Deep Learning Essentials**: Interpret **training and validation loss curves** to see if your model is actually learning
- **Evaluation**: Re-run the test and see the improvement in classification accuracy

#### 3. Stylistic Fine-Tuning and LLM-as-a-Judge

Now a more creative task: teaching the model to adopt the **alien speech** persona. Simple accuracy doesn't work here, so you'll fine-tune for style and explore more advanced, qualitative evaluation techniques.

- **Stylistic Fine-Tuning**: Train the model on dialogue to make it adopt a unique, consistent persona
- **Good Overfitting**: See how "overfitting" can be a desirable outcome for locking in a specific character
- **LLM-as-a-Judge**: Use another LLM to evaluate your model's stylistic consistency

### Workshop 5: Building Agents and Eval Harnesses with Local LLMs
**Recording:** https://youtube.com/live/Hhwi-2vWMPA  
**Notebook:** [Colab](https://colab.research.google.com/drive/1AzOiIOV8MN-wAqErPlVs8-WxGD0Zzeuf)

*Build an agent that runs on a phone and learn how to rigorously evaluate agentic behavior.*

This workshop uses a single Colab notebook for all three phases.

#### 1. Why FunctionGemma?

You'll start with why Google DeepMind built a 270M parameter model specialized for function calling:

- Understand the spectrum from **single-step tool calling to multi-hop autonomous agents**
- See where **small local models beat frontier models**: latency, privacy, and on-device deployment
- Define **tool schemas** and their arguments, and format data into the Gemma prompt structure

#### 2. Eval Harness for Agentic Behavior

You'll kick the tires on the base model, then build a proper eval harness:

- **Vibe test** the model with informal prompts to see what works and what doesn't
- Build an eval harness that checks **function selection, argument correctness, and hallucinated functions**
- Explore simple, multiple, and parallel function calling evals via the **Berkeley Function Calling Leaderboard**

#### 3. Fine-Tuning and Mobile Deployment

You'll fine-tune FunctionGemma 270M on a mobile actions dataset:

- Fine-tune using **SFT** on actions like flashlight, calendar events, maps, and email
- Read **training and validation loss curves** to check the model is learning
- **Deploy to mobile devices** using Google AI Edge
