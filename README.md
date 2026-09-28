# LangChain Chains

A simple hands-on project to understand and implement different types of **chains in LangChain** using Python.

This repository contains small, focused examples of LangChain chains, starting from a basic chain and progressing to sequential, parallel, and conditional workflows.

## 📌 What is a Chain?

In LangChain, a **chain** is a sequence of steps that connects components such as prompts, language models, parsers, and other functions to complete a task.

For example:

```text
User Input
    ↓
Prompt
    ↓
LLM
    ↓
Output
```

Chains become more useful when multiple operations need to be connected together.

---

## 📂 Project Structure

```text
Langchain_Chains/
│
├── simple_chain.py
├── sequential_chain.py
├── parallel_chain.py
├── conditional_chain.py
│
├── .vscode/
│
└── README.md
```

### Files

| File                   | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `simple_chain.py`      | Basic LangChain chain implementation             |
| `sequential_chain.py`  | Executes multiple steps one after another        |
| `parallel_chain.py`    | Executes multiple independent chains in parallel |
| `conditional_chain.py` | Executes different chains based on a condition   |

---

# 🔗 Types of Chains

## 1. Simple Chain

A simple chain connects a prompt with an LLM and produces an output.

```text
Input
  ↓
Prompt
  ↓
LLM
  ↓
Output
```

**Use case:** Basic LLM applications and understanding LangChain fundamentals.

File:

```text
simple_chain.py
```

---

## 2. Sequential Chain

A sequential chain executes multiple operations in a specific order.

```text
Input
  ↓
Step 1
  ↓
Step 2
  ↓
Step 3
  ↓
Final Output
```

The output from one step can become the input for the next step.

**Example:**

```text
Topic
  ↓
Generate Explanation
  ↓
Generate Summary
  ↓
Final Response
```

File:

```text
sequential_chain.py
```

---

## 3. Parallel Chain

A parallel chain runs independent operations at the same time.

```text
              ┌──→ Chain A ──→ Result A
Input ────────┤
              └──→ Chain B ──→ Result B
```

This is useful when multiple pieces of information can be generated independently.

**Example:**

Given a topic:

```text
              ┌──→ Generate Summary
Topic ────────┤
              └──→ Generate Key Points
```

File:

```text
parallel_chain.py
```

---

## 4. Conditional Chain

A conditional chain selects a particular path depending on the input or result of a previous step.

```text
                 ┌──→ Chain A
Input → Condition
                 └──→ Chain B
```

For example:

```text
User Question
      ↓
Check Question Type
      ↓
 ┌───────────────┐
 │               │
Technical      General
 │               │
 ↓               ↓
Technical      General
Chain          Chain
```

**Use case:** Applications where different inputs require different processing logic.

File:

```text
conditional_chain.py
```

---

# 🛠️ Technologies Used

* Python
* LangChain
* Large Language Models (LLMs)
* Prompt Templates
* Runnable Chains

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/laxmankhedkar/Langchain_Chains.git
```

### 2. Move into the project directory

```bash
cd Langchain_Chains
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install langchain
```

Depending on the LLM used in the examples, you may also need the corresponding LangChain integration package.

---

# 🔑 API Key

If the examples use a cloud-based LLM, configure the required API key as an environment variable.

For example:

```bash
OPENAI_API_KEY=your_api_key
```

Avoid putting API keys directly inside Python files.

> **Never commit your API keys to GitHub.**

---

# ▶️ Running the Examples

Run any example using Python:

```bash
python simple_chain.py
```

```bash
python sequential_chain.py
```

```bash
python parallel_chain.py
```

```bash
python conditional_chain.py
```

Each file demonstrates a different way of connecting components in LangChain.

---

# 🎯 Learning Objectives

This repository is mainly created for learning and interview preparation.

By going through these examples, you can understand:

* What LangChain chains are
* How chains connect different components
* Simple chains
* Sequential workflows
* Parallel execution
* Conditional routing
* Prompt and LLM integration
* Runnable-based workflows
* Building more structured LLM applications

---

# 🧠 Real-World Applications

Chain-based workflows can be used in applications such as:

### Document Processing

```text
Document
   ↓
Extract Text
   ↓
Summarize
   ↓
Generate Key Points
```

### Customer Support

```text
User Query
    ↓
Classify Query
    ↓
Route to Appropriate Chain
    ↓
Generate Response
```

### Content Generation

```text
Topic
  ↓
Generate Content
  ↓
Review Content
  ↓
Improve Content
  ↓
Final Content
```

### RAG Applications

Chains can also be used as part of Retrieval-Augmented Generation systems:

```text
User Query
    ↓
Retriever
    ↓
Relevant Documents
    ↓
Prompt
    ↓
LLM
    ↓
Answer
```

---

# 📚 Recommended Learning Order

If you are new to LangChain, follow the files in this order:

```text
1. simple_chain.py
       ↓
2. sequential_chain.py
       ↓
3. parallel_chain.py
       ↓
4. conditional_chain.py
```

This progression helps build an understanding from basic chains to more flexible workflows.

---

# 🚀 Future Improvements

Possible additions to this repository:

* RAG chain
* Retrieval chain
* Tool calling
* Structured output
* Agent workflows
* LangGraph workflows
* Streaming responses
* Memory/conversation history
* Evaluation of chain outputs

---

# 👨‍💻 Author

**Laxman Khedkar**

Data Scientist & ML Engineer
Python | SQL | Machine Learning | NLP | LLMs | RAG | Generative AI

GitHub: [@laxmankhedkar](https://github.com/laxmankhedkar)

---

## ⭐ If this repository helps you

Feel free to explore the examples, experiment with the code, and build your own LangChain workflows.

If you find it useful, consider giving the repository a ⭐.
