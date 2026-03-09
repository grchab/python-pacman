import pandas as pd

# Load your dataset (replace with your file path or existing DataFrame)
file_path = ".csv"  # Replace with the actual file name
df = pd.read_csv(file_path)

# Step 1: Sorting the dataset
# Example: Sorting by TotalSpending in descending order
df_sorted = df.sort_values(by="TotalSpending", ascending=False).reset_index(drop=True)

print("Top 5 Customers by Spending:")
print(df_sorted.head(5))  # Display top 5 spenders

# Step 2: Binary Search Implementation
def binary_search(df, target, column="CustomerID"):
    """Binary search for a target value in a specific column of a sorted DataFrame."""
    low, high = 0, len(df) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = df.loc[mid, column]
        if mid_value == target:
            return df.loc[mid]
        elif mid_value < target:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Example: Searching for a specific CustomerID
target_customer_id = 12345  # Replace with an actual CustomerID from your dataset
result = binary_search(df_sorted, target_customer_id, column="CustomerID")

# Display search result
if result is not None:
    print(f"\nCustomer Details for CustomerID {target_customer_id}:")
    print(result)
else:
    print(f"\nCustomerID {target_customer_id} not found.")
