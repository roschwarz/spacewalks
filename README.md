[![CI](https://github.com/roschwarz/spacewalks/actions/workflows/main.yml/badge.svg)](https://github.com/roschwarz/spacewalks/actions/workflows/main.yml)

# Spacewalks



## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12 
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation

## Installation

Create your python envorinment.

```
python3 -m venv venv_spacewalks
```

Activate the envorinment

```
source venv_spacewalks/bin/activate
```

Install the requirements

```
python3 -m pip install -r requirements.txt
```

## Usage Example

```
python3 eva_data_analysis.py <input.file> <output.file>
```