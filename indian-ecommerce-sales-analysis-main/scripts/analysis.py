import pandas as pd
import os

# ---------------------------------------------------------
# Step 1: Load CSV data
# ---------------------------------------------------------

def load_merged_data():
    file_path = os.path.join("data", "merged_orders.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError("merged_orders.csv not found in /data folder")

    df = pd.read_csv(file_path)

    print("Loaded merged_orders.csv")
    print(df.head())

    return df


# ---------------------------------------------------------
# Step 2: Clean Date Column
# ---------------------------------------------------------

def clean_date(df):
    # Convert 'Order Date' to datetime (handles dd-mm-yyyy)
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    # Check for invalid dates
    invalid_dates = df["Order Date"].isna().sum()

    if invalid_dates > 0:
        print(
            f"Warning: {invalid_dates} rows had invalid dates "
            "and were set to NaT"
        )

    print("Converted 'Order Date' to datetime format")

    return df


# ---------------------------------------------------------
# Step 3: Add Time Features
# ---------------------------------------------------------

def add_time_features(df):
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month_Name"] = df["Order Date"].dt.strftime("%b")
    df["Quarter"] = df["Order Date"].dt.quarter
    df["Day"] = df["Order Date"].dt.day
    df["Weekday"] = df["Order Date"].dt.weekday
    df["Weekday_Name"] = df["Order Date"].dt.strftime("%A")

    print("Added Year, Month, Quarter, Day, Weekday columns")

    return df


# ---------------------------------------------------------
# Step 4: Save cleaned file
# ---------------------------------------------------------

def save_clean_file(df):
    output_path = os.path.join(
        "data",
        "merged_orders_cleaned.csv"
    )

    df.to_csv(output_path, index=False)

    print(f"Saved cleaned file to {output_path}")


# ---------------------------------------------------------
# Step 5: Monthly Sales Analysis
# ---------------------------------------------------------

def monthly_sales_analysis(df):
    monthly_df = (
        df.groupby(
            ["Year", "Month", "Month_Name"]
        )
        .agg(
            Total_Sales=("Amount", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .reset_index()
        .sort_values(["Year", "Month"])
    )

    print("\nMonthly Sales Analysis:")
    print(monthly_df.head())

    output_path = os.path.join(
        "data",
        "monthly_sales.csv"
    )

    monthly_df.to_csv(
        output_path,
        index=False
    )

    print("Saved monthly_sales.csv to data/")

    return monthly_df


# ---------------------------------------------------------
# Step 6: Compare Monthly Sales with Sales Targets
# ---------------------------------------------------------

def compare_sales_vs_target(df):
    """
    Compare monthly sales with sales targets.

    Args:
        df (DataFrame): Monthly sales dataframe with
                        'Year' and 'Month' columns

    Returns:
        merged (DataFrame): Monthly sales merged with targets,
                            including difference and achievement percentage
    """

    # Load sales target CSV
    target_path = os.path.join(
        "data",
        "Sales Target.csv"
    )

    if not os.path.exists(target_path):
        raise FileNotFoundError(
            "Sales Target.csv not found in /data folder"
        )

    targets = pd.read_csv(target_path)

    print("\nLoaded Sales Target.csv:")
    print(targets.head())

    # Convert Month of Order Date to datetime
    targets["Month_Date"] = pd.to_datetime(
        targets["Month of Order Date"],
        format="%b-%y"
    )

    # Extract Year and Month
    targets["Year"] = targets["Month_Date"].dt.year
    targets["Month"] = targets["Month_Date"].dt.month

    # Merge monthly sales with targets
    merged = pd.merge(
        df,
        targets,
        on=["Year", "Month"],
        how="left"
    )

    # Calculate difference
    merged["Difference"] = (
        merged["Total_Sales"] - merged["Target"]
    )

    # Calculate achievement percentage
    merged["Achievement_pct"] = (
        merged["Total_Sales"] /
        merged["Target"]
    ) * 100

    # Reorder columns
    cols_order = [
        "Year",
        "Month",
        "Month_Name",
        "Total_Sales",
        "Total_Profit",
        "Category",
        "Target",
        "Difference",
        "Achievement_pct"
    ]

    merged = merged[
        [c for c in cols_order if c in merged.columns]
    ]

    print("\nMonthly Sales vs Target:")
    print(merged.head())

    # Save output
    output_path = os.path.join(
        "data",
        "monthly_sales_vs_target.csv"
    )

    merged.to_csv(
        output_path,
        index=False
    )

    print("Saved monthly_sales_vs_target.csv to data/")

    return merged


# ---------------------------------------------------------
# Step 7: Save Final Outputs
# ---------------------------------------------------------

def save_outputs(monthly_df, sales_vs_target_df):
    """
    Save the key analysis results to CSV files.
    """

    # Ensure outputs folder exists
    output_dir = "outputs"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save monthly sales
    monthly_path = os.path.join(
        output_dir,
        "monthly_sales.csv"
    )

    monthly_df.to_csv(
        monthly_path,
        index=False
    )

    print(f"Saved monthly sales to {monthly_path}")

    # Save monthly sales vs target
    target_path = os.path.join(
        output_dir,
        "monthly_sales_vs_target.csv"
    )

    sales_vs_target_df.to_csv(
        target_path,
        index=False
    )

    print(
        f"Saved monthly sales vs target to {target_path}"
    )

    print("\nAll key outputs saved successfully!")


# ---------------------------------------------------------
# Step 8: Deeper Insights & Trends
# ---------------------------------------------------------

def top_customers(df, top_n=10):

    top_cust = (
        df.groupby("CustomerName")["Amount"]
        .sum()
        .reset_index()
    )

    top_cust = (
        top_cust
        .sort_values(
            by="Amount",
            ascending=False
        )
        .head(top_n)
    )

    print("\nTop Customers by Revenue:")
    print(top_cust)

    # Save to CSV
    output_path = os.path.join(
        "outputs",
        "top_customers.csv"
    )

    top_cust.to_csv(
        output_path,
        index=False
    )

    print(
        f"Saved top customers to {output_path}\n"
    )

    return top_cust


def category_sales(df):

    cat_df = (
        df.groupby("Category")[["Amount", "Profit"]]
        .sum()
        .reset_index()
    )

    cat_df = cat_df.sort_values(
        by="Amount",
        ascending=False
    )

    print("\nCategory-wise Sales & Profit:")
    print(cat_df)

    # Save to CSV
    output_path = os.path.join(
        "outputs",
        "category_sales.csv"
    )

    cat_df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Saved category-wise sales to {output_path}\n"
    )

    return cat_df


def state_sales(df):

    state_df = (
        df.groupby("State")[["Amount", "Profit"]]
        .sum()
        .reset_index()
    )

    state_df = state_df.sort_values(
        by="Amount",
        ascending=False
    )

    print("\nState-wise Sales & Profit:")
    print(state_df)

    # Save to CSV
    output_path = os.path.join(
        "outputs",
        "state_sales.csv"
    )

    state_df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Saved state-wise sales to {output_path}\n"
    )

    return state_df


def monthly_trends(monthly_df):

    trends_df = (
        monthly_df
        .groupby(
            ["Year", "Month", "Month_Name"]
        )[["Total_Sales", "Total_Profit"]]
        .sum()
        .reset_index()
    )

    print("\nMonthly Sales Trends:")
    print(trends_df)

    # Save to CSV
    output_path = os.path.join(
        "outputs",
        "monthly_trends.csv"
    )

    trends_df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Saved monthly trends to {output_path}\n"
    )

    return trends_df


