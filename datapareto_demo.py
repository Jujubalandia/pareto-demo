import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    try:
        st.title('Demo Pareto Distribution')
        # Implementing the Alpha Input Field
        alpha = st.number_input('Alpha', min_value=0.0, max_value=5.0, value=1.0, step=0.1)
        st.write(f'Current alpha value: {alpha}')  # Logging the current alpha value
        
        product_revenues = {}  # Dictionary to store product revenues
        all_revenues_filled = True  # Flag to check if all revenues are filled
        for i in range(1, 6):  # Loop from 1 to 5 for five products
            # Generate label for each product
            label = f'Product {i}'
            # Use st.number_input to get revenue input for each product, ensuring it's a float
            revenue = st.number_input(label, min_value=0.0, format="%.2f", key=f'product_{i}')
            # Store the input in the dictionary
            product_revenues[label] = revenue
            # Check if any revenue input is missing or zero
            if revenue <= 0:
                all_revenues_filled = False
        st.write("Product Revenues:", product_revenues)  # Logging the product revenues
        
        # Separate logic for button's enabled state
        button_enabled = all_revenues_filled

        # Conditionally displaying the 'Generate Results' button based on 'button_enabled' state
        if button_enabled:
            if st.button('Generate Results'):
                # Convert product revenues to a pandas DataFrame for easier manipulation
                df_products = pd.DataFrame(list(product_revenues.items()), columns=['Product', 'Revenue'])
                df_products.sort_values(by='Revenue', ascending=False, inplace=True)  # Sorting products by revenue in descending order

                # Applying the Pareto distribution formula
                # Calculate the Pareto distribution values for each product revenue
                x_m = min(df_products['Revenue'])  # Assuming the minimum revenue as x(m)
                df_products['ParetoDistribution'] = df_products['Revenue'].apply(lambda x: 1 - (x_m / x) ** alpha if x >= x_m else 0)

                # Calculate cumulative revenue to sort and identify the top 80%
                df_products['CumulativeRevenue'] = df_products['Revenue'].cumsum()
                total_revenue = df_products['Revenue'].sum()
                df_products['CumulativePercentage'] = 100 * df_products['CumulativeRevenue'] / total_revenue

                # Identify the products that contribute to the top 80% of revenues
                top_80_cutoff = df_products[df_products['CumulativePercentage'] <= 80]
                if not top_80_cutoff.empty:
                    # Store results in session state for access in other parts of the app if necessary
                    st.session_state['pareto_results'] = top_80_cutoff
                    st.write("Top 80% Products by Revenue:", top_80_cutoff)
                else:
                    st.error("Unable to calculate top 80% products based on revenue. Please check the revenue inputs.")

                # Plotting the graph using the sorted order of products
                fig, ax = plt.subplots()
                ax.bar(range(1, len(df_products['Product']) + 1), df_products['Revenue'], tick_label=df_products['Product'], label='Revenue')
                ax.set_xlabel('Product')
                ax.set_ylabel('Revenue')
                ax.set_title('Products Pareto Revenues 80/20')

                # Plotting the Pareto line
                sorted_revenue = df_products['Revenue'].sort_values(ascending=False).reset_index(drop=True)
                pareto_line_y = [sorted_revenue[0] * (1 - (alpha / 5)) ** (x-1) for x in range(len(sorted_revenue))]
                ax.plot(range(1, len(df_products['Product']) + 1), pareto_line_y, color='r', label='Pareto Line')
                ax.legend()

                st.pyplot(fig)

                # Displaying the results in a table format
                st.write("Results Table: Products contributing to the top 80% of revenues")
                if 'pareto_results' in st.session_state:
                    st.dataframe(st.session_state['pareto_results'][['Product', 'Revenue']])
                else:
                    st.write("No results to display. Please generate results first.")

                # Placeholder for additional results or processing feedback
                st.write("Pareto distribution analysis completed.")
        else:
            st.warning("Please fill in all revenue values to enable the 'Generate Results' button.")
    except Exception as e:
        st.error("An error occurred in the application.")
        st.error(str(e))  # Ensure to log the full error message and trace

if __name__ == '__main__':
    main()