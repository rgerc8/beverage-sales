# Beverage Sales Analysis Project

## Overview

This project performs data ingestion, cleaning, and profiling analysis on a synthetic beverage sales dataset. The analysis leverages PySpark for handling large-scale data processing, focusing on sales patterns, customer segmentation, and regional trends in the beverage industry.

The dataset simulates realistic sales data, including both Business-to-Business (B2B) and Business-to-Consumer (B2C) transactions, highlighting factors such as regional preferences, seasonal fluctuations, and pricing strategies.

## Dataset Description

The dataset is sourced from Kaggle: [Beverage Sales Dataset](https://www.kaggle.com/datasets/sebastianwillmann/beverage-sales).

### Key Features:
- **Order_ID**: Unique identifier for each order, grouping multiple products within the same order.
- **Customer_ID**: Unique identifier for each customer.
- **Customer_Type**: Indicates B2B or B2C transactions.
- **Product**: Name of the product (e.g., "Coca-Cola", "Erdinger Weißbier").
- **Category**: Product category (e.g., "Soft Drinks", "Alcoholic Beverages").
- **Unit_Price**: Price per unit of the product.
- **Quantity**: Number of units purchased.
- **Discount**: Discount applied (only to B2B customers, e.g., 0.1 for 10%).
- **Total_Price**: Total price after discounts.
- **Region**: Customer region (e.g., "Bayern", "Berlin").
- **Order_Date**: Date of the order.

### Dataset Details:
- **File**: `synthetic_beverage_sales_data.csv`
- **Size**: Approximately 789 MB
- **Rows**: Large-scale dataset for big data analysis
- **Columns**: 11
- **License**: MIT
- **Update Frequency**: Quarterly

This dataset is ideal for analytical purposes such as sales forecasting, customer segmentation, and trend analysis.

## Project Structure

```
beverage-sales/
├── data/
│   ├── raw/
│   │   └── synthetic_beverage_sales_data.csv  # Raw dataset
│   ├── silver/                                # Processed data (if applicable)
│   └── gold/                                  # Final cleaned data (if applicable)
├── notebooks/
│   ├── 01-ingestion.ipynb                     # Data ingestion and cleaning
│   ├── 02-teste.ipynb                         # Additional tests or analysis
│   └── api.ipynb                              # API-related notebook
├── scripts/
│   └── get-data.py                            # Script for data retrieval
├── requirements.txt                           # Python dependencies
└── README.md                                  # This file
```

## Installation and Setup

### Prerequisites
- Python 3.8+
- Java 8+ (required for PySpark)
- Hadoop (for distributed processing, if needed)

### Steps
1. Clone or download the project repository.
2. Create a virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\Activate.ps1`
   - Linux/Mac: `source .venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Ensure Hadoop is installed and configured if running in distributed mode.

## Usage

### Running the Notebooks
1. Start Jupyter Notebook or VS Code with Jupyter extension.
2. Open `notebooks/01-ingestion.ipynb`.
3. Execute the cells to perform data ingestion, cleaning, and profiling.

### Key Analyses
- Data profiling: Basic info, summary statistics, missing values, unique values, distributions, correlations, and outlier detection.
- Sales analysis: By category, region, and monthly trends.

### Scripts
- `scripts/get-data.py`: Utility for data handling.

## Technologies Used
- **PySpark**: For big data processing and analysis.
- **Python**: Core programming language.
- **Jupyter Notebooks**: For interactive analysis.

## License

This project uses the MIT License, in line with the dataset's license.

## Contributing

Feel free to submit issues or pull requests for improvements. Feedback on the dataset and analysis is welcome.

## Acknowledgments

- Dataset provided by Sebastian Willmann on Kaggle.
- Inspired by real-world beverage industry patterns.