# Factor Assay Analysis

This Python function, `factor_assay_analysis`, is a tool designed for analyzing Factor VIII assay data. It takes in reference data and one or more sample datasets, performs several data visualization and analysis steps, and provides insights into Factor VIII values for the samples.

It was built to help a friend with some analysis but i figured it would be helpful to someone else.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Function Description](#function-description)
- [Parameters](#parameters)
- [Example](#example)
- [License](#license)

## Introduction

Factor VIII assay is an important test in the diagnosis and management of bleeding disorders, particularly hemophilia. This function helps you visualize and analyze Factor VIII assay data by plotting the data points, fitting lines of best fit, and calculating Factor VIII values for each sample.

## Usage

You can use this function to analyze Factor VIII assay data by providing the reference data and sample datasets as input. The function performs the following steps:

1. Plots reference data and a line of best fit for the reference.
2. Plots each sample dataset and lines of best fit.
3. Calculates and prints Factor VIII values for each sample.

## Function Description

The function has the following signature:

```python
def factor_assay_analysis(reference, samples):
    # Function code here
```
## Parameters
reference (dict): A dictionary containing reference data with 'activity' and 'time' keys.
samples (dict): A dictionary containing sample datasets with keys representing sample names and values as dictionaries containing 'activity' and 'time' keys.

### Example
Here's an example of how to use the factor_assay_analysis function:

```python
import numpy as np
import matplotlib.pyplot as plt

# Define reference data
reference_data = {
    'activity': [10, 25, 50, 100, 200],
    'time': [180, 100, 60, 40, 30]
}

# Define sample datasets
sample_datasets = {
    'Sample A': {
        'activity': [5, 20, 40, 80, 160],
        'time': [200, 120, 70, 45, 35]
    },
    'Sample B': {
        'activity': [8, 15, 30, 75, 150],
        'time': [190, 110, 65, 42, 33]
    }
}

# Call the function to analyze Factor VIII assay data
factor_assay_analysis(reference_data, sample_datasets)
```

# NOTE
- Function can be modified to return the Factor VIII instead of just printing them out
- There is a helper function included called 'getIntersect' that simply gets the intersection between to lines on a semi log graph

## License
This code is absolutely free.
You are free to use, modify, and distribute it as needed for your purposes.