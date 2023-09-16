import numpy as np
import matplotlib.pyplot as plt

def getIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # Check if the second line is horizontal (constant y-value)
    x1_log = np.log(x1)
    x2_log = np.log(x2)
    x3_log = np.log(x3)
    x4_log = np.log(x4)
    
    denom = (x1_log - x2_log) * (x3_log - x4_log) - (y1 - y2) * (x3_log - x4_log)
    px_log = ((x1_log * y2 - y1 * x2_log) * (x3_log - x4_log) - (x1_log - x2_log) * (x3_log * y4 - y3 * x4_log)) / denom
    py = ((x1_log * y2 - y1 * x2_log) * (y3 - y4) - (y1 - y2) * (x3_log * y4 - y3 * x4_log)) / denom
    px = np.exp(px_log)
    
    return px

def factor_assay_analysis(reference, samples):
    # Reference data
    reference_x = np.array(reference['activity'])
    reference_y = np.array(reference['time'])

    # Extend the x-range for the line of best fit
    x_extension = 20  # Adjust as needed to extend the line
    ref_extension = 12 # Adjust as needed to extend the start reference line

    # Initialize a list to store Factor VIII values
    factor_viii_values = []

    plt.figure(figsize=(10, 8))

    # Plot reference data
    # plt.scatter(reference_x, reference_y, label="Reference", marker='s')
    reference_fit = np.polyfit(np.log(reference_x), reference_y, 1)
    reference_fit_line = np.poly1d(reference_fit)
    x_min_reference, x_max_reference = min(reference_x), max(reference_x)
    x_range_reference = np.linspace(x_min_reference - ref_extension, x_max_reference + x_extension, 100)
    plt.plot(x_range_reference, reference_fit_line(np.log(x_range_reference)), label="Control", linestyle='--')

    # Step 1: Plot each sample data set on a Log Lin graph
    for k, data in samples.items():
        x_data = np.array(data['activity'])
        y_data = np.array(data['time'])

        # Plot sample data
    #     plt.scatter(x_data, y_data, label=f"Sample {i+1}", marker='o')

        # Step 2: Plot a line of best fit
        fit = np.polyfit(np.log(x_data), y_data, 1)
        fit_line = np.poly1d(fit)

        # Extend the x-values for the line of best fit
        x_min, x_max = min(x_data), max(x_data)
        x_range = np.linspace(x_min - 5, x_max + x_extension, 100)

        plt.plot(x_range, fit_line(np.log(x_range)), label=k, linestyle='--')

        # Step 3: Plot a line from (100, 0) to the Fit Line
        y_intersection = fit_line(np.log(100))
        plt.plot([100, 100], [0, y_intersection], linestyle=':', color='black')

        # Step 4: Plot a line from the intersection to the y-axis
        plt.plot([100, 0], [y_intersection, y_intersection], linestyle=':', color='black')

        # Calculate the x-coordinate of the intersection point
        x_intersection = getIntersect(
            x_range_reference[0], reference_fit_line(np.log(x_range_reference))[0],
            x_range_reference[-1], reference_fit_line(np.log(x_range_reference))[-1],
            1, y_intersection, 100, y_intersection
        )

        factor_viii_values.append(x_intersection)

        # Step 5: Plot a line from the intersection to the x-axis
        plt.plot([x_intersection, x_intersection], [0, y_intersection], linestyle=':', color='black')

#         # Step 6: Output the value on the X-axis where the line in Step 5 touches the x-axis
#         plt.scatter(x_intersection, 0, color='black', label=f'{k} Factor VIII: {x_intersection:.2f}%', marker='x')

    # Set x-axis to logarithmic scale
    x_ticks = [12.5, 25, 50, 100]  # X-values where you want to place custom labels
    x_labels = ['1/80', '1/40', '1/20', '1/10']  # Custom labels for those points
    
    plt.xscale('log')
    plt.xticks(x_ticks, x_labels)
    
    plt.xlabel("% Activity")
    plt.ylabel("Time")
    plt.title("Factor Assay Analysis")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True, which='both', linestyle='--')

    # Set x-axis limits
    plt.xlim(1, 300)  # Adjust the limits as needed
    plt.ylim(0, 250)
    plt.show()

    for i, value in enumerate(factor_viii_values):
        print(f"The Factor VIII for Sample {i+1} is at {value:.2f}%")
