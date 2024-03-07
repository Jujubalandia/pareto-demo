# Data Pareto Interactivity Basic & Sily

An Online Application for Interactive Pareto Distribution Graph of Product Revenue. This web-based application allows users to interactively generate and visualize a graph showcasing the Pareto distribution (80/20 rule) of revenue for up to 5 products. Users can input or modify product names and revenue values, with the application dynamically updating to reflect these changes in both graph and summary form.

## Overview

This application is built using Python and the Streamlit library, enabling a seamless integration of frontend and backend functionalities. The app's architecture is straightforward, with Streamlit handling both user inputs through an editable table and the dynamic rendering of the Pareto distribution graph and summary section.

## Features

- **Interactive Input Table:** Users can input or edit names and revenue values for up to 5 products.
- **Dynamic Graph Generation:** The application automatically generates a graph depicting the Pareto distribution of product revenues.
- **Summary of Key Contributors:** A summary is provided, highlighting the products that contribute to 80% of the total revenue, in line with the Pareto principle.
- **Random Value Initialization:** On launch, the application populates the input table with random product names and revenue values.

## Getting Started

### Requirements

- Python
- Streamlit
- Matplotlib or Seaborn (for graph generation)
- Pandas and NumPy (for data manipulation)

### Quickstart

1. Ensure all requirements are installed by running `pip install streamlit pandas numpy matplotlib seaborn` in your terminal.
2. Download the project files to your local machine.
3. Navigate to the project directory and run the application with `streamlit run app.py`.

### License

Copyright BMoura (c) Feel Free to Use and Abuse, All Consequences are Yours 2024.