# 🤖 **ReplyMate AI Agent**
![ReplyMate Cover](replymate_cover.png)

**Built by Aptiva AI for the lablab.ai Hackathon 2025**

**ReplyMate AI Agent** is a real-time conversational intelligence system that enables secure, automated communication with built-in fraud detection and contextual memory. It’s designed for businesses that value smart, responsive, and ethical AI-powered messaging.

---

## 🚀 **Features**
- **AI-powered Responses** using GPT-4o  
- **Fraud Detection** with hybrid rule-based + LLM techniques  
- **Smart Context Memory** via LangChain and Redis  
- **Multi-Platform Messaging** (WhatsApp Business API, Webchat, Email)  
- **Real-Time Backend** with FastAPI / Node.js  
- **Frontend Dashboard** built using React.js  
- **Scalable Databases** using MongoDB and PostgreSQL  
- **Revisit Consent Button** to let users update data-sharing preferences anytime  

---

## 🧠 **Tech Stack**

| Frontend   | Backend           | AI/NLP             | Infra & Database           |
|------------|-------------------|--------------------|-----------------------------|
| React.js   | FastAPI / Node.js | GPT-4o, LangChain  | Redis, MongoDB, PostgreSQL |

---

## 👥 **Team Aptiva AI**

| Name                   | Role                      | GitHub                                       |
|------------------------|---------------------------|----------------------------------------------|
| **Eesha Tariq**        | AI Engineer / Team Lead   | [codewithEshaYoutube](https://github.com/codewithEshaYoutube) |
| **Zeeshan Tariq**      | Data Scientist            | [zeeshantariqpkn](https://github.com/zeeshantariqpkn) |
| **Ramspheld Onyango**  | Python Developer          | [RamspheldOnyangoOchieng](https://github.com/RamspheldOnyangoOchieng) |
| **Najma Razzaq**       | Data Scientist            | [najma](https://github.com/najma) |
| **Deepak Kumar**       | Software Design Engineer  | [Deepakkumar0707](https://github.com/Deepakkumar0707) |
| **Muhammad Ehtisham**  | Software Engineer         | [mehtisham](https://github.com/mehtisham) |

---

## 📽️ **Demo & Presentation**

### **Demo Video:**
![ReplyMate AI Demo](demo-replymate-2.mp4)

*The video will autoplay once clicked.*

- 🖼️ **Slide Deck:** [Download PDF - replymate_slides.pdf](link_to_download_pdf)
- 🧾 **Cover Page:** _Coming Soon_

---

## 🧪 **How to Run**

```bash
# Clone the repository
git clone https://github.com/YourRepo/ReplyMate-AI-Agent.git
cd ReplyMate-AI-Agent

# Backend setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend setup
cd ../frontend
npm install
npm start
