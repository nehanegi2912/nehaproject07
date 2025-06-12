




import mysql.connector 
import pandas as pd
import matplotlib.pyplot as plt 

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',         # Replace with your MySQL username
    password='op93452912@N',     # Replace with your MySQL password
    database='sales_trend'
)

# Query to get product-wise revenue and quantity
query = """
SELECT 
    Product Name AS product,
    SUM(Units Sold) AS total_qty,
    SUM(Units Sold * Unit Price) AS revenue
FROM order
GROUP BY product;
"""

# Load into DataFrame
df = pd.read_sql(query, conn)

# Print results
print("📦 Sales Summary:\n", df)

# Plot revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title('Revenue by Product')
plt.ylabel('Revenue (INR)')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close connection
conn.close()
