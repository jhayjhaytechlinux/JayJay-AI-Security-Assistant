# 🛡️ JayJay AI Security Assistant

An AI-powered Telegram Cybersecurity Assistant built with Python and powered by **Ollama** using the **Phi-3 Mini** Large Language Model.

The assistant is designed to provide cybersecurity guidance, answer technical questions, and serve as the foundation for an intelligent Security Operations Center (SOC) assistant that runs locally without relying on cloud AI services.

---

## 🚀 Features

- 🤖 AI-powered Telegram chatbot
- 🧠 Local AI using Ollama
- 💬 Powered by Microsoft Phi-3 Mini
- 🔒 Cybersecurity-focused responses
- 💾 Conversation memory support
- ⚙️ Modular Python architecture
- 🐧 Optimized for Ubuntu (WSL) development
- 🔑 Environment variable configuration

---

## 🛠️ Technologies Used

- Python 3
- Telegram Bot API
- Ollama
- Phi-3 Mini
- Git & GitHub
- Ubuntu (WSL)
- Virtual Environment (venv)

---

## 📂 Project Structure

```text
JayJay-AI-Security-Assistant/
│
├── ai_engine.py
├── bot.py
├── config.py
├── logger.py
├── memory.py
├── security.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone git@github.com:jhayjhaytechlinux/JayJay-AI-Security-Assistant.git
```

Enter the project folder

```bash
cd JayJay-AI-Security-Assistant
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate it

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Install Ollama from the official website.

Download the Phi-3 Mini model:

```bash
ollama pull phi3:mini
```

Start the Ollama server:

```bash
ollama serve
```

---

## ▶️ Run the Bot

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the Telegram bot:

```bash
python bot.py
```

---

## 🛣️ Roadmap

### Version 1.0

- ✅ Telegram AI Assistant
- ✅ Ollama Integration
- ✅ Phi-3 Mini Support
- ✅ GitHub Repository

### Version 1.1

- Health check command
- Better logging
- Startup diagnostics
- Improved error handling

### Version 2.0

- Threat intelligence
- CVE explanations
- Nmap scan analysis
- IOC analysis
- MITRE ATT&CK integration
- Security report generation

---

## 👨‍💻 Developer

**Jhay Jhay**

Cybersecurity Analyst | SOC Analyst | AI Automation | Python Developer

GitHub:
https://github.com/jhayjhaytechlinux

---

## 📄 License

This project is released under the MIT License.
