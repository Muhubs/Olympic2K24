# Olympic2K24

![Olympic Rings](https://github.com/user-attachments/assets/a597db17-34d8-4465-a5e3-9ff112296c84)

## Overview
This project demonstrates how to create a data pipeline using Apache Airflow to extract and process Olympic ranking data. The goal is to extract ranking data from the Olympic website, map the country names and their total medals, order them by the number of medals, and send the results using Line Notify.

## Features
- **Data Extraction:** Retrieve ranking data from the official Olympic website.
- **Data Processing:** Extract country names and total medals.
- **Data Mapping:** Map the extracted data for clarity.
- **Data Ordering:** Order the countries by their total medal count.
- **Notification:** Send the ordered data to a Line chat using Line Notify.

## Components
- **Apache Airflow:** Orchestrates the data extraction, processing, and notification tasks.
- **Line Notify:** Sends the final ordered medal data to a specified Line chat.

## Getting Started

### Prerequisites
- Python 3.7+
- Apache Airflow
- Line Notify Token
