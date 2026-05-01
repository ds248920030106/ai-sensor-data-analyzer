from pathlib import Path
import matplotlib.pyplot as plt


def plot_sensor_data(df, output_path: str) -> None:
    """
    Plot sensor readings over time and save the figure.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    sensor_columns = [
        "temperature",
        "humidity",
        "pressure",
        "accel_x",
        "accel_y",
        "accel_z",
    ]

    plt.figure(figsize=(10, 6))

    for col in sensor_columns:
        plt.plot(df.index, df[col], label=col)

    plt.xlabel("Sample Index")
    plt.ylabel("Sensor Value")
    plt.title("Sensor Readings Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()