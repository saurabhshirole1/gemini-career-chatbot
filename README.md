# 🚀 Gemini Career Advisor Chatbot

**Production-Ready GenAI Career Mentorship System (Deployed on AWS EC2)**

## 🌐 Live Demo

Access the deployed application here:

🔗 http://35.154.201.249:8501/

---

## 📌 Project Overview

Gemini Career Advisor Chatbot is a production-grade, domain-specific GenAI application built using Google Gemini API. The system provides structured, professional career guidance including:

- Skill gap analysis
- Learning roadmaps
- Interview preparation strategy
- Technology recommendations
- Career transition guidance

The application follows clean architecture principles and is deployed on AWS EC2 for real-world accessibility.

---

## 🏗️ System Architecture

```
User
   ↓
Streamlit UI Layer
   ↓
Backend Service Layer
   ↓
Prompt Engineering Module
   ↓
Google Gemini API
   ↓
Response Processing
   ↓
UI Rendering
```

---

## ✨ Key Features

### 🔹 Domain-Specific Career Guidance
- Structured professional responses
- Roadmap generation
- Interview-focused mentoring

### 🔹 Advanced Prompt Engineering
- Dedicated system role
- Domain constraints
- Structured response formatting
- Reduced hallucination behavior

### 🔹 Multi-Turn Context Memory
- Session-based chat history
- Sliding-window memory optimization
- Token usage control

### 🔹 Production-Grade Architecture
- Modular folder structure
- Separation of concerns
- Dedicated services for:
  - API handling
  - Memory management
  - Prompt configuration

### 🔹 Secure Configuration
- Environment variable-based API management
- No hardcoded credentials
- `.env` protection

### 🔹 Logging System
- User query logging
- API response time tracking
- Error monitoring

### 🔹 Cloud Deployment
- Hosted on AWS EC2
- Public IP accessibility
- Background process handling via `nohup`
- Secure Security Group configuration

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.12 |
| AI Model | Google Gemini API (`google-genai` SDK) |
| UI Framework | Streamlit |
| Cloud | AWS EC2 (Ubuntu 22.04) |
| Monitoring | Python Logging Module |
| Configuration | Environment-based (`.env`) |

---

## 📂 Project Structure

```
gemini-career-chatbot/
│
├── app.py
├── config.py
├── requirements.txt
│
├── services/
│   ├── gemini_service.py
│   ├── memory_service.py
│   └── app_logger.py
│
├── prompts/
│   └── system_prompt.py
│
├── utils/
│
└── logs/
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Local Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ AWS EC2 Deployment

### 1. Launch EC2 Instance
- **OS:** Ubuntu 22.04
- **Type:** t2.micro
- **Security Group Rules:**

| Type | Protocol | Port | Source |
|------|----------|------|--------|
| SSH | TCP | 22 | My IP |
| Custom TCP | TCP | 8501 | 0.0.0.0/0 |

### 2. Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip python3-venv git -y
```

### 3. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/gemini-career-chatbot.git
cd gemini-career-chatbot
```

### 4. Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Add Environment Variables

```bash
nano .env
```

Add the following:

```env
GEMINI_API_KEY=your_api_key
```

### 6. Run Permanently

```bash
nohup venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0 > streamlit.log 2>&1 &
```

Access the app via:

```
http://YOUR_PUBLIC_IP:8501
```

---

## 📊 Production Considerations

- Sliding window memory to reduce token explosion
- Modular codebase for scalability
- Background execution using `nohup`
- Logging system for monitoring
- Clean separation of UI and backend

---

## 🚀 Future Enhancements

- [ ] Nginx reverse proxy (port 80)
- [ ] HTTPS with SSL
- [ ] Custom domain integration
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Database-backed persistent chat storage
- [ ] Role-based authentication

---

## 📈 Resume Value

This project demonstrates:

- End-to-end GenAI system design
- Prompt engineering expertise
- Secure API management
- Cloud deployment skills
- Production-level backend structuring
- Multi-turn conversational memory implementation
