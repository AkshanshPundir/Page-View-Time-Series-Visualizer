import unittest
import time_series_visualizer
import matplotlib as mpl

class TimeSeriesTestCase(unittest.TestCase):
    def setUp(self):
        self.line_fig = time_series_visualizer.draw_line_plot()
        self.bar_fig = time_series_visualizer.draw_bar_plot()
        self.box_fig = time_series_visualizer.draw_box_plot()

    def test_line_plot(self):
        self.assertEqual(type(self.line_fig), mpl.figure.Figure, "Expected draw_line_plot to return a matplotlib figure.")
        self.assertEqual(len(self.line_fig.axes[0].lines), 1, "Expected line plot to have one line.")
        self.assertEqual(self.line_fig.axes[0].get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019", "Expected line plot title to be correct.")
        self.assertEqual(self.line_fig.axes[0].get_xlabel(), "Date", "Expected line plot xlabel to be 'Date'.")
        self.assertEqual(self.line_fig.axes[0].get_ylabel(), "Page Views", "Expected line plot ylabel to be 'Page Views'.")

    def test_bar_plot(self):
        self.assertEqual(type(self.bar_fig), mpl.figure.Figure, "Expected draw_bar_plot to return a matplotlib figure.")
        self.assertEqual(len(self.bar_fig.axes[0].patches), 48, "Expected bar plot to have 48 bars (4 years * 12 months).")
        self.assertEqual(self.bar_fig.axes[0].get_xlabel(), "Years", "Expected bar plot xlabel to be 'Years'.")
        self.assertEqual(self.bar_fig.axes[0].get_ylabel(), "Average Page Views", "Expected bar plot ylabel to be 'Average Page Views'.")

    def test_box_plot(self):
        self.assertEqual(type(self.box_fig), mpl.figure.Figure, "Expected draw_box_plot to return a matplotlib figure.")
        self.assertEqual(len(self.box_fig.axes), 2, "Expected two subplots in the box plot figure.")
        self.assertEqual(self.box_fig.axes[0].get_title(), "Year-wise Box Plot (Trend)", "Expected first box plot title to be 'Year-wise Box Plot (Trend)'.")
        self.assertEqual(self.box_fig.axes[1].get_title(), "Month-wise Box Plot (Seasonality)", "Expected second box plot title to be 'Month-wise Box Plot (Seasonality)'.")

if __name__ == "__main__":
    unittest.main()