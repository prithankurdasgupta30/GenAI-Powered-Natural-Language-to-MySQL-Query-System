# 🚀 GenAI-Powered Natural Language to MySQL Query System

A full-stack AI application that converts natural language into executable MySQL queries using a locally hosted Large Language Model (LLM) powered by **Ollama**. 

This project allows users to interact with a MySQL database using simple English instead of writing SQL manually. The entire system runs locally inside an Ubuntu Virtual Machine, making it fully offline and independent of any external API.

---

## 📌 Project Overview

This system integrates:
* **🐧 Ubuntu Linux:** Running inside VirtualBox VM for isolation.
* **🗄️ MySQL Database:** Local relational data storage.
* **🤖 Mistral LLM:** Locally hosted via Ollama for private AI processing.
* **🐍 Flask Backend:** Python-based API orchestration.
* **🌐 Modern Frontend:** HTML/CSS/JavaScript interface.

The application translates natural language into syntactically correct MySQL queries using Generative AI and executes them directly on the database.

---

## 🏗️ System Architecture

The flow of data through the system is as follows:


**User (Browser)** ↓  
**Frontend (HTML / JavaScript)** ↓  
**Flask Backend (Python)** ↓  
**Ollama Server (Mistral LLM)** ↓  
**MySQL Database (company_db)**

---

## 🖥️ Development Environment

This project was developed using:
* **Ubuntu Linux:** Inside VirtualBox Virtual Machine.
* **Python 3:** Core logic and backend.
* **MySQL Server:** Local installation.
* **Ollama:** For running LLMs locally.
* **Virtual Environment (venv):** For dependency management.

### Why Ubuntu + VirtualBox?
* **Isolated environment:** Prevents conflicts with the host OS.
* **Memory Management:** Controlled allocation for resource-heavy LLMs.
* **Linux Simulation:** Provides real-world deployment experience.

---

## 📦 Technologies Used

* **Backend:** Python, Flask
* **Database:** MySQL, `mysql-connector-python`
* **AI Engine:** Ollama (Mistral / Phi-3)
* **Frontend:** HTML5, CSS3, JavaScript
* **Infrastructure:** Ubuntu, VirtualBox

---

## 📂 Project Structure

```text
project/
│
├── app.py              # Flask backend (Logic & AI Prompting)
├── index.html          # Frontend UI (User Interface)
├── venv/               # Python virtual environment
└── database/           # SQL scripts for company_db
