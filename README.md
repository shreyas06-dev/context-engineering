# Context Engineering — A Field Guide for AI-Fluent Leaders

A production-grade prompt engineering library built with FastAPI, SQLAlchemy, and JWT auth. Implements the hierarchical Prompt Pyramid framework to help developers and enterprise leaders move beyond basic prompting.

## 🧠 The Concept
Most prompt libraries are just random lists of tips. Context Engineering treats prompt engineering as a formal discipline. Every entry is structured hierarchically:
1. **Base / Persona:** Defining the AI's role and constraints.
2. **Context / Examples:** Providing the necessary data and few-shot examples.
3. **Task / Instruction:** The immediate, specific request.

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy, Alembic
- **Database:** SQLite (Development), PostgreSQL ready
- **Frontend:** Jinja2 Templates, Vanilla JS, Custom CSS
- **Security:** JWT Authentication, Bcrypt Password Hashing

## ✨ Features
- **Editorial UI:** A dark-mode, highly polished interface designed for readability.
- **Secure Auth:** Full user registration and login flow with JSON Web Tokens.
- **Progressive Disclosure:** An accordion-style library that keeps the UI clean while holding deep technical details.
- **Interactive Elements:** Copy-to-clipboard for examples, rotating specimen cards, and smooth micro-interactions.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shreyas06-dev/context-engineering.git
   cd context-engineering
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Open your browser and navigate to `http://127.0.0.1:8000`.
