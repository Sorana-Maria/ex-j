def open_meteo(latitude, longitude):
    """Create the meteo API request and return it if we have successful status code"""
    try:
        # useless variables but we need to check if we can convert the values to float
        lat = float(latitude)
        lon = float(longitude)
    except ValueError as e:
        print(f"Please provide float inputs for latitude and longitude. (inputs: {latitude} | {longitude})")

        return None

    meteo_url = f"https://api.open-meteo.com/v1/forecast?latitude={str(latitude)}&longitude={str(longitude)}&hourly=temperature_2m"
    response = requests.get(meteo_url)

    if response.status_code == 200:
        print("Successful connection to meteo API.")
        print('-------------------------------')
        data = response.json()

        return data
    else:
        print("Unable to create the API request!")

        return None