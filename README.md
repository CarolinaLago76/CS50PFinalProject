# CS50PFinalProject
Final project in the course CS50P at HarvardX. The intent of this program is to get 2 or more Company Tickers from user and plot their historical prices on a graph for comparison.
# Stock Market Performance Visualizer
#### Video Demo: [YouTube URL]
#### Description:

Stock Market Performance Visualizer is a Python application that allows users to input a list of stock tickers and visualize the relative performance of those stocks over time. The project uses the yfinance library to fetch historical stock data and leverages the power of Pandas and Matplotlib for data manipulation and visualization.

The project consists of a single file, `project.py`, which contains the main function and four custom functions. The main function takes care of calling the other functions in sequence to create the final visualization. Here's a brief description of each custom function:

- `get_tickers()`: This function prompts the user to enter the number of stock tickers they want to compare and then collects the ticker symbols from the user.

- `prepare_dataframe(tickers)`: This function takes the list of tickers as input and fetches the historical stock data using the yfinance library. It then returns a Pandas DataFrame with the adjusted closing prices of the stocks.

- `calculate_relative_performance(df)`: This function takes the DataFrame and calculates the relative performance of each stock by dividing its price by the initial price. It helps to compare the stocks' performance over time more easily.

- `create_plot(df)`: This function takes the prepared DataFrame and visualizes the stocks' relative performance over time using Matplotlib. It generates a line plot with the x-axis representing time and the y-axis representing the relative performance.

To ensure the quality of the project, we created a `test_project.py` file containing test functions for `prepare_dataframe` and `calculate_relative_performance` using the pytest library.

#### Requirements:

This project uses the following libraries:

- pandas: A powerful library for data manipulation and analysis.
- matplotlib: A plotting library for creating static, animated, and interactive visualizations in Python.
- yfinance: A library to fetch financial data from Yahoo Finance.

