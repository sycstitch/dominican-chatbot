<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"/>
  <img src="https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face Transformers"/>
</p>

# **Case Study Outline & Project Log**

**Last Updated:** July 5, 2025
<br /><br />

## **1. Project Description**

The goal is to build a conversational AI that embodies a character named "Chamo," an interactive tutor for Dominican Spanish. This project is more than a simple Q&A bot; it's a fully conversational agent designed to engage users with a friendly, witty, and encouraging personality. The ability to accurately answer questions about the language is a core feature within this broader conversational framework.

The AI will be able to:

* Engage in natural, character-consistent small talk and general conversation.
* Define unique Dominican words and phrases from a custom-built knowledge base when asked.
* Explain grammatical habits and linguistic nuances (e.g., shortening words, common slang usage).
* Intelligently understand user questions about the language, even when they don't know the exact term they're looking for.

The final project will serve as a portfolio piece demonstrating practical skills in Natural Language Processing, RAG system design, and prompt engineering.
<br /><br />

### **Motivation**

This project was born from a deep interest in Caribbean Spanish, sparked by friendships and relationships with people from the region. Dominican Spanish, in particular, is a rich and vibrant dialect that is often misunderstood or overlooked in favor of more "standard" forms of Spanish. There's a fascinating parallel between its linguistic patterns—such as cadence and word-final shortening—and African American Vernacular English (AAVE). As someone deeply interested in AAVE, Dominican Spanish, and other Creole and Pidgin expressions, this project is an opportunity to celebrate and explore these often-sidelined but vital parts of language.
<br /><br />

## **2. Decision Process & Learning Journey**

This section outlines the key questions, points of confusion, and learning milestones that shaped the project's direction.

* **Initial Confusion: From Data to Application**
  * **Problem:** Started with a valuable dataset but was unsure how to turn it into an interactive project.
  * **Learning:** The concept of a "chatbot" was identified as the ideal application, shifting the focus from static data to a conversational experience.
* **Pivotal Moment 1: Choosing the Right NLP Task**
  * **Problem:** Faced with numerous NLP task options, it was unclear which were relevant.
  * **Learning:** Clarified that `Text Generation` is the core engine, while `Question Answering` is the *framework*.
* **Pivotal Moment 2: The RAG Breakthrough**
  * **Problem:** How can the chatbot understand questions about concepts (e.g., "...what's the word for 'party'?")?
  * **Learning:** The solution is **Retrieval-Augmented Generation (RAG)**, a two-model system using a "Retriever" (`Sentence Similarity`) and a "Generator" (`Text Generation`).
* **Pivotal Moment 3: The "Two-Model" Workflow**
  * **Problem:** Realized that GUI tools or a basic Ollama setup are designed for one model at a time.
  * **Learning:** The professional workflow is to use a **Python script** as the orchestrator to manage both models.
* **Pivotal Moment 4: Clarifying the Architecture**
  * **Problem:** Why wouldn't Ollama just run both models? Why separate them?
  * **Learning:** The optimal architecture is to treat the two models differently based on their size and function. The large Generator model (`Mistral-7B`) runs as a dedicated service via Ollama (like a "power plant"), while the small Retriever model (`all-MiniLM`) is loaded directly into the Python script (like a "handheld tool"). This is more efficient and gives the script faster, more direct control over the retrieval process.
* **Pivotal Moment 5: Data Provenance & Ethics**
  * **Problem:** Realized that the primary dictionary source was proprietary, making it unethical and illegal to reproduce in a public project.
  * **Learning:** The project's public-facing version will use a small, representative sample of 10-15 terms in a `dominican-terms-example.json` file. This allows the technology to be showcased without infringing on copyright.
* **Strategic Decision: Model Selection Philosophy**
  * **Problem:** Should I be very picky about models from the start?
  * **Learning:** Start with reliable, industry-standard models to build the system's foundation. Defer "pickiness" to the final testing phase with OpenRouter.
<br /><br />

## **3. Tools, Models & Hardware**

* **Hardware:** MacBook M1 Pro (16GB RAM)
  * *Why:* My trusty personal computer, which is now working much harder than it ever signed up for. It's a powerful and efficient machine capable of running 7-billion-parameter language models locally.
* **Primary Language:** Python
  * *Why:* The undisputed standard for NLP, necessary for orchestrating the RAG system.
