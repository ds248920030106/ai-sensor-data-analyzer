from pathlib import Path
import pandas as pd


def load_sensor_data(file_path: str) -> pd.DataFrame:
    """
    Load sensor data from a CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A pandas DataFrame containing sensor data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or cannot be parsed.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError as exc:
        raise ValueError("Input CSV file is empty.") from exc
    except pd.errors.ParserError as exc:
        raise ValueError("Input CSV file cannot be parsed.") from exc

    if df.empty:
        raise ValueError("Input CSV file contains no data rows.")

    return df