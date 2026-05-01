from pathlib import Path


def generate_markdown_report(analysis_result: dict, output_path: str) -> None:
    """
    Generate a markdown summary report from analysis results.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = []

    lines.append("# Sensor Data Summary Report\n")
    lines.append("## Dataset Overview\n")
    lines.append(f"- Total rows analyzed: {analysis_result['row_count']}\n")

    lines.append("## Missing Values\n")
    for sensor, count in analysis_result["missing_values"].items():
        lines.append(f"- {sensor}: {count}\n")

    lines.append("## Summary Statistics\n")
    for sensor, stats in analysis_result["summary_statistics"].items():
        lines.append(f"### {sensor}\n")
        lines.append(f"- Mean: {stats['mean']}\n")
        lines.append(f"- Min: {stats['min']}\n")
        lines.append(f"- Max: {stats['max']}\n")
        lines.append(f"- Standard deviation: {stats['std']}\n")

    lines.append("## Outlier Detection\n")
    lines.append("Outliers are detected using the mean ± 3 standard deviations rule.\n")
    for sensor, count in analysis_result["outliers"].items():
        lines.append(f"- {sensor}: {count}\n")

    path.write_text("\n".join(lines), encoding="utf-8")