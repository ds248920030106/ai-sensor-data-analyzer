# AI-Assisted Sensor Data Analyzer

[![Python CI](https://github.com/ds248920030106/ai-sensor-data-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/ds248920030106/ai-sensor-data-analyzer/actions/workflows/ci.yml)

This project is a small AI-assisted Python tool for analyzing engineering sensor data. It reads sensor data from a CSV file, validates the required columns, calculates summary statistics, detects missing values and outliers, generates a markdown report, and saves a plot of sensor readings.

The project was developed as a final project for a generative AI coding course. The goal is not only to build a working tool, but also to demonstrate how generative AI can support coding, debugging, testing, and documentation in an engineering workflow.

## Features

- Load sensor data from a CSV file
- Validate required sensor columns
- Count missing values
- Calculate summary statistics
- Detect outliers using the mean ± 3 standard deviations rule
- Generate a markdown summary report
- Generate a sensor plot
- Include unit tests with pytest
- Support CI testing with GitHub Actions

## Project Structure

```text
ai-sensor-data-analyzer/
├── README.md
├── requirements.txt
├── main.py
├── src/
│   ├── data_loader.py
│   ├── validator.py
│   ├── analyzer.py
│   ├── report_generator.py
│   └── plotter.py
├── data/
│   └── sample_sensor_data.csv
├── outputs/
│   └── .gitkeep
├── tests/
│   ├── test_validator.py
│   └── test_analyzer.py
└── prompts/
```

## Required CSV Format
The input CSV file should include the following columns:
timestamp,temperature,humidity,pressure,accel_x,accel_y,accel_z
An example file is provided at:
data/sample_sensor_data.csv

## Installation
Create and activate a Python environment:
conda create -n sensor-ai python=3.11 -y
conda activate sensor-ai

Install dependencies:
pip install -r requirements.txt

## Usage
Run the analyzer with the sample dataset:
python main.py data/sample_sensor_data.csv

Expected output:
Sensor Data Analysis Complete.
Rows analyzed: 10
Report saved to: outputs/summary_report.md
Plot saved to: outputs/sensor_plot.png

The generated report and plot will be saved in the outputs/ folder.

## Running Tests
Run unit tests using:
python -m pytest
Expected result:
6 passed

## AI-Assisted Development Workflow

Generative AI was used to support several parts of the development process:

1. Creating the initial Python project structure.
2. Generating the first version of the CSV loading and validation logic.
3. Refactoring the code into separate modules.
4. Designing pytest unit tests for edge cases such as missing columns.
5. Improving documentation and README instructions.

However, AI-generated code was not accepted blindly. I reviewed the logic, tested the output, and modified the implementation where needed. For example, I chose not to silently replace all missing values with zero because that could hide real sensor failures. Instead, the tool reports missing values explicitly.

## Engineering Context

In engineering systems, sensor data is often used to monitor system behavior and detect abnormal conditions. This project demonstrates a simple workflow for validating and summarizing sensor data before further analysis. Although the dataset is small, the same structure can be extended to larger sensor datasets from real hardware systems.

## Limitations

* The outlier detection method is simple and based only on mean and standard deviation.
* The tool assumes the input data follows a fixed CSV format.
* The visualization is basic and intended for quick inspection.
* More advanced sensor-specific validation rules could be added in the future.