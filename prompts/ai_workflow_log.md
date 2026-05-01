# AI Workflow Log

This document summarizes how generative AI was used during the development of the AI-Assisted Sensor Data Analyzer project. The goal was not to accept AI-generated code blindly, but to use AI as a coding assistant while keeping human judgment, testing, and engineering reasoning in the loop.

## Prompt 1: Defining the Project Idea

**Prompt**

I asked the AI to help design a small final project for a generative AI coding course. I wanted the project to be simple enough to finish, but still relevant to engineering workflows.

**AI Suggestion**

The AI suggested building an AI-assisted sensor data analysis tool. The tool would read sensor data from a CSV file, validate the format, calculate summary statistics, detect missing values and outliers, and generate a report.

**My Decision**

I accepted this idea because it matched my engineering background and could be demonstrated without relying on real hardware. A CSV-based workflow also made the project easier to test and reproduce.

## Prompt 2: Creating the Initial Code Structure

**Prompt**

I asked the AI to propose a clean Python project structure with separate files for loading data, validating data, analyzing data, generating reports, plotting results, and testing.

**AI Suggestion**

The AI suggested separating the project into modules such as `data_loader.py`, `validator.py`, `analyzer.py`, `report_generator.py`, and `plotter.py`.

**My Decision**

I accepted the modular structure because it made the code easier to explain, test, and maintain. This also helped the final project look like a real software repository instead of one large script.

## Prompt 3: Generating and Refining the Analysis Logic

**Prompt**

I asked the AI to generate Python functions for counting missing values, calculating summary statistics, and detecting outliers in sensor columns.

**AI Suggestion**

The AI generated functions using pandas and suggested detecting outliers using the mean ± 3 standard deviations rule.

**My Decision**

I accepted the simple outlier detection method because it was easy to explain during a short presentation. However, I also documented it as a limitation because this method may not work well for all real sensor datasets.

## Prompt 4: Handling Missing Values

**Prompt**

I asked the AI how to handle missing sensor values in the dataset.

**AI Suggestion**

One possible AI suggestion was to fill missing values with zero or another default value.

**My Decision**

I rejected silently replacing missing values with zero. In an engineering system, missing sensor values may indicate a real hardware or data collection problem. Replacing them automatically could hide important failures. Instead, the project reports missing values explicitly.

## Prompt 5: Writing Unit Tests

**Prompt**

I asked the AI to help create pytest unit tests for the validator and analyzer modules.

**AI Suggestion**

The AI suggested tests for valid columns, missing columns, missing value counts, summary statistics, outlier detection output, and the combined analysis result.

**My Decision**

I accepted these testing ideas and used them to verify the project. The tests helped catch import and packaging issues, such as needing an `__init__.py` file in the `src` folder.

## Prompt 6: Adding GitHub Actions CI

**Prompt**

I asked the AI how to add a simple GitHub Actions workflow to automatically run pytest.

**AI Suggestion**

The AI generated a `.github/workflows/ci.yml` file that checks out the repository, sets up Python 3.11, installs dependencies from `requirements.txt`, and runs `python -m pytest`.

**My Decision**

I accepted this workflow because it directly matched the project requirement. After pushing to GitHub, I confirmed that the CI workflow passed and added the CI badge to the README.

## What I Learned

This project showed that AI is useful for generating structure, boilerplate code, tests, and documentation. However, AI still requires human review. I had to decide what behavior made sense for engineering data, fix formatting and GitHub setup issues, and verify the code through tests and CI.

The most important lesson is that AI can accelerate software development, but it should not replace engineering judgment.

