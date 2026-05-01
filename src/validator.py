REQUIRED_COLUMNS = [
    "timestamp",
    "temperature",
    "humidity",
    "pressure",
    "accel_x",
    "accel_y",
    "accel_z",
]


def validate_required_columns(df) -> None:
    """
    Validate that the DataFrame contains all required sensor columns.

    Args:
        df: Input pandas DataFrame.

    Raises:
        ValueError: If one or more required columns are missing.
    """
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")