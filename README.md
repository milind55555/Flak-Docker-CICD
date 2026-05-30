# 🚀 Flask CI/CD Pipeline with GitHub Actions & Docker

## Overview

This project demonstrates a complete DevOps CI/CD pipeline for a Flask application using:

* Python Flask
* Docker
* DockerHub
* GitHub Actions
* Automated Build & Deployment
* Container Validation Testing

The pipeline automatically builds, tests, containerizes, and publishes Docker images whenever code is pushed to the main branch.

---

## Architecture

Developer Push → GitHub Actions → Docker Build → DockerHub Push → Container Validation → Deployment Ready

---

## Features

✅ Flask Web Application

✅ Docker Containerization

✅ GitHub Actions CI/CD

✅ Automated DockerHub Deployment

✅ Container Health Verification

✅ Security Scanning (Trivy)

✅ Production Ready Dockerfile

---

## Tech Stack

| Technology     | Purpose               |
| -------------- | --------------------- |
| Flask          | Backend Framework     |
| Docker         | Containerization      |
| GitHub Actions | CI/CD                 |
| DockerHub      | Image Registry        |
| Trivy          | Security Scanning     |
| Gunicorn       | Production Web Server |

---

## Project Structure

flask-cicd-docker/

├── app.py

├── requirements.txt

├── Dockerfile

├── .dockerignore

├── .github/workflows/ci-cd.yml

└── README.md

---

## CI/CD Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions pipeline starts.
3. Docker image is built.
4. Image security scan is performed.
5. Docker image is pushed to DockerHub.
6. Container validation test is executed.
7. Deployment artifact becomes available.

---

## Docker Commands

Build Image

docker build -t flask-cicd .

Run Container

docker run -d -p 5000:5000 flask-cicd

View Logs

docker logs <container-id>

Stop Container

docker stop <container-id>

---

## Learning Outcomes

* CI/CD Pipeline Design
* Docker Image Management
* GitHub Actions Automation
* DockerHub Integration
* Container Security Best Practices
* DevOps Workflow Automation

---

## Author

Milind Hanchate

Aspiring DevOps Engineer | Cloud Enthusiast | Docker & Kubernetes Learner

Actively building real-world DevOps projects focused on automation, CI/CD, cloud deployment, and container orchestration.
