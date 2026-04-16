# 🚸 Pedestrian Crossing Detection

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Status](https://img.shields.io/badge/Status-Project_Completed-brightgreen)

## Table of Contents
* [About the Project](#about-the-project)
* [Demo](#demo)
* [System Architecture](#system-architecture)
* [Getting Started](#getting-started)
* [Usage](#usage)

## About the Project
This project was developed for the **RSA (Redes e Sistemas Autónomos)** course. The main objective is to detect pedestrians crossing the street using computer vision algorithms and a simulation environment. 

By identifying pedestrians in real-time or simulated environments, the system aims to improve road safety, potentially triggering alerts or autonomous braking systems in vehicles approaching crosswalks.

## Demo
Check out the simulation and the system in action:
🎥 **[Watch the Simulation Video on YouTube](https://youtu.be/o6qV1tiywO0)**

## System Architecture
The repository is divided into two main components:
* `app2/`: Contains the core application and detection logic (Python/JS and HTML interfaces).
* `simulador/`: The simulation environment setup designed to recreate pedestrian crossing scenarios and test the detection algorithms safely.

## Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
Make sure you have Docker and Docker Compose installed on your system to run the containerized setup.
* Docker
* Docker Compose (v2 recommended)

### Installation
Clone the repository to your local machine:
```bash
git clone [https://github.com/Migueljfc/Pedestrian-Crossing-Detection.git](https://github.com/Migueljfc/Pedestrian-Crossing-Detection.git)
cd Pedestrian-Crossing-Detection
```

### Usage
The project includes a docker-compose.yml file to orchestrate the application and the simulator dependencies effortlessly.
To start the system, run:
```bash
docker compose up -d
```
(Use docker-compose up -d if you are using older versions of Docker).
This will spin up all the necessary services for the pedestrian detection and the simulator interface.
(Note: Depending on how the frontend is exposed, you may access the dashboard via ``http://localhost:<PORT>`` — adjust the port according to your docker-compose config).

To stop the system, run:
```bash
docker compose down
```
