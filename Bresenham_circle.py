import matplotlib.pyplot as plt
import numpy as np

def plot_circle_points(x_center, y_center, x, y, points):
    """ add all symmetric points of a circle."""
    points.append((x_center + x, y_center + y))
    points.append((x_center - x, y_center + y))
    points.append((x_center + x, y_center - y))
    points.append((x_center - x, y_center - y))
    points.append((x_center + y, y_center + x))
    points.append((x_center - y, y_center + x))
    points.append((x_center + y, y_center - x))
    points.append((x_center - y, y_center - x))

def bresenham_circle(x_center, y_center, radius):
    points = []
    x = 0
    y = radius
    d = 3 - 2 * radius  # Initial decision parameter
    second_octant_points = [] 
    plot_circle_points(x_center, y_center, x, y, points)
    while x <= y:
        # Collect 2nd Octant Points (top-right)
        second_octant_points.append(( y_center + x,x_center + y))

        x += 1
        if d <= 0:
            d = d + 4 * x + 6
        else:
            y -= 1
            d = d + 4 * (x - y) + 10
        
        plot_circle_points(x_center, y_center, x, y, points)

# Print the points in the 2nd octant
    print("Second Octant Points:")
    for i, point in enumerate(second_octant_points, start=1):
        print(f"P{i}={point}") 

    return points

def draw_circle(x_center, y_center, radius):
    points = bresenham_circle(x_center, y_center, radius)
    x_coords, y_coords = zip(*points)

    # Plotting points
    plt.plot(x_coords, y_coords, 'rs')
    plt.xticks(np.arange(-6, 9, 1))
    plt.yticks(np.arange(-6, 9, 1))
    plt.title("Bresenham Algorithm Points")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()

# Example usage:
draw_circle(1, 1, 7)
