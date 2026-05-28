import pandas as pd

def transform_weather_data(data):

    hourly_data = data.get("hourly", {})

    df = pd.DataFrame({
        "time": hourly_data.get("time", []),
        "temperature": hourly_data.get("temperature_2m", []),
        "humidity": hourly_data.get("relative_humidity_2m", [])
    })

    # Derived field
    df["weather_condition"] = df["temperature"].apply(
        lambda x: "Hot" if x > 30 else "Normal"
    )

    return df