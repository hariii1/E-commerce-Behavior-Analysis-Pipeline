# E-commerce Behavior Analysis Pipeline

This project sets up an automated data pipeline using Apache Airflow to analyze e-commerce consumer behavior. The pipeline extracts raw data from a PostgreSQL database, processes it to categorize cities and map regions, and generates insights into purchasing frequencies and payment options across different demographics and geographical areas in India.

## Project Structure

* `data_souls.py`: Defines the Apache Airflow DAG responsible for orchestrating the data extraction and analysis workflow.
* `script.py`: Contains the `data()` function to connect to a PostgreSQL database (named `DataENG`) and extract the `e_commerce` table into a Pandas DataFrame.
* `main.py`: Imports data from `script.py` and performs data cleaning, feature engineering (e.g., `Citytype`, `Region`), and analytical aggregations. It also generates visualizations (count plots) for payment preferences and purchase frequency across regions.
* `hello.py`: A simple Python script executed as part of the Airflow DAG for demonstration or testing purposes.

## Technologies Used

* Python
* Pandas: For data manipulation and analysis.
* Psycopg2: Python adapter for PostgreSQL.
* Apache Airflow: For workflow orchestration.
* Seaborn & Matplotlib: For data visualization.
* PostgreSQL: As the data source.

## Data Source

The project connects to a PostgreSQL database named `DataENG` and queries the `e_commerce` table. This table is expected to contain various attributes related to online shopping behavior, such as `city`, `purchasefrequency`, `paymentoption`, `Browsetime`, and `retailersshopped`.

## Setup and How to Run

1.  **Database Setup:** Ensure you have a PostgreSQL instance running with a database named `DataENG` and an `e_commerce` table populated with relevant data. Update the database connection details (host, port, user, password, dbname) in `script.py` if different from the default.
2.  **Airflow Environment:** Set up an Apache Airflow environment. You will need to place `data_souls.py`, `script.py`, `main.py`, and `hello.py` in your Airflow DAGs folder.
3.  **Install Dependencies:** Install the required Python libraries:
    ```bash
    pip install pandas psycopg2-binary apache-airflow seaborn matplotlib tabulate
    ```
4.  **Run the Airflow DAG:**
    * Start your Airflow scheduler and webserver.
    * Unpause the `Data_souls` DAG in the Airflow UI.
    * Trigger the DAG manually or wait for its scheduled run.

    The DAG `Data_souls` will execute the following tasks:
    * `print_date`: Prints the current working directory.
    * `sleep`: Pauses for 5 seconds.
    * `run`: Executes `hello.py` (ensure the path in `data_souls.py` is correct for your Airflow worker).

    The `main.py` script, which performs the core analysis and visualization, is intended to be run either as part of an Airflow task (if integrated) or independently after data extraction via `script.py`.

## Key Analysis and Insights

The `main.py` script provides the following analytical insights:

* **Comparison of Online Shopping Behaviors by City Type:** Analyzes and compares the modal `purchasefrequency`, `paymentoption`, `Browsetime`, and `retailersshopped` between 'Metropolitan' (Delhi, Bangalore) and 'Non_Metropolitan' cities.
* **Regional Payment Preferences:** Visualizes the distribution of payment options across different regions in India (`North` for Delhi, `South` for Bangalore).
* **Regional Purchase Frequency:** Illustrates the frequency of purchases across the defined regions.

These analyses help understand varying consumer behaviors based on urban classification and geographical location.
