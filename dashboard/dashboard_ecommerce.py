import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
order_distribution_path = "order_distribution.csv"
top_customer_regions_path = "top_customer_regions.csv"

order_distribution_df = pd.read_csv("order_distribution.csv")
top_customer_regions_df = pd.read_csv("top_customer_regions.csv")



# Adjusting the order of regions in the top_customer_regions dataset
if top_customer_regions_df['Orders'].dtype == 'object':
    top_customer_regions_df['Orders'] = top_customer_regions_df['Orders'].str.replace('.', '').astype(int)

# Streamlit app
st.title("E-Commerce Data Dashboard")

# Section 1: Order Distribution
st.header("Order Distribution")
if not order_distribution_df.empty:
    st.write("### Do Customers Frequently Order from the Same Seller?")
    st.write("This section analyzes the distribution of orders to determine if customers often order from the same seller.")
    
    # Summary statistics
    total_combinations = 96880  # Total unique customer-seller pairs
    single_order_customers = 87581  # Customers who ordered only once from the same seller
    repeat_order_customers = 9299  # Customers who ordered more than once from the same seller

    st.write(f"**Total Unique Customer-Seller Pairs:** {total_combinations}")
    st.write(f"**Customers with Single Orders:** {single_order_customers} ({(single_order_customers / total_combinations) * 100:.2f}%)")
    st.write(f"**Customers with Repeat Orders:** {repeat_order_customers} ({(repeat_order_customers / total_combinations) * 100:.2f}%)")

    # Visualize the distribution
    labels = ['Single Order', 'Repeat Orders']
    sizes = [single_order_customers, repeat_order_customers]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'orange'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
else:
    st.write("Order distribution data is unavailable.")

# Section 2: Top Customer Regions
st.header("Top Customer Regions")
if not top_customer_regions_df.empty:
    st.write("### Orders by Region")
    st.dataframe(top_customer_regions_df)

    # Plotting the regions
    fig, ax = plt.subplots()
    ax.barh(top_customer_regions_df['Region'], top_customer_regions_df['Orders'], color='skyblue')
    ax.set_xlabel('Number of Orders')
    ax.set_ylabel('Region')
    ax.set_title('Top Customer Regions by Orders')
    st.pyplot(fig)
else:
    st.write("Top customer regions data is unavailable.")

# Run the app
# Save this script as `app.py` and run with the command: `streamlit run app.py