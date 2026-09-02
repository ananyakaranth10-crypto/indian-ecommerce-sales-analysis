# Indian E-Commerce Sales Analysis

An end-to-end **Data Analytics portfolio project** using **Python,
MySQL, and Power BI** to transform Indian e-commerce transaction data
into business insights and interactive dashboards.

## 📌 Project Overview

This project analyzes e-commerce order data to understand sales, profit,
customers, categories, sub-categories, monthly trends, and state-wise
performance.

The workflow covers:

**Raw Data → Data Cleaning → Python Analysis → MySQL SQL Analysis →
Power BI Dashboard → Business Insights**

## 🎯 Objectives

-   Clean and preprocess e-commerce sales data.
-   Perform exploratory and business analysis using Python.
-   Analyze sales, profit, quantity, customers, and orders.
-   Store cleaned data in MySQL.
-   Perform SQL-based business analysis.
-   Build an interactive Power BI dashboard.
-   Identify high-performing customers, categories, sub-categories, and
    states.
-   Identify loss-making sub-categories and areas requiring attention.

## 🛠️ Tech Stack

  Technology         Purpose
  ------------------ -------------------------------
  Python             Data cleaning and analysis
  Pandas             Data manipulation
  NumPy              Numerical operations
  Matplotlib         Visualization
  Seaborn            Visualization
  MySQL              Database and SQL analysis
  Power BI           Interactive dashboard
  DAX                KPI calculations
  Jupyter Notebook   Exploratory analysis
  GitHub             Version control and portfolio

## 📂 Project Structure

``` text
indian-ecommerce-sales-analysis/
│
├── data/
│   ├── List of Orders.csv
│   ├── Order Details.csv
│   ├── merged_orders.csv
│   ├── merged_orders_cleaned.csv
│   └── Sales Target.csv
│
├── scripts/
│   ├── analysis.py
│   ├── visualizations.py
│   └── report_generator.py
│
├── sql/
│   ├── initial.sql
│   ├── queries.sql
│   ├── final.sql
│   ├── advanced_analytics.sql
│   └── stored_procedures.sql
│
├── outputs/
│   └── analysis outputs and plots
│
├── PowerBi/
│   ├── Ecommerce_Dashboard.pbix
│   └── Ecommerce_Dashboard_PowerBi.pdf
│
├── requirements.txt
└── README.md
```

## 🔄 Project Workflow

1.  Load the raw CSV datasets.
2.  Merge and clean the order data using Python.
3.  Create analytical fields such as Year, Month, Quarter, Day, and
    Weekday.
4.  Perform sales, profit, customer, category, sub-category, and state
    analysis.
5.  Generate analytical CSV outputs and visualizations.
6.  Store the cleaned dataset in MySQL.
7.  Run SQL queries for business analysis.
8.  Build an interactive Power BI dashboard.
9.  Present key business insights through KPIs and charts.

## 🐍 Python Analysis

Python is used for:

-   Data loading and preprocessing
-   Dataset merging
-   Data cleaning
-   Missing-value checks
-   Date transformation
-   Monthly sales and profit analysis
-   Sales-target comparison
-   Customer analysis
-   Category and sub-category analysis
-   State-wise analysis
-   Generating analytical outputs
-   Generating visualizations

### Main Dataset Fields

-   Order ID
-   Order Date
-   CustomerName
-   State
-   City
-   Amount
-   Profit
-   Quantity
-   Category
-   Sub-Category
-   Year
-   Month
-   Month_Name
-   Quarter
-   Day
-   Weekday

## 🗄️ MySQL Analysis

The cleaned data is stored in:

**Database:** `ecommerce_sales_db`

**Table:** `orders_cleaned`

SQL analysis includes:

-   Total revenue
-   Total profit
-   Total quantity
-   Monthly revenue
-   State-wise revenue and profit
-   Top customers by revenue
-   Category-wise revenue and profit
-   Daily revenue
-   Advanced business analysis

Example query:

``` sql
SELECT
    Category,
    SUM(Amount) AS TotalRevenue,
    SUM(Profit) AS TotalProfit
FROM orders_cleaned
GROUP BY Category
ORDER BY TotalRevenue DESC;
```

## 📊 Power BI Dashboard

The Power BI report contains two pages.

### 1. Executive Overview

The Executive Overview provides a high-level view of business
performance.

### KPI Cards

