# Personal_Coding_projects
CDC Data and more

# CDC Vaccine Data Retrieval

## Overview

This project uses Python to retrieve vaccine-related public health data from the Centers for Disease Control and Prevention (CDC) open data platform. It connects to the CDC's Socrata API, retrieves records from a selected dataset, and converts the results into a pandas DataFrame for further analysis.

The goal of this project is to develop practical skills in accessing public health datasets programmatically and preparing data for biomedical data analysis.

## Features

- Connects to the CDC's Socrata data platform.
- Retrieves records from the selected CDC dataset (`vh55-3he6`).
- Uses environment variables to configure API credentials.
- Converts API results into a pandas DataFrame.
- Displays the first five records for an initial inspection of the data.

## Technologies Used

- **Python** — Main programming language.
- **pandas** — Data manipulation and DataFrame creation.
- **Sodapy** — Python client for interacting with the Socrata API.
- **CDC Open Data Platform** — Source of public health data.

## Dataset

- **Source:** CDC Open Data
- **Dataset ID:** `vh55-3he6`
- **Platform:** Socrata Open Data API
- **Records retrieved:** Up to 2,000 per query

Dataset contents and availability may change over time. Consult the CDC data portal for the current dataset description and metadata.

## Prerequisites

Before running this project, install:

- Python 3.10 or later
- pip
- A CDC/Socrata application token and any additional credentials required by your chosen authentication method

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YOUR_REPOSITORY
   ```

3. Install the required Python packages:

   ```bash
   pip install pandas sodapy
   ```

## Configuration

Configure the required environment variables before running the script.

The current code references these variables:

| Environment variable | Purpose |
|---|---|
| `CDC_Password` | CDC/Socrata account password |
| `CDC_API_KEY` | Application token used in the separately defined API URL |
| `CDC_API_Secret_KEY` | Defined in the script but not currently used |
| `CDC_Project_1_Token` | Application token passed to the Sodapy client |

Set these variables in your local environment. Do not publish passwords, secret keys, or actual tokens in this repository.

The application token passed to Sodapy is separate from the username and password arguments in the current implementation. Confirm which authentication method is required for your dataset and account before running the script.

## Usage

Run the Python script from your terminal:

```bash
python main.py
```

Replace `main.py` with the actual filename if your script uses a different name.

The script retrieves up to 2,000 records from the selected dataset, converts the results into a pandas DataFrame, and prints the first five rows.

## Example Output

The program displays a preview of the retrieved dataset:

```text
   [column_1]  [column_2]  [column_3]
0         ...         ...         ...
1         ...         ...         ...
2         ...         ...         ...
3         ...         ...         ...
4         ...         ...         ...
```

The actual column names and values depend on the dataset returned by the CDC API.

## Future Improvements

Potential next steps for this project include:

- Explore dataset metadata and document the available variables.
- Add error handling for API requests and authentication failures.
- Save retrieved records to CSV for reproducible analysis.
- Clean missing or inconsistent data.
- Generate summary statistics and visualizations.
- Investigate trends in vaccine-related public health data.

## Author

Developed as a Python and biomedical data analysis learning project.
