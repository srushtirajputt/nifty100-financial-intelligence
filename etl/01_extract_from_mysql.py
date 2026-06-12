import pandas as pd
import os

# Source folder containing Excel files
RAW_DATA_PATH = "data/raw"

# Output folder for CSV files
OUTPUT_PATH = "data/raw"

files = [
    "companies.xlsx",
    "analysis.xlsx",
    "balancesheet.xlsx",
    "profitandloss.xlsx",
    "cashflow.xlsx",
    "prosandcons.xlsx",
    "documents.xlsx"
]

print("\n===== EXTRACTION STARTED =====\n")

for file in files:
    file_path = os.path.join(RAW_DATA_PATH, file)

    try:
        # Read Excel file
        df = pd.read_excel(file_path, engine="openpyxl")

        # Generate CSV filename
        csv_name = file.replace(".xlsx", ".csv")
        csv_path = os.path.join(OUTPUT_PATH, csv_name)

        # Save as CSV
        df.to_csv(csv_path, index=False)

        print(f"✓ {file}")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {list(df.columns)}")
        print("-" * 50)

    except Exception as e:
        print(f"✗ Error processing {file}")
        print(e)

print("\n===== EXTRACTION COMPLETED =====")