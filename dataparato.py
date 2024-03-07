#dataparato.py

# Importing necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate random product names and values - helper function
def generate_random_data():
    product_names = [f"Product {i}" for i in range(1, 6)]
    revenue_values = np.random.randint(1000, 50000, size=5)
    return pd.DataFrame({"Product Name": product_names, "Revenue": revenue_values})

# Function to calculate Pareto distribution
def calculate_pareto_distribution(dataframe):
    try:
        # Sort the DataFrame based on Revenue in descending order
        sorted_df = dataframe.sort_values('Revenue', ascending=False)
        
        # Calculate the total revenue
        total_revenue = sorted_df['Revenue'].sum()
        
        # Calculate the cumulative revenue percentage
        sorted_df['Cumulative Revenue'] = sorted_df['Revenue'].cumsum()
        sorted_df['Cumulative Percentage'] = (sorted_df['Cumulative Revenue'] / total_revenue) * 100
        
        # Identify the set of products contributing to the top 80% of the total revenue
        pareto_products_df = sorted_df[sorted_df['Cumulative Percentage'] <= 80]
        
        # Return the DataFrame containing Pareto products and their cumulative percentage
        return pareto_products_df
    except Exception as e:
        st.error("An error occurred during Pareto distribution calculation.")
        print(f"An error occurred during Pareto distribution calculation: {e}")

# Function to generate and display the Pareto graph
def generate_pareto_graph(pareto_df):
    try:
        fig, ax = plt.subplots()
        ax.bar(pareto_df['Product Name'], pareto_df['Revenue'], color='SkyBlue')
        ax2 = ax.twinx()
        ax2.plot(pareto_df['Product Name'], pareto_df['Cumulative Percentage'], color='DarkRed', marker='o', ms=7)
        
        ax.set_xlabel('Product Name')
        ax.set_ylabel('Revenue', color='SkyBlue')
        ax2.set_ylabel('Cumulative Percentage', color='DarkRed')
        
        plt.title('Pareto Distribution of Product Revenues')
        st.pyplot(fig)
    except Exception as e:
        st.error("An error occurred during graph generation.")
        print(f"An error occurred during graph generation: {e}")

# Setting up the Streamlit application structure
def main():
    try:
        # Sidebar for user inputs
        st.sidebar.header("Product Revenue Input")
        
        # Temporary storage for user inputs
        if 'user_data' not in st.session_state:
            st.session_state.user_data = generate_random_data()

        # Input form in the sidebar
        with st.sidebar.form(key='input_form'):
            product_names = [st.text_input(f"Product {i} Name", value=st.session_state.user_data['Product Name'].iloc[i-1]) for i in range(1, 6)]
            revenue_values = [st.number_input(f"Product {i} Revenue", min_value=0, value=int(st.session_state.user_data['Revenue'].iloc[i-1])) for i in range(1, 6)]
            submit_button = st.form_submit_button(label='Submit')

        # Update session state upon submission
        if submit_button:
            st.session_state.user_data = pd.DataFrame({"Product Name": product_names, "Revenue": revenue_values})

        # Display the DataFrame in the main area (temporary for verification)
        st.title("Interactive Pareto Distribution of Product Revenue")
        st.write("Current Data:", st.session_state.user_data)
        
        if 'user_data' in st.session_state:
            # Calculate Pareto distribution
            pareto_df = calculate_pareto_distribution(st.session_state.user_data)
            # Generate and display the graph
            generate_pareto_graph(pareto_df)
            
            # Generate and display the summary
            top_contributors = pareto_df[['Product Name', 'Revenue']]
            st.write("Summary: Products contributing to 80% of total revenue")
            st.table(top_contributors)

    except Exception as e:
        st.error("An error occurred in initializing the application.")
        st.error(f"Error details: {e}")
        print(f"An exception occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred while running the application: {e}")