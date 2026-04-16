# 🚸 Pedestrian Crossing Detection

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Status](https://img.shields.io/badge/Status-Project_Completed-brightgreen)

## 📖 About the Project

This project, developed for the **RSA (Redes e Sistemas Autónomos)** course, implements a **V2X-enabled Pedestrian Safety System**. It goes beyond simple computer vision by integrating an autonomous detection unit with a Cooperative Intelligent Transport Systems (C-ITS) communication stack.

The system is designed to detect Vulnerable Road Users (VRUs) at crosswalks and broadcast standardized ITS messages to alert surrounding connected vehicles (V2I/V2V communication), effectively extending the "line-of-sight" of autonomous agents through network cooperation.

### 🏗️ System Architecture & Components

The ecosystem is orchestrated via **Docker**, ensuring a modular microservice architecture:

1.  **V2X Communication Stack (Vanetza):** Running in a dedicated container, [Vanetza](https://github.com/riebl/vanetza) provides the implementation of the **ETSI ITS-G5** protocol suite. It handles the generation, encoding, and transmission of standardized messages (such as **DENM** or **CAM**) when a hazard (pedestrian) is identified.
    
2.  **Detection & Logic Unit (`/app2`):**
    The "brain" of the system. Written in **Python**, it processes data from the simulator. Once a pedestrian is detected within the crosswalk's safety ROI (Region of Interest), it triggers an API call to the Vanetza stack to broadcast a decentralized notification to the network.
    
3.  **The Environment Simulator (`/simulador`):**
    A virtual testbed (built with **JavaScript/HTML**) that simulates urban traffic and pedestrian behavior. It provides the necessary telemetry and visual triggers to validate the detection logic and the latency of the V2X message propagation.

### 🛠️ Technology Stack

* **Communication:** [Vanetza](https://github.com/riebl/vanetza) (ETSI ITS-G5 stack: Facilities, Networking & Transport, Security).
* **Message Standards:** Likely utilizing **DENM** (Decentralized Environmental Notification Message) for pedestrian hazard alerts.
* **Logic & Backend:** **Python** for detection processing and V2X trigger orchestration.
* **Frontend & Simulation:** **JavaScript** and **HTML** for the interactive environment and real-time monitoring dashboard.
* **Deployment:** **Docker & Docker Compose** for microservices isolation and networking.

### Demo
Check out the simulation and the system in action:
🎥 **[Watch the Simulation Video on YouTube](https://youtu.be/o6qV1tiywO0)**

