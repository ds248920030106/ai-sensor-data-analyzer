import argparse

from src.data_loader import load_sensor_data
from src.validator import validate_required_columns
from src.analyzer import analyze_sensor_data
from src.report_generator import generate_markdown_report
from src.plotter import plot_sensor_data


def main() -> None:
    parser = argparse.ArgumentParser(
        description="AI-assisted sensor data analyzer"
    )

    parser.add_argument(
        "input_file",
        help="Path to the input sensor CSV file"
    )

    parser.add_argument(
        "--report",
        default="outputs/summary_report.md",
        help="Path to save the markdown report"
    )

    parser.add_argument(
        "--plot",
        default="outputs/sensor_plot.png",
        help="Path to save the sensor plot"
    )

    args = parser.parse_args()

    df = load_sensor_data(args.input_file)
    validate_required_columns(df)

    analysis_result = analyze_sensor_data(df)

    generate_markdown_report(analysis_result, args.report)
    plot_sensor_data(df, args.plot)

    print("Sensor Data Analysis Complete.")
    print(f"Rows analyzed: {analysis_result['row_count']}")
    print(f"Report saved to: {args.report}")
    print(f"Plot saved to: {args.plot}")


if __name__ == "__main__":
    main()