# Page View Time Series Visualizer

A Python data visualization project developed as part of the freeCodeCamp *Data Analysis with Python* certification. This program uses **Pandas**, **Matplotlib**, and **Seaborn** to visualize daily page views on the freeCodeCamp.org forum from May 2016 to December 2019 to identify growth patterns and seasonal trends.

---

## Key Features & Visualizations

* **Data Cleaning:** Filters out extreme outliers by removing page views in the top 2.5% and bottom 2.5% of the dataset.
* **Line Chart (`draw_line_plot`):** Visualizes daily page view trends over time with labeled axes and custom chart titles.
* **Bar Chart (`draw_bar_plot`):** Groups average daily page views by year and month with a proper chronological legend.
* **Box Plots (`draw_box_plot`):** Generates adjacent Seaborn box plots to analyze yearly trends and monthly seasonality distributions.

---

## Tech Stack

* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Visualizations:** Matplotlib, Seaborn
* **Testing:** Unittest framework

---

## Project Structure

* `time_series_visualizer.py`: Contains the core data wrangling and plotting functions.
* `main.py`: Entry point script used to execute visual generation and tests locally.
* `test_module.py`: Official unit test suite validating figure types, labels, and elements.
* `fcc-forum-pageviews.csv`: The underlying time series dataset.
