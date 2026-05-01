# Reflection

In this final project, I used generative AI as a coding assistant to develop a small sensor data analysis tool. The project reads sensor data from a CSV file, validates required columns, calculates summary statistics, detects missing values and outliers, generates a markdown report, and creates a plot for quick inspection. My goal was not only to make the program work, but also to understand how AI can support an engineering coding workflow.

AI was most helpful during the early design stage. It helped me define a clear project scope, organize the repository structure, and separate the program into modules such as data loading, validation, analysis, report generation, and plotting. It also helped generate initial versions of the Python functions and pytest unit tests. This saved time and gave me a useful starting point.

However, I did not accept all AI suggestions blindly. For example, one possible approach was to automatically replace missing sensor values with zero. I rejected this idea because missing sensor values may indicate a real sensor or data collection problem. Silently filling them with zero could hide important engineering failures. Instead, I chose to report missing values explicitly.

I verified the AI-assisted code by running the program on a sample CSV file, checking the generated report and plot, and writing unit tests with pytest. I also added a GitHub Actions CI workflow so that the tests run automatically after pushing to GitHub. This helped prove that the repository can be tested reproducibly, not just on my own computer.

The biggest lesson I learned is that generative AI is powerful for accelerating coding, debugging, testing, and documentation, but it still requires human judgment. AI can suggest code, but the engineer must decide whether the logic is appropriate, whether edge cases are handled, and whether the final result is reliable.
