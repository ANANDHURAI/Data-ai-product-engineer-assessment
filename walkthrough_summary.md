# Walkthrough Summary

## Task 1 - Product Scoping

For the product scoping task, I focused on designing a simple internal dashboard for marketing teams.

My primary goal was to avoid overengineering and instead focus on:
- usability
- workflow compatibility
- realistic v1 scope

I intentionally excluded advanced features such as AI recommendations and real-time integrations in order to keep the initial version lightweight and easier to adopt.

I also considered user trust, data consistency, and operational simplicity while defining the product scope.

---

## Task 2 - Data Pipeline

For the pipeline task, I built a complete ETL workflow using the Open-Meteo API and Google BigQuery.

The pipeline:
1. fetches weather data
2. transforms nested API responses into tabular format
3. adds derived analytical fields
4. uploads cleaned data into BigQuery
5. runs SQL aggregation queries for analysis

While building the pipeline, I focused on:
- clear structure
- parameterization
- logging
- graceful error handling
- clean schema design

I also improved timestamp readability and handled duplicate ingestion using WRITE_TRUNCATE in BigQuery loading.

---

## What I Would Improve With More Time

- automated scheduling
- monitoring and alerting
- CI/CD integration
- dashboard visualization
- multi-source ingestion
- automated testing