# csv_cleaner.py
# Purpose: Clean a CSV file by removing duplicates and handling null values
# Author: shrustie patil
# Date: June 13, 2026

import pandas as pd
import os
import numpy as np

def load_csv(filepath):
    """Load CSV file and return DataFrame."""
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return None
    df = pd.read_csv(filepath)
    print(f"Loaded file: {filepath}")
    print(f"Original shape: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def remove_duplicates(df):
    """Remove duplicate rows from DataFrame."""
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    removed = before - after
    print(f"\n--- Duplicate Removal ---")
    print(f"Duplicates removed: {removed}")
    print(f"Rows remaining: {after}")
    return df

def fill_nulls(df):
    """Fill null values based on column data type."""
    print(f"\n--- Null Value Handling ---")
    for column in df.columns:
        null_count = df[column].isnull().sum()
        if null_count > 0:
            # Check if column is numeric (int or float)
            if pd.api.types.is_numeric_dtype(df[column]):
                df[column] = df[column].fillna(df[column].mean())
                print(f"{column}: filled {null_count} nulls with mean value ({df[column].mean():.2f})")
            else:
                # Fill string/object columns with "Unknown"
                df[column] = df[column].fillna("Unknown")
                print(f"{column}: filled {null_count} nulls with 'Unknown'")
        else:
            print(f"{column}: no nulls found ✅")
    return df

def save_clean_csv(df, filepath):
    """Save cleaned DataFrame to a new CSV file."""
    clean_path = filepath.replace(".csv", "_cleaned.csv")
    df.to_csv(clean_path, index=False)
    print(f"\nCleaned file saved to: {clean_path}")

def main():
    filepath = "file-handling/sample_data.csv"
    
    df = load_csv(filepath)
    if df is None:
        return
    
    df = remove_duplicates(df)
    df = fill_nulls(df)
    save_clean_csv(df, filepath)
    
    print("\n--- Final Shape ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print("\nCleaning complete ✅")

if __name__ == "__main__":
    main()