# Agentic AI Writer

### AI-Powered Stateful Blog Generation Pipeline

**Agentic AI Writer** is a professional, automated content generation tool built using **LangGraph**, **LangChain**, and **Google Generative AI (Gemini)**. This project moves beyond simple prompting by implementing a stateful graph architecture. It orchestrates a structured workflow that refines user topics, utilizes reasoning to draft high-quality content, and automatically translates the result into **French** or **Kurdish**.

Designed for production environments, the application is fully containerized with **Docker**, rigorously tested with **Postman**, and offers deep observability through **LangSmith**.

## 🚀 Key Features

*   **Stateful Graph Workflow:** Leverages **LangGraph** to manage the cyclical flow of logic and state between processing nodes (Refinement → Writing → Translation).
*   **Google Gemini Integration:** Powered by Google's advanced Generative AI models for superior reasoning and creative writing capabilities.
*   **Smart Title Refinement:** The system acts as an editor, analyzing raw topics to generate SEO-optimized and engaging titles before drafting begins.
*   **Automated Localization:** Seamlessly translates the finalized blog post into specific target languages (**French** and **Kurdish**) while preserving context.
*   **Production-Ready:** Containerized using **Docker** for consistent hosting and deployment.
*   **Full Observability:** Integrated with **LangSmith** for real-time tracing, debugging, and latency monitoring.

## 🛠️ Tech Stack

*   **Orchestration:** [LangGraph](https://langchain-ai.github.io/langgraph/)
*   **Framework:** [LangChain](https://www.langchain.com/)
*   **Model Provider:** Google Generative AI (Gemini)
*   **Observability:** [LangSmith](https://www.langchain.com/langsmith)
*   **Deployment:** Docker
*   **Testing:** Postman

## ⚙️ Workflow Architecture

The application executes a directed sequence of logic nodes:

1.  **Input:** The user provides a blog topic and selects a target language (French or Kurdish).
2.  **Refinement Node:** The model evaluates the input and generates a polished, professional title.
3.  **Writing Node:** Using the refined title, the model employs reasoning to outline and draft the full blog article.
4.  **Translation Node:** The final draft is translated into the selected target language as the output.

## 📦 Configuration

To run the project, you need to set up the following environment variables. Create a `.env` file in the root directory:

```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT="BlogAgentic"
LANGCHAIN_API_KEY="your_langchain_api_key"
LANGSMITH_API_KEY="your_langsmith_api_key"
GOOGLE_API_KEY="your_google_api_key"
