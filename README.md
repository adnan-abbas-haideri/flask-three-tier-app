# Flask Three-Tier App 🚀

A simple **three-tier web application** built with **Flask and MySQL**, and containerized using **Docker and Docker Compose**.

This project demonstrates how a frontend, backend application, and database can work together using separate containers.

## 🏗️ Architecture

```text
                User
                  │
                  ▼
          ┌───────────────┐
          │    Flask      │
          │   Backend     │
          │   Port 5000   │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │     MySQL     │
          │   Database    │
          │   Port 3306   │
          └───────┬───────┘
                  │
                  ▼
             Docker Volume
```

## ✨ Features

* Flask web application
* MySQL database
* Contact form with database storage
* Multiple pages
* Responsive modern UI
* Custom Docker network
* Persistent MySQL volume
* Docker Compose setup
* Environment-based database configuration
* Health check endpoint

## 🛠️ Technologies

* **Python**
* **Flask**
* **MySQL**
* **Docker**
* **Docker Compose**
* **HTML / CSS / JavaScript**

## 📁 Project Structure

```text
flask-three-tier-app/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── database/
│   └── init.sql
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── templates/
    ├── index.html
    ├── about.html
    ├── services.html
    └── contact.html
```

## 🚀 Run the Project

### 1. Clone the repository

```bash
https://github.com/adnan-abbas-haideri/flask-three-tier-app.git
```

```bash
cd flask-three-tier-app
```

### 2. Start the application

```bash
docker compose up -d --build
```

### 3. Check running containers

```bash
docker compose ps
```

You should see:

```text
flask_app
mysql
```

### 4. Open the application

Open:

```text
http://localhost:5000
```

## 🗄️ Database

The application uses MySQL with the following database:

```text
Database: devops_app
Table: messages
```

Messages submitted through the contact form are stored in the `messages` table.

To access MySQL:

```bash
docker exec -it mysql mysql -uroot -proot
```

Then:

```sql
USE devops_app;

SELECT * FROM messages;
```

## 💾 Persistent Storage

MySQL data is stored using a Docker named volume:

```text
mysql-data
```

This allows database data to remain available even when the MySQL container is removed and recreated.

Check the volume:

```bash
docker volume ls
```

## 🌐 Docker Network

Both containers communicate through a custom Docker network:

```text
flask
```

The Flask application connects to MySQL using the Docker Compose service name:

```text
DB_HOST=mysql
```

The application does **not** use `localhost` to connect to MySQL because Flask and MySQL run in separate containers.

## ❤️ Health Check

The application provides a simple health endpoint:

```text
GET /health
```

Open:

```text
http://localhost:5000/health
```

Example response:

```json
{
  "application": "Flask DevOps App",
  "status": "healthy"
}
```

## 🧹 Stop the Application

```bash
docker compose down
```

To remove the containers and the database volume:

```bash
docker compose down -v
```

> **Warning:** `docker compose down -v` removes the MySQL volume and therefore deletes the stored database data.

## 🎯 Project Purpose

This project was created to practice:

* Docker containerization
* Docker networking
* Docker volumes
* Docker Compose
* Flask application deployment
* MySQL database connectivity
* Multi-container application architecture

## 📌 Future Improvements

* Add Jenkins CI/CD pipeline
* Push Docker images to Docker Hub
* Deploy to AWS EC2
* Add Kubernetes manifests
* Add Prometheus and Grafana monitoring
* Add production WSGI server

---

**Built with Flask, MySQL, Docker & Docker Compose.**

