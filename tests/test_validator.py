import pandas as pd
import pytest

from src.validator import validate_required_columns


def test_valid_columns_pass():
    df = pd.DataFrame(
        {
            "timestamp": ["2026-05-01 12:00:00"],
            "temperature": [23.5],
            "humidity": [45.2],
            "pressure": [101.3],
            "accel_x": [0.01],
            "accel_y": [0.02],
            "accel_z": [9.80],
        }
    )

    validate_required_columns(df)


def test_missing_columns_raise_error():
    df = pd.DataFrame(
        {
            "timestamp": ["2026-05-01 12:00:00"],
            "temperature": [23.5],
        }
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_required_columns(df)