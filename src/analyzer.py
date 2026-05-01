import pandas as pd


SENSOR_COLUMNS = [
    "temperature",
    "humidity",
    "pressure",
    "accel_x",
    "accel_y",
    "accel_z",
]


def count_missing_values(df: pd.DataFrame) -> dict:
    """
    Count missing values for each sensor column.
    """
    return df[SENSOR_COLUMNS].isna().sum().to_dict()


def calculate_summary_statistics(df: pd.DataFrame) -> dict:
    """
    Calculate basic summary statistics for each sensor column.
    """
    stats = {}

    for col in SENSOR_COLUMNS:
        stats[col] = {
            "mean": round(df[col].mean(), 3),
            "min": round(df[col].min(), 3),
            "max": round(df[col].max(), 3),
            "std": round(df[col].std(), 3),
        }

    return stats


def detect_outliers(df: pd.DataFrame, threshold: float = 3.0) -> dict:
    """
    Detect outliers using the mean ± threshold * standard deviation rule.

    Args:
        df: Input pandas DataFrame.
        threshold: Number of standard deviations used as the outlier boundary.

    Returns:
        A dictionary mapping each sensor column to the number of outliers.
    """
    outliers = {}

    for col in SENSOR_COLUMNS:
        series = df[col].dropna()
        mean = series.mean()
        std = series.std()

        if std == 0 or pd.isna(std):
            outliers[col] = 0
            continue

        lower_bound = mean - threshold * std
        upper_bound = mean + threshold * std

        count = ((series < lower_bound) | (series > upper_bound)).sum()
        outliers[col] = int(count)

    return outliers


def analyze_sensor_data(df: pd.DataFrame) -> dict:
    """
    Run all analysis steps and return a combined result dictionary.
    """
    return {
        "row_count": len(df),
        "missing_values": count_missing_values(df),
        "summary_statistics": calculate_summary_statistics(df),
        "outliers": detect_outliers(df),
    }