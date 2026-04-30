# 🚀 Multi-Tier AI Banking Application (Dockerized)

This project demonstrates a complete **multi-tier DevOps architecture** using Docker. It includes a frontend UI, backend API, PostgreSQL database, and basic AI (LLM-ready) integration.

---

## 📌 Overview

The application follows a 3-tier architecture:

```txt
Frontend (UI) → Backend (Flask API) → Database (PostgreSQL)
                                ↓
                          AI Chat Endpoint
```

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript (served via Nginx)
* **Backend:** Python (Flask API)
* **Database:** PostgreSQL
* **Containerization:** Docker
* **Orchestration:** Docker Compose
* **Security:** GPG Signed Commits
* **Future:** AI/LLM Integration (OpenAI/Ollama)

---

## 📁 Project Structure

```txt
multi-tier-ai-bankapp/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── Dockerfile
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── database/
│   └── init.sql
│
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

## ⚙️ How It Works

* **Frontend** calls backend APIs (`/accounts`, `/ai-chat`)
* **Backend** connects to PostgreSQL database
* **Database** stores account & transaction data
* **AI endpoint** returns mock response (LLM-ready)

---

## ▶️ Run the Project

### 1. Build & Start

```bash
docker compose up -d --build
```

---

### 2. Verify Containers

```bash
docker ps
```

---

### 3. Access Application

Frontend:

```txt
http://localhost:8080
```

Backend APIs:

```txt
http://localhost:5000/health
http://localhost:5000/accounts
```

---

## 🔑 Key Concepts Used

* Multi-tier architecture (Frontend + Backend + DB)
* Dockerfile and containerization
* Docker Compose for orchestration
* Docker networks for inter-container communication
* Docker volumes for persistent database storage
* Health checks for service reliability
* Environment variables for configuration
* CORS handling for frontend-backend communication

---

## 🔐 Security Practices

* GPG signed commits for code authenticity
* No hardcoded credentials
* `.dockerignore` used to exclude unnecessary files

---

## 🔥 Interview Questions & Answers

### 1. What is a multi-tier architecture?

A system divided into layers like frontend, backend, and database.

---

### 2. Why use Docker Compose?

To run and manage multiple containers using a single configuration file.

---

### 3. How do containers communicate?

Using Docker networks with service names (e.g., backend connects to `db`).

---

### 4. What is a Docker volume?

Used to persist data even if containers are deleted.

---

### 5. Why is CORS required?

To allow frontend (port 8080) to access backend (port 5000).

---

### 6. What are health checks?

They verify whether a service is running properly.

---

### 7. Why use port mapping?

To expose container services to the host machine.

---

### 8. How does backend connect to DB?

Using environment variables and service name (`db`) as hostname.

---

## 🚀 Future Enhancements

* Real AI/LLM integration (OpenAI / Ollama)
* Nginx reverse proxy with HTTPS
* Deployment on AWS EC2
* CI/CD pipeline (GitHub Actions)
* Kubernetes deployment

---

## 📌 Conclusion

This project demonstrates a **real-world DevOps workflow** involving application development, containerization, orchestration, and system design.

---
