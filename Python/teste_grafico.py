import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot y versus x as lines
ax.plot(x, y)

# Set labels for x and y axis
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')

# Set title of the plot
ax.set_title('Title of the plot')

# Display the plot
plt.show()