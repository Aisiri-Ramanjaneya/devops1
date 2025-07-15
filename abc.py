


import pandas as pd

# Load the original Excel file
input_file = "fraud_feature_matrix.xlsx"  # Update with your actual file name
df = pd.read_excel(input_file)

# Select the required columns
selected_columns = [
    "BILLEDAMOUNT", "PAIDAMOUNT", "TOTALADJUSTMENTAMOUNT", "DENIEDADJUSTMENT",
    "num_diagnoses", "num_procedures", "num_cpt_codes", "total_units",
    "billed_to_paid_ratio", "adjustment_to_billed_ratio", "has_denial"
]
new_df = df[selected_columns]

# Save to a new Excel file
output_file = "filtered_data.xlsx"
new_df.to_excel(output_file, index=False)

print(f"New Excel file saved as {output_file}")