* **Containerization:** [Docker](https://www.docker.com/)
  * *Why:* To ensure a consistent, reproducible development environment for myself and any future collaborators. Docker simplifies dependency management and makes the entire application portable and easier to deploy.
* **Data Sources:**
  * *Why:* A multi-faceted approach to capture authentic language. Sources include social media platforms for emerging terms, existing dictionaries for foundational vocabulary, and direct consultation with two native Dominican speakers currently living in the DR. This provides a contemporary snapshot of the language, but also introduces known variables (see Limitations section below).
* **Generator/QA Model:** [`mistral-7b-instruct:Q4_K_M`](https://ollama.com/koesn/mistral-7b-instruct:Q4_K_M)
  * *Why:* A top-tier 7B instruction-following model licensed under **Apache 2.0**, a permissive license ideal for portfolio work. The base model is on Hugging Face [here](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3).
* **Retriever Model:** [`all-MiniLM-L6-v2`](https://ollama.com/tazarov/all-minilm-l6-v2-f32)
  * *Why:* The industry-standard for sentence similarity. It's lightweight, fast, and also licensed under **Apache 2.0**. The base model is on Hugging Face [here](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).
* **Local Model Server:** [Ollama](https://ollama.com/)
  * *Why:* A streamlined tool for serving local LLMs via an API, acting as the "engine" for the Python script. It will be run as a service within a Docker container.
* **Final Testing Platform:** [OpenRouter](https://openrouter.ai/)
  * *Why:* A service providing a single API to access state-of-the-art models for final testing and optimization.
<br /><br />

### **A Note on Licensing**

The choice to use models licensed under **Apache 2.0** was deliberate. This permissive license allows for broad use (including modification and distribution) while requiring attribution, providing a safe and professional foundation for an open-source portfolio project.
<br /><br />

## **4. Limitations & Considerations**

This project aims for authenticity, but it's important to acknowledge its limitations.

* **Regional & Social Variation:** Dominican Spanish is not monolithic. The primary human sources reflect this: one is a male from the countryside (*campo*), while the other is a female from the capital, Santo Domingo, who is more connected to urban music culture (reggaeton, dembow). This means the knowledge base may have gaps in slang that is hyper-regional (e.g., specific to the Cibao region) or not prevalent in certain social circles.
* **Usage Frequency & Context:** While one dictionary source provides a helpful "usage meter" for many terms, this data is not available for all entries. Therefore, the chatbot's perception of a word's commonality may not always be precise. Furthermore, actual usage will always vary significantly based on an individual's specific social circle and location.
* **Diaspora vs. Homeland:** The data is primarily sourced from speakers currently in the DR. The Spanish spoken by the large Dominican diaspora (most notably in New York and Florida) has its own unique evolution and influences, which may not be fully captured here.
* **Data Sample Size:** The public version of this project on GitHub uses a small, representative sample of terms (`dominican-terms-example.json`) to respect the copyright of proprietary dictionary sources. The full knowledge base used for private development is more extensive.
* **Snapshot in Time:** Language, especially slang, evolves rapidly. This project's knowledge base represents a snapshot from 2025 and will require ongoing updates to stay current.
<br /><br />

## **5. Step-by-Step Project Plan**

* **Phase 1: Setup & Environment (Done)**
  * \[x] **Action:** Confirmed hardware suitability and development tool choices.
  * \[ ] **Action:** Created a `Dockerfile` for the Python application and a `docker-compose.yml` to define the application services (Ollama + Python chatbot).
  * \[ ] **Action:** Used the Docker setup to run Ollama and download the selected Generator and Retriever models.
  * \[ ] **Action:** Converted the initial dictionary entries into a structured `JSON` format.
  * \[ ] **Action:** Protected the proprietary data by creating a separate, smaller `dominican-terms-example.json` for public repository use.
* **Phase 2: Core RAG Prototyping (Current Step)**
  * \[ \] **Action:** Launch the entire environment with a single command: `docker-compose up`.
  * \[ \] **Action:** Create the main Python script for the chatbot service.
  * \[ \] **Action:** In the script, load the `dominican-terms-example.json` data.
  * \[ \] **Action:** In the script, load the `all-MiniLM-L6-v2` model and write the "retrieval" function.
  * \[ \] **Action:** In the script, write the "generation" function that constructs a detailed prompt and sends it to the Ollama service.
  * \[ \] **Goal:** Create a working command-line version of the chatbot where the entire RAG pipeline is functional using the sample data.
* **Phase 3: Polishing & Optimization**
  * \[ \] **Action:** Adapt the Python script to point its API requests to OpenRouter.
  * \[ \] **Action:** Systematically test various high-end models (e.g., GPT-4o, Claude 3.5 Sonnet).
  * \[ \] **Action:** Evaluate responses based on creativity, adherence to the persona, and accuracy.
  * \[ \] **Goal:** Select the definitive "best" Generator model for the final version of the project and document why it was chosen.
