# Task 2 - Weather Data Pipeline

## Overview

This project demonstrates a simple end-to-end ETL pipeline using the Open-Meteo public API and Google BigQuery.

The pipeline fetches weather forecast data, transforms it into a cleaner analytical structure, and stores it in BigQuery for querying and analysis.

---

# Why Open-Meteo API?

I selected Open-Meteo because:
- it is free and publicly accessible
- no API key is required
- the API returns structured JSON data
- it is suitable for demonstrating ETL concepts clearly

---

# Pipeline Architecture

```text
Open-Meteo API
        ↓
Fetch Layer (requests)
        ↓
Transformation Layer (pandas)
        ↓
BigQuery Storage
        ↓
SQL Analytics
```

---

# Features Implemented

## Data Fetching
- parameterized API requests
- logging support
- graceful error handling

## Data Transformation
- flattened nested API response
- handled structured hourly data
- converted timestamps into readable format
- added derived analytical field:
  - weather_condition

## BigQuery Integration
- created dataset and schema manually
- uploaded transformed dataframe
- prevented duplicate ingestion using WRITE_TRUNCATE

## SQL Analytics
Implemented aggregation query to analyze:
- average temperature
- total records grouped by weather condition

---

# Project Structure

```text
task-2-data-pipeline/
│
├── main.py
├── config.py
├── fetch_weather.py
├── transform.py
├── bigquery_loader.py
├── requirements.txt
├── queries/
│   └── summary.sql
└── assets/
```

---

# How to Run

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Add service account credentials

Place:
```text
service_account.json
```

inside:
```text
task-2-data-pipeline/
```

---

## 3. Run pipeline

```bash
python main.py
```

---

# BigQuery Setup

Dataset:
```text
weather_pipeline
```

Table:
```text
weather_data
```

---

# Sample SQL Query

```sql
SELECT
    weather_condition,
    AVG(temperature) AS average_temperature,
    COUNT(*) AS total_records
FROM
    `sound-country-464003-n4.weather_pipeline.weather_data`
GROUP BY
    weather_condition
ORDER BY
    average_temperature DESC;
```

---

# Production Considerations

## Scheduling
In production, the pipeline could be scheduled using:
- cron jobs
- Apache Airflow
- Cloud Scheduler

## Monitoring
Pipeline failures could be monitored using:
- logging
- alerting systems
- retry mechanisms

## Scaling Improvements
If data volume increased significantly:
- partitioned BigQuery tables could be used
- asynchronous ingestion could be added
- incremental loading strategies could be implemented
- orchestration tools like Airflow could manage workflows

---

# Future Improvements

- direct API integrations for multiple cities
- automated orchestration
- dashboard visualization layer
- real-time weather streaming
- historical trend analysis

---

# Author

Anand Kumar D