# ERP Inventory Forecasting with AI Assistant

> **An intelligent ERP demand forecasting system built using FastAPI, PostgreSQL, multiple Machine Learning models, and Ollama (Llama 3) for AI-powered business insights.**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange)
![Ollama](https://img.shields.io/badge/Ollama-Llama3-purple)

---

# Project Overview

Modern ERP systems require accurate demand forecasting to optimize inventory, reduce stockouts, and improve supply chain planning.

This project predicts the next **30 days of product demand** using multiple forecasting models and automatically selects the best-performing model based on evaluation metrics. The system also integrates **Ollama (Llama 3)** to generate AI-powered business insights and inventory recommendations from forecast results.

---

# Features

- Multi-model demand forecasting
- Automatic best model selection
- FastAPI REST API
- PostgreSQL database integration
- Feature engineering pipeline
- Model evaluation using MAE, RMSE and MAPE
- AI-generated forecast explanation using Ollama (Llama 3)
- Interactive Swagger documentation
- Enterprise-ready modular architecture

---

# Technology Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

### Machine Learning
- XGBoost
- SARIMA
- LSTM
- Temporal Fusion Transformer (TFT)

### AI
- Ollama
- Llama 3

---

# System Architecture

```text
                 ERP Database
                (PostgreSQL)
                      │
                      ▼
            Feature Engineering
                      │
                      ▼
       ┌───────────────────────────┐
       │ Multiple ML Models        │
       │                           │
       │ • XGBoost                 │
       │ • SARIMA                  │
       │ • LSTM                    │
       │ • TFT                     │
       └─────────────┬─────────────┘
                     │
                     ▼
         Automatic Best Model Selection
                     │
                     ▼
           30-Day Demand Forecast
                     │
                     ▼
          Ollama (Llama 3)
                     │
                     ▼
      AI Business Recommendation
                     │
                     ▼
             FastAPI JSON Response
```

---

# Project Structure

```text
ERP_Demand_Forecasting
│
├── app
│   ├── forecasting
│   │   ├── xgboost_model.py
│   │   ├── sarima_model.py
│   │   ├── lstm_model.py
│   │   └── tft_model.py
│   │
│   ├── services
│   │   └── ai_service.py
│   │
│   ├── main.py
│   ├── schemas.py
│   ├── preprocessing.py
│   ├── evaluation.py
│   ├── model_registry.py
│   ├── database.py
│   └── config.py
│
├── training
│   └── train_all_models.py
│
├── models
├── requirements.txt
├── README.md
└── .env
```

---

# Machine Learning Models

| Model | Description |
|--------|-------------|
| XGBoost | Gradient boosting model for feature-based demand prediction |
| SARIMA | Statistical time-series forecasting |
| LSTM | Deep learning model for sequential demand prediction |
| TFT | Transformer-based forecasting model |

The system automatically selects the best-performing model based on evaluation metrics.

---

# AI Business Assistant

The forecasting results are analysed using **Ollama (Llama 3)**.

Instead of only returning numerical predictions, the AI generates:

- Demand trend analysis
- Increase/decrease summary
- Inventory recommendation
- Business-friendly explanation

Example:

```
Forecast:
Day 1 : 64.63 units
Day 2 : 65.79 units
...
```

AI Response:

> Demand is expected to gradually decrease over the next month. Maintain moderate inventory levels while increasing stock during short demand peaks to avoid shortages.

---

# API Endpoints

| Endpoint | Description |
|----------|-------------|
| GET /health | Health Check |
| POST /train | Train all forecasting models |
| GET /forecast | Generate demand forecast |
| GET /models | Display available models and evaluation metrics |

---

## ⚙️ Setup Instructions

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.11+
- PostgreSQL 15+
- Git
- Ollama
- Visual Studio Code (Recommended)

---

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ERP-Demand-Forecasting-AI.git
cd ERP-Demand-Forecasting-AI
```

---

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv311
venv311\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv311
source venv311/bin/activate
```

---

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 4. Configure the Database

Create a PostgreSQL database and update your `.env` file.

Example:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/erp_forecasting
```

---

### 5. Seed the Database

Generate sample ERP data.

```bash
python scripts/seed_data.py
```

---

### 6. Install Ollama

Download Ollama from:

https://ollama.com/download

Pull the Llama 3 model:

```bash
ollama pull llama3
```

Start the Ollama server:

```bash
ollama serve
```

Keep this terminal running while using the application.

---

### 7. Train the Forecasting Models

```bash
python training/train_all_models.py
```

The following models will be trained:

- XGBoost
- SARIMA
- LSTM
- Temporal Fusion Transformer (TFT)

The best-performing model is automatically selected and registered.

---

### 8. Run the FastAPI Application

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

### 9. Open API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

### 10. Test the API

#### Health Check

```
GET /health
```

#### Train Models

```
POST /train
```

#### Generate Forecast

```
GET /forecast
```

#### View Registered Models

```
GET /models
```

---

## 🚀 Project Workflow

```text
PostgreSQL ERP Database
          │
          ▼
Feature Engineering
          │
          ▼
Train ML Models
(XGBoost | SARIMA | LSTM | TFT)
          │
          ▼
Best Model Selection
          │
          ▼
30-Day Demand Forecast
          │
          ▼
Ollama (Llama 3)
          │
          ▼
AI Business Insights
          │
          ▼
FastAPI JSON Response
```
# Sample Forecast Response

```json
{
  "product_id": "P001",
  "warehouse_id": "W001",
  "model_used": "xgboost",
  "forecast_horizon_days": 30,
  "forecast": [
    {
      "day": 1,
      "forecast_units": 64.63
    }
  ],
  "ai_summary": "Demand is expected to gradually decrease over the next month. Maintain moderate inventory levels and avoid overstocking."
}
```

---

# Evaluation Metrics

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- Training Time
- Inference Time

---

# Future Improvements

- Interactive Dashboard
- Docker Deployment
- SAP S/4HANA Integration
- Real-Time Data Streaming
- Weather-aware Demand Forecasting
- Promotion-aware Forecasting

---

# Skills Demonstrated

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Machine Learning
- Time Series Forecasting
- XGBoost
- LSTM
- SARIMA
- Temporal Fusion Transformer (TFT)
- REST API Development
- Ollama
- Llama 3
- AI Integration
- Backend Development

---

# Author

**Abhijith Reddy**

B.Tech Computer Science Engineering

Amrita Vishwa Vidyapeetham
