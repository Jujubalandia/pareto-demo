import streamlit as st
import pandas as pd
import numpy as np
import matplotlib

def main():
    try:
        st.title('Demo Pareto Distribution')
        # Implementing the Alpha Input Field
        alpha = st.number_input('Alpha', min_value=0.0, max_value=5.0, value=1.0, step=0.1)
        st.write(f'Current alpha value: {alpha}')  # Logging the current alpha value
        
        product_revenues = {}  # Dictionary to store product revenues
        for i in range(1, 6):  # Loop from 1 to 5 for five products
            # Generate label for each product
            label = f'Product {i}'
            # Use st.number_input to get revenue input for each product, ensuring it's a float
            revenue = st.number_input(label, min_value=0.0, format="%.2f", key=f'product_{i}')
            # Store the input in the dictionary
            product_revenues[label] = revenue
        st.write("Product Revenues:", product_revenues)  # Logging the product revenues
        
        # Implementing the 'Generate Results' button
        if st.button('Generate Results'):
            # Convert product revenues to a pandas DataFrame for easier manipulation
            df_products = pd.DataFrame(list(product_revenues.items()), columns=['Product', 'Revenue'])

            # Applying the Pareto distribution formula
            # Calculate the Pareto distribution values for each product revenue
            x_m = min(df_products['Revenue'])  # Assuming the minimum revenue as x(m)
            df_products['ParetoDistribution'] = df_products['Revenue'].apply(lambda x: 1 - (x_m / x) ** alpha if x >= x_m else 0)

            # Calculate cumulative revenue to sort and identify the top 80%
            df_products['CumulativeRevenue'] = df_products['Revenue'].cumsum()
            total_revenue = df_products['Revenue'].sum()
            df_products['CumulativePercentage'] = 100 * df_products['CumulativeRevenue'] / total_revenue
            df_products_sorted = df_products.sort_values(by='Revenue', ascending=False)

            # Identify the products that contribute to the top 80% of revenues
            top_80_cutoff = df_products_sorted[df_products_sorted['CumulativePercentage'] <= 80]
            if not top_80_cutoff.empty:
                # Store results in session state for access in other parts of the app if necessary
                st.session_state['pareto_results'] = top_80_cutoff
                st.write("Top 80% Products by Revenue:", top_80_cutoff)
            else:
                st.error("Unable to calculate top 80% products based on revenue. Please check the revenue inputs.")

            # Plotting the graph using the original order of products
            fig, ax = matplotlib.pyplot.subplots()
            # Order the df_products by 'Product' for plotting
            df_products_ordered = df_products.sort_values(by='Product')
            ax.bar(df_products_ordered['Product'], df_products_ordered['Revenue'], label='Revenue')
            ax.set_xlabel('Product')
            ax.set_ylabel('Revenue')
            ax.set_title('Products Pareto Revenues 80/20')

            # Plotting the Pareto line
            pareto_line_x = np.arange(1, len(df_products_ordered['Product']) + 1)
            pareto_line_y = [max(df_products_ordered['Revenue']) * (1 - (alpha / 5)) ** (x-1) for x in pareto_line_x]
            ax.plot(pareto_line_x, pareto_line_y, color='r', label='Pareto Line')
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
    except Exception as e:
        st.error("An error occurred in the application.")
        st.error(str(e))  # Ensure to log the full error message and trace

if __name__ == '__main__':
    main()