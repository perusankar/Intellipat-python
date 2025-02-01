import matplotlib.pyplot as plt
import mpld3

# Create a simple plot
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

# Convert the plot to HTML
html_str = mpld3.fig_to_html(plt.gcf())

# Save the HTML to a file or embed it in a web page
with open("plot.html", "w") as f:
    f.write(html_str)