# YouTube API – ELT Data Pipeline

End-to-end ELT data pipeline built using Python, PostgreSQL, Apache Airflow, and Docker.  
The project extracts data from the YouTube API, orchestrates workflows with Airflow DAGs, and ensures data quality through automated testing and CI/CD.

---

## Motivation

The goal of this project is to gain hands-on experience with modern data engineering tools and best practices by building a robust ELT pipeline.  
The project focuses on:
- workflow orchestration
- containerized infrastructure
- data quality validation
- automated testing and CI/CD

---

## Data Source

The pipeline uses the **YouTube Data API** as the data source.  
Data is extracted from a public YouTube channel (*MrBeast*), but the pipeline is fully reusable for any other channel by changing the channel ID or handle.

### Extracted Fields
- Video ID  
- Video Title  
- Upload Date  
- Duration  
- View Count  
- Like Count  
- Comment Count  

---

## Pipeline Overview

The ELT pipeline follows these steps:

1. **Extract**  
   - Data is extracted from the YouTube API using Python scripts.

2. **Load (Staging Layer)**  
   - Raw data is loaded into a `staging` schema in a Dockerized PostgreSQL database.

3. **Transform & Load (Core Layer)**  
   - Lightweight transformations are applied using Python.
   - Cleaned data is loaded into a `core` schema optimized for analysis.

The initial execution performs a **full load**, while subsequent runs **upsert** updated values into the core tables.

---

## Orchestration

Workflow orchestration is handled using **Apache Airflow**.  
Three DAGs are executed sequentially and can be monitored via the Airflow UI (`http://localhost:8080`):

- **produce_json** – Extracts raw data and generates JSON files  
- **update_db** – Loads data into staging and core schemas  
- **data_quality** – Runs data quality checks on both layers  

---

## Containerization

The entire stack is containerized using **Docker** and **Docker Compose**.

Key points:
- Airflow is deployed using an extended Docker image built via a custom Dockerfile.
- Environment variables are used for Airflow connections and variables:
  - `AIRFLOW_CONN_<CONN_ID>`
  - `AIRFLOW_VAR_<VARIABLE_NAME>`
- A Fernet key is used to encrypt sensitive credentials.
- Docker images are built and tested automatically through CI/CD pipelines.

---

## Data Storage

Data is stored in a Dockerized **PostgreSQL** database.  
The database can be accessed using:
- `psql` inside the container
- External tools such as **DBeaver**

---

## Testing & Data Quality

The project includes both **unit testing** and **data quality validation**:

- **pytest** for unit and integration tests
- **SODA Core** for data quality checks on staging and core tables

---

## CI/CD

Continuous Integration and Deployment are implemented using **GitHub Actions** to:
- build Docker images
- run tests
- validate Airflow DAG integrity
- ensure pipeline stability after code changes

---

## Tools & Technologies

- **Languages:** Python, SQL  
- **Orchestration:** Apache Airflow  
- **Containerization:** Docker, Docker Compose  
- **Data Storage:** PostgreSQL  
- **Testing:** pytest, SODA  
- **CI/CD:** GitHub Actions  

---

## License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.
