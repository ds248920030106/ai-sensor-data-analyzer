import pandas as pd

from src.analyzer import (
    analyze_sensor_data,
    calculate_summary_statistics,
    count_missing_values,
    detect_outliers,
)


def sample_dataframe():
    return pd.DataFrame(
        {
            "timestamp": [
                "2026-05-01 12:00:00",
                "2026-05-01 12:00:01",
                "2026-05-01 12:00:02",
            ],
            "temperature": [20.0, 22.0, 24.0],
            "humidity": [40.0, None, 44.0],
            "pressure": [101.0, 101.2, 101.4],
            "accel_x": [0.01, 0.02, 0.03],
            "accel_y": [0.01, 0.01, 0.02],
            "accel_z": [9.79, 9.80, 9.81],
        }
    )


def test_count_missing_values():
    df = sample_dataframe()
    result = count_missing_values(df)

    assert result["humidity"] == 1
    assert result["temperature"] == 0


def test_calculate_summary_statistics():
    df = sample_dataframe()
    result = calculate_summary_statistics(df)

    assert result["temperature"]["mean"] == 22.0
    assert result["temperature"]["min"] == 20.0
    assert result["temperature"]["max"] == 24.0


def test_detect_outliers_returns_counts():
    df = sample_dataframe()
    result = detect_outliers(df)

    assert isinstance(result, dict)
    assert "temperature" in result


def test_analyze_sensor_data_combines_results():
    df = sample_dataframe()
    result = analyze_sensor_data(df)

    assert result["row_count"] == 3
    assert "missing_values" in result
    assert "summary_statistics" in result
    assert "outliers" in result