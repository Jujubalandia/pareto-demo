# Demo Pareto Data Products Distribution

This web application, leveraging the Pareto distribution concept, is designed to help users identify the most profitable products based on their revenue values, adhering to the 80/20 principle. Utilizing the Streamlit Python library, it offers a user-friendly interface for inputting product revenues and an alpha value to generate and visualize the distribution of product revenues in a Pareto graph.

## Overview

The application is built with Streamlit, a powerful library that simplifies the creation of web apps for data science projects. The architecture is straightforward, featuring a single-page application that dynamically updates based on user inputs. The project is structured with a main app file (`app.py`) that handles all the user interactions and data processing.

## Features

- **Alpha Input Field**: Allows users to input a float value for alpha, affecting the Pareto distribution curve.
- **Product Revenue Input**: Enables input of revenue values for five different products.
- **Generate Results Button**: Computes the Pareto distribution and updates the graph and results table based on the given inputs.
- **Graph Area**: Displays the Pareto distribution graph, illustrating the revenue distribution among the products.
- **Results Table**: Lists the products contributing to the top 80% of revenues post-distribution calculation.

## Getting started

### Requirements

- Python 3.6 or newer
- Streamlit library

### Quickstart

1. Clone the repository to your local machine.
2. Install Streamlit using `pip install streamlit`.
3. Navigate to the project directory and run `streamlit run app.py` in your terminal to start the application.

### License

Copyright (c) 2024.