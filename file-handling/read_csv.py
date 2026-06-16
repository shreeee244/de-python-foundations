# read_csv.py
# Purpose: Read a CSV file, display its contents, and count missing values
# Author: Your Name
# Date: June 12, 2026

import pandas as pd
import os

def load_csv(filepath):
    """Load a CSV file and return a DataFrame."""
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return None
    
    df = pd.read_csv(filepath)
    print(f"Successfully loaded: {filepath}")
    return df


def display_basic_info(df):
    """Print basic information about the dataset."""
    print("\n--- Dataset Shape ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n--- Column Names ---")
    print(df.columns.tolist())
    
    print("\n--- First 5 Rows ---")
    print(df.head())


def count_nulls(df):
    """Count and display null values in each column."""
    print("\n--- Null Value Count ---")
    null_counts = df.isnull().sum()
    
    for column, count in null_counts.items():
        status = "⚠️  has nulls" if count > 0 else "✅ clean"
        print(f"{column}: {count} nulls — {status}")
    
    total_nulls = null_counts.sum()
    print(f"\nTotal missing values: {total_nulls}")


def main():
    # Update this path to your CSV file
    filepath = "file-handling/sample_data.csv"
    
    df = load_csv(filepath)
    
    if df is not None:
        display_basic_info(df)
        count_nulls(df)


if __name__ == "__main__":
    main()