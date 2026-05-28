from fetch_weather import fetch_weather_data
from transform import transform_weather_data

def main():

    raw_data = fetch_weather_data()

    if raw_data:

        transformed_df = transform_weather_data(raw_data)

        print(transformed_df.head())

    else:
        print("Failed to fetch weather data")


if __name__ == "__main__":
    main()
    
    