<p align="center">

# Healthcare Fraud Detection System

### AI-Powered Healthcare Insurance Fraud Detection Platform

Detecting fraudulent healthcare insurance claims using Artificial Intelligence, Machine Learning, FastAPI, React, Azure SQL, and Apache Spark.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=28&pause=1200&color=0F766E&center=true&vCenter=true&width=900&lines=Healthcare+Fraud+Detection+System;AI-Powered+Insurance+Analytics;FastAPI+%7C+React+%7C+Machine+Learning"/>

</p>

---

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Azure SQL](https://img.shields.io/badge/Azure_SQL-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine_Learning-orange?style=for-the-badge)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-Messaging-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)

</p>

---

# Table of Contents

- Overview
- Project Objectives
- Features
- System Architecture
- Machine Learning Pipeline
- Technology Stack
- Project Structure
- Dashboard
- API Endpoints
- Installation
- Future Improvements
- Team

---

# Overview

Healthcare Fraud Detection System is an intelligent enterprise platform that detects fraudulent healthcare insurance claims using Artificial Intelligence and Machine Learning.

The platform integrates real-time claim processing, fraud prediction, provider monitoring, patient management, and interactive dashboards into a single enterprise application.

The main objective is to help insurance companies reduce financial losses caused by fraudulent medical claims while improving claim processing efficiency.

---

# Project Objectives

- Detect fraudulent insurance claims.
- Improve claim review efficiency.
- Reduce insurance fraud.
- Provide real-time fraud prediction.
- Deliver interactive healthcare dashboards.
- Support providers and insurance companies with intelligent analytics.

---

# Key Features

| Feature | Description |
|---------|-------------|
| Fraud Detection | AI-powered claim classification |
| Claim Submission | Submit healthcare claims |
| Claim Tracking | Monitor claim status |
| Insurance Dashboard | Executive analytics dashboard |
| Provider Dashboard | Provider statistics |
| Patient Management | Manage patient records |
| Provider Management | Manage healthcare providers |
| Analytics | Interactive visual reports |
| Authentication | Secure role-based login |
| Machine Learning | XGBoost prediction engine |
| REST APIs | FastAPI backend |
| Azure SQL | Cloud database |

---

# System Architecture

```text
                  Users
                     │
                     ▼
            React + Vite Frontend
                     │
                     ▼
              FastAPI Backend
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
    Azure SQL Database      ML Predictor
                                   │
                                   ▼
                            XGBoost Model
                                   │
                                   ▼
                         Fraud Prediction
                                   │
                                   ▼
                         Interactive Dashboard
```

---

# Machine Learning Pipeline

```
Medical Claims
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Data Encoding
      │
      ▼
Model Training
      │
      ▼
XGBoost
      │
      ▼
Fraud Probability
      │
      ▼
Risk Classification
```

---

# Technology Stack

| Layer | Technologies |
|------|--------------|
| Frontend | React, Vite, Tailwind CSS |
| Backend | FastAPI, Python |
| Database | Azure SQL |
| Machine Learning | XGBoost, Scikit-Learn |
| Big Data | Apache Spark |
| Messaging | RabbitMQ |
| Charts | Chart.js |
| Version Control | Git & GitHub |

---

# Project Structure

```text
Healthcare-Fraud-Detection/
│
├── app/
│   ├── routes.py
│   ├── schemas.py
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── api.js
│
├── ML/
│   ├── predictor.py
│   ├── model.pkl
│   └── preprocessing.py
│
├── services/
│
├── spark/
│
├── core/
│
├── requirements.txt
└── README.md
```

---

# Dashboard

The platform provides two enterprise dashboards.

## Insurance Dashboard

- Executive KPIs
- Total Claims
- Fraud Claims
- Fraud Rate
- Monthly Claims
- Monthly Fraud Trend
- Provider Performance
- Top Providers
- Top Patients
- Risk Distribution
- Claims Timeline

---

## Provider Dashboard

- Submitted Claims
- Approved Claims
- Rejected Claims
- Fraud Alerts
- Recent Claims
- Monthly Activity

---

# REST API

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/login | User Authentication |
| POST | /api/process-claim | Submit Claim |
| GET | /api/stats | Dashboard Statistics |
| GET | /api/my-claims | Claims |
| GET | /api/patients | Patients |
| GET | /api/providers | Providers |

---

# Installation

## Backend

```bash
pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Future Improvements

- Explainable AI
- Deep Learning Models
- Cloud Deployment
- Mobile Application
- Real-time Streaming
- Automatic Model Retraining

---

# Team

| Name | Role |
|------|------|
| Omnya Ayman Roshdy Mohamed | Team Leader |
| Sama Osama Mohamed Younes | Team Member |
| Abdelhamed Ahmed Abdelhamed | Team Member |
| Kareem Ahmed Taha | Team Member | Team Member |
| Laila hesham helmy mohamed  | Team Member
