from fetch_weather import fetch_weather_data
from transform import transform_weather_data
from bigquery_loader import load_to_bigquery


def main():

    raw_data = fetch_weather_data()

    if raw_data:

        transformed_df = transform_weather_data(raw_data)

        print(transformed_df.head())

        load_to_bigquery(transformed_df)

    else:
        print("Failed to fetch weather data")


if __name__ == "__main__":
    main()