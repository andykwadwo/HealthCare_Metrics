import pandas as pd

# Input and output files
input_file = "PBJ_Daily_Nurse_Staffing_Q2_2024.csv"
output_file = "cleaned.csv"

# Load CSV
df = pd.read_csv(input_file, encoding='cp1252')

# Remove completely empty rows and columns
df = df.dropna(how="all")
df = df.dropna(axis=1, how="all")

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove leading/trailing whitespace from text columns
text_columns = df.select_dtypes(include=["object"]).columns
df[text_columns] = df[text_columns].apply(lambda col: col.str.strip())

# Remove duplicate rows
df = df.drop_duplicates()

# Reset row numbers
# df = df.reset_index(drop=True)

# Save cleaned CSV
df.to_csv(output_file, index=False)

print(f"Cleaned CSV saved to: {output_file}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