# ---------------------------------------------------------
# Step A1: Profitability Analysis
# ---------------------------------------------------------

def category_profitability(df):
    """
    Compute total sales, total profit and profit margin
    per Category.
    """

    cat = (
        df.groupby("Category")
        .agg(
            Total_Sales=("Amount", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Quantity=("Quantity", "sum")
        )
        .reset_index()
    )

    # Profit margin
    cat["Profit_Margin_pct"] = (
        cat["Total_Profit"] /
        cat["Total_Sales"].replace(0, pd.NA)
    ) * 100

    cat = cat.sort_values(
        "Total_Profit",
        ascending=False
    )

    # Save
    out = os.path.join(
        "outputs",
        "category_profitability.csv"
    )

    cat.to_csv(
        out,
        index=False
    )

    print(
        f"Saved category profitability -> {out}"
    )

    return cat


def state_profitability(df):
    """
    Compute total sales, total profit and profit margin
    per State.
    """

    st = (
        df.groupby("State")
        .agg(
            Total_Sales=("Amount", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Quantity=("Quantity", "sum")
        )
        .reset_index()
    )

    st["Profit_Margin_pct"] = (
        st["Total_Profit"] /
        st["Total_Sales"].replace(0, pd.NA)
    ) * 100

    st = st.sort_values(
        "Total_Profit",
        ascending=False
    )

    out = os.path.join(
        "outputs",
        "state_profitability.csv"
    )

    st.to_csv(
        out,
        index=False
    )

    print(
        f"Saved state profitability -> {out}"
    )

    return st


def monthly_profit_trend(df):
    """
    Create month-level profit summary.
    """

    # Ensure time features are present
    if (
        "Year" not in df.columns
        or "Month" not in df.columns
        or "Month_Name" not in df.columns
    ):

        df["Order Date"] = pd.to_datetime(
            df["Order Date"],
            errors="coerce",
            dayfirst=True
        )

        df["Year"] = df["Order Date"].dt.year
        df["Month"] = df["Order Date"].dt.month
        df["Month_Name"] = (
            df["Order Date"].dt.strftime("%b")
        )

    monthly = (
        df.groupby(
            ["Year", "Month", "Month_Name"]
        )
        .agg(
            Total_Sales=("Amount", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .reset_index()
        .sort_values(["Year", "Month"])
    )

    out = os.path.join(
        "outputs",
        "monthly_profit_trend.csv"
    )

    monthly.to_csv(
        out,
        index=False
    )

    print(
        f"Saved monthly profit trend -> {out}"
    )

    return monthly


def subcategory_profit(df, top_n=10):
    """
    Top and bottom sub-categories by profit.
    """

    sub = (
        df.groupby("Sub-Category")
        .agg(
            Total_Sales=("Amount", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Quantity=("Quantity", "sum")
        )
        .reset_index()
    )

    sub["Profit_Margin_pct"] = (
        sub["Total_Profit"] /
        sub["Total_Sales"].replace(0, pd.NA)
    ) * 100

    sub_sorted = sub.sort_values(
        "Total_Profit",
        ascending=False
    )

    top = sub_sorted.head(top_n)

    bottom = (
        sub_sorted
        .tail(top_n)
        .sort_values("Total_Profit")
    )

    out_top = os.path.join(
        "outputs",
        f"subcategory_profit_top{top_n}.csv"
    )

    out_bottom = os.path.join(
        "outputs",
        f"subcategory_profit_bottom{top_n}.csv"
    )

    top.to_csv(
        out_top,
        index=False
    )

    bottom.to_csv(
        out_bottom,
        index=False
    )

    print(
        f"Saved top {top_n} sub-categories -> {out_top}"
    )

    print(
        f"Saved bottom {top_n} sub-categories -> {out_bottom}"
    )

    return top, bottom


# ---------------------------------------------------------
# Step A2: Business KPI Analysis
# ---------------------------------------------------------

def business_kpis(df):
    """
    Calculate important business KPIs.

    KPIs:
    - Total Revenue
    - Total Profit
    - Total Quantity Sold
    - Total Orders
    - Profit Margin
    - Average Order Value
    - Average Quantity per Order
    - Profitable Orders
    - Loss-Making Orders
    """

    total_revenue = df["Amount"].sum()

    total_profit = df["Profit"].sum()

    total_quantity = df["Quantity"].sum()

    total_orders = df["Order ID"].nunique()

    # Profit margin
    profit_margin = (
        (total_profit / total_revenue) * 100
        if total_revenue != 0
        else 0
    )

    # Average Order Value
    average_order_value = (
        total_revenue / total_orders
        if total_orders != 0
        else 0
    )

    # Average quantity per order
    average_quantity_per_order = (
        total_quantity / total_orders
        if total_orders != 0
        else 0
    )

    # Count profitable and loss-making orders
    profitable_orders = (
        df.groupby("Order ID")["Profit"]
        .sum()
        .gt(0)
        .sum()
    )

    loss_orders = (
        df.groupby("Order ID")["Profit"]
        .sum()
        .lt(0)
        .sum()
    )

    # Create KPI DataFrame
    kpis = pd.DataFrame({
        "KPI": [
            "Total Revenue",
            "Total Profit",
            "Total Quantity Sold",
            "Total Orders",
            "Profit Margin (%)",
            "Average Order Value",
            "Average Quantity per Order",
            "Profitable Orders",
            "Loss-Making Orders"
        ],

        "Value": [
            total_revenue,
            total_profit,
            total_quantity,
            total_orders,
            round(profit_margin, 2),
            round(average_order_value, 2),
            round(average_quantity_per_order, 2),
            profitable_orders,
            loss_orders
        ]
    })

    print("\n========== BUSINESS KPIs ==========")

    print(
        kpis.to_string(index=False)
    )

    # Save KPI output
    output_dir = "outputs"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(
        output_dir,
        "business_kpis.csv"
    )

    kpis.to_csv(
        output_path,
        index=False
    )

    print(
        f"\nSaved business KPIs -> {output_path}"
    )

    return kpis


# ---------------------------------------------------------
# Main runner
# ---------------------------------------------------------

if __name__ == "__main__":

    # Step 1: Load data
    df = load_merged_data()

    # Step 2: Clean dates
    df = clean_date(df)

    # Step 3: Add time features
    df = add_time_features(df)

    # Step 4: Save cleaned data
    save_clean_file(df)

    print(
        "\nBase preprocessing completed successfully."
    )

    # Step 5: Monthly sales
    monthly_df = monthly_sales_analysis(df)

    print(
        "\nBase preprocessing + Monthly sales completed."
    )

    # Step 6: Sales vs Target
    sales_vs_target_df = compare_sales_vs_target(
        monthly_df
    )

    print(
        "\nMonthly sales analysis + target comparison completed."
    )

    # Step 7: Save outputs
    save_outputs(
        monthly_df,
        sales_vs_target_df
    )

    print(
        "\nFull analysis completed!"
    )

    # Step 8: Insights & Trends
    top_customers(df)

    category_sales(df)

    state_sales(df)

    monthly_trends(monthly_df)

    print(
        "\nAll analysis completed successfully! "
        "Check the 'outputs/' folder for CSV files."
    )

    # Step A1: Profitability Analysis
    category_profit = category_profitability(df)

    state_profit = state_profitability(df)

    monthly_profit = monthly_profit_trend(df)

    top_sub, bottom_sub = subcategory_profit(
        df,
        top_n=10
    )

    # Step A2: Business KPI Analysis
    kpi_df = business_kpis(df)

    print(
        "\nBusiness KPI analysis completed successfully!"
    )

    print(
        "\n========== ALL ANALYSIS COMPLETED =========="
    )