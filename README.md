# CSCI 436 – Assignment 3: Docker & Containerization

This repository contains a Flask + MongoDB containerized application that demonstrates:
- Docker fundamentals and commands
- Running and debugging containers
- Building a custom image with Dockerfile
- Multi-container setup with Docker Compose
- Data persistence with Docker volumes
- (Optional bonus) Push image to Docker Hub

---

## 1) Project Structure

```text
docker-assignment/
├─ app/
│  ├─ app.py
│  └─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ screenshots/
│  ├─ task1-hello-world.png
│  ├─ task1-ps-images.png
│  ├─ task2-nginx-browser.png
│  ├─ task2-logs-exec.png
│  ├─ task3-build-run.png
│  ├─ task4-compose-up.png
│  └─ task5-volume-persistence.png
└─ README.md
```

---

## 2) Prerequisites

- Docker Desktop installed and running
- Git installed
- (Optional) Docker Hub account

Check Docker:
```bash
docker --version
docker compose version
```

---

## 3) Task 1 – Docker Installation & Basic Commands

Run:
```bash
docker run hello-world
docker ps -a
docker images
```

Take screenshots of command outputs.

---

## 4) Task 2 – Run and Debug a Container (Nginx Example)

Run nginx:
```bash
docker run -d --name mynginx -p 8080:80 nginx
```

Open in browser:
- http://localhost:8080

Debug commands:
```bash
docker logs mynginx
docker exec -it mynginx sh
```

Take screenshots:
- Browser page on localhost:8080
- logs and exec output

Cleanup (optional):
```bash
docker stop mynginx
docker rm mynginx
```

---

## 5) Task 3 – Build Your Own Docker Image (Flask)

Build image:
```bash
docker build -t assignment3-flask:v1 .
```

Run container:
```bash
docker run -d --name flask-app -p 5000:5000 assignment3-flask:v1
```

Test:
- http://localhost:5000
- http://localhost:5000/health

Take screenshot of:
- build output
- running Flask app in browser

Cleanup (optional):
```bash
docker stop flask-app
docker rm flask-app
```

---

## 6) Task 4 – Multi-Container App with Docker Compose (Flask + MongoDB)

Start services:
```bash
docker compose up -d --build
```

Check running services:
```bash
docker compose ps
```

Test endpoints:
```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/visit -H "Content-Type: application/json" -d "{\"user\":\"Sabir\"}"
curl http://localhost:5000/visits
```

Take screenshot of:
- `docker compose ps`
- API output in terminal and/or browser

Stop services:
```bash
docker compose down
```

---

## 7) Task 5 – Docker Volumes (Persistence)

Start compose:
```bash
docker compose up -d --build
```

Insert data:
```bash
curl -X POST http://localhost:5000/visit -H "Content-Type: application/json" -d "{\"user\":\"PersistenceTest\"}"
curl http://localhost:5000/visits
```

Restart containers:
```bash
docker compose restart
```

Check data still exists:
```bash
curl http://localhost:5000/visits
```

If the inserted record is still present after restart, persistence is verified.

Take screenshots:
- before restart
- after restart (same data exists)

---

## 8) Optional Bonus – Push Image to Docker Hub

```bash
docker login
docker tag assignment3-flask:v1 <your_dockerhub_username>/assignment3-flask:v1
docker push <your_dockerhub_username>/assignment3-flask:v1
```

---

## 9) Submission Checklist

- [ ] 5–10 minute demo video
- [ ] GitHub repository link
- [ ] Source code included
- [ ] Dockerfile included
- [ ] docker-compose.yml included
- [ ] README.md included
- [ ] All screenshots included

---

## 10) Useful Cleanup Commands

```bash
docker compose down -v
docker container prune -f
docker image prune -f
```