-   **Total Sales:** 432K
-   **Total Profit:** 24K
-   **Total Quantity Sold:** 5,615
-   **Total Customers:** 332
-   **Total Orders:** 500
-   **Profit Margin:** 5.55%
-   **Average Order Value:** 863.00

### Visualizations

-   Sales vs Profit
-   Monthly Sales Trend
-   Category-wise Sales
-   Sales by State
-   Profit Margin
-   Average Order Value

Interactive filters:

-   Year
-   Category

### 2. Detailed Analysis

The Detailed Analysis page contains:

-   Top 10 Customers by Sales
-   Category-wise Profit
-   Top 10 Profitable Sub-Categories
-   Bottom 10 Loss-Making Sub-Categories
-   Monthly Profit Trend
-   Profit by State

It also includes Year and Category slicers for interactive analysis.

## 📐 Important DAX Measures

### Total Orders

``` dax
Total Orders =
DISTINCTCOUNT('merged_orders_cleaned'[Order ID])
```

### Total Customers

``` dax
Total Customers =
DISTINCTCOUNT('merged_orders_cleaned'[CustomerName])
```

### Profit Margin

``` dax
Profit Margin =
DIVIDE(
    SUM('merged_orders_cleaned'[Profit]),
    SUM('merged_orders_cleaned'[Amount]),
    0
)
```

### Average Order Value

``` dax
Average Order Value =
DIVIDE(
    SUM('merged_orders_cleaned'[Amount]),
    DISTINCTCOUNT('merged_orders_cleaned'[Order ID]),
    0
)
```

### Average Quantity per Order

``` dax
Average Quantity per Order =
DIVIDE(
    SUM('merged_orders_cleaned'[Quantity]),
    DISTINCTCOUNT('merged_orders_cleaned'[Order ID]),
    0
)
```

## 📈 Key Business Insights

-   Total sales are approximately **432K**.
-   Total profit is approximately **24K**.
-   Overall profit margin is approximately **5.55%**.
-   The major categories are **Electronics, Clothing, and Furniture**.
-   Top customers can be identified using the Top 10 Customers analysis.
-   Profitable and loss-making sub-categories are separately
    highlighted.
-   State-wise analysis helps identify geographic differences in sales
    and profitability.
-   Monthly trends help identify stronger and weaker business periods.

## 🚀 How to Run

### Install dependencies

``` bash
pip install -r requirements.txt
```

### Run Python analysis

``` bash
python scripts/analysis.py
```

### Generate visualizations

``` bash
python scripts/visualizations.py
```

### MySQL

Create/use the `ecommerce_sales_db` database, load the cleaned dataset
into `orders_cleaned`, and execute the SQL scripts in the `sql/`
directory.

### Power BI

Open:

``` text
PowerBi/Ecommerce_Dashboard.pbix
```

Refresh the data if required and use the Year and Category filters to
explore the dashboard.

## 📸 Dashboard Screenshots

Create a `screenshots/` folder and add:

``` text
screenshots/
├── executive-overview.png
└── detailed-analysis.png
```

Then add them to this README:

``` markdown
## Executive Overview

![Executive Overview](screenshots/executive-overview.png)

## Detailed Analysis

![Detailed Analysis](screenshots/detailed-analysis.png)
```

## 💡 Future Enhancements

-   Customer segmentation using clustering
-   Sales forecasting
-   RFM customer analysis
-   Product-level profitability analysis
-   Interactive geographic maps
-   Automated data refresh
-   Machine-learning-based predictions
-   Web-based analytics application

## 📌 Skills Demonstrated

**Python • Pandas • NumPy • Matplotlib • Seaborn • SQL • MySQL • Power
BI • DAX • Data Cleaning • Exploratory Data Analysis • Business
Analytics • Data Visualization • KPI Development • GitHub**

## 👩‍💻 About This Project

This is a **portfolio-focused Data Analytics project** created to
demonstrate an end-to-end workflow from raw transactional data to
business insights.

It combines programming, database analysis, and business intelligence to
show how raw e-commerce data can be transformed into meaningful and
actionable information.

## ⭐ Conclusion

This project demonstrates an end-to-end analytics workflow using
**Python, MySQL, and Power BI**. The final dashboard provides an
interactive view of sales and profitability across customers,
categories, sub-categories, months, and states, while the underlying
Python and SQL analysis provides the foundation for the reported
insights.
