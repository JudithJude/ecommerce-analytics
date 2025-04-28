# ecommerce-analytics
# 🛠️ Olist ETL Project

This project sets up a full ETL pipeline using Dockerised services. It extracts e-commerce data (Olist dataset from Kaggle), transforms and loads it into a PostgreSQL database, and exposes the data for analysis via Metabase.

---

## 📦 Tech Stack

- **Python**: For ETL (Extract, Transform, Load) logic.
- **PostgreSQL**: Relational database to store the transformed data.
- **pgAdmin**: GUI for managing the PostgreSQL instance.
- **Metabase**: BI tool to build dashboards and explore data.
- **Docker & Docker Compose**: Orchestration for the stack.

---

## 📁 Project Structure

- scripts:
        - `.csvs`: contains raw Olist CSVs from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
- `etl.py`: contains python script to load the CSVs into PostgreSQL.
- `docker-compose.yml`: this spins up the full stack: PostgreSQL, pgAdmin, Metabase, and the ETL service.
- `Dockerfile`: this builds the custom image for running the ETL script.
`requirements.txt`: this contains python dependencies used by the ETL script.
`wait-for-it.sh`: this contains a shell script that waits for the database to be ready (used by Docker).


---

## 🚀 How to Run the Project

### 1. Clone this repository
```bash
git clone https://github.com/judithjude/ecommerce-analytics.git
cd ecommerce-analytics


### 2. Download the Olist Dataset
- Get it from Kaggle - Olist Store Dataset.
- Place all CSV files into the data/ folder.

### 3. Build and Start All Services
docker-compose up --build


📊 Data Pipeline Overview
Extract: Reads all 9 CSVs from the data/ directory.
Transform: Applies type casting and light transformations.
Load: Inserts data into PostgreSQL under properly named tables.


📈 Dashboarding with Metabase

After the data is loaded:
Connect Metabase to the PostgreSQL database (host: postgres, user: postgres, password: postgres, db: olist_db)
Start building charts and dashboards based on:

    Orders by month
    Revenue per seller
    Delivery delays
    Top-selling products
    Customer location breakdowns


🧩 Next Steps
Coming soon in the next phase...
Integrate dbt for data modeling
Create fact and dimension tables
Add tests and documentation
Enable version-controlled SQL transformations

📄 License
This project is for educational purposes and uses the publicly available Olist dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).