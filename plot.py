def plot_data(data):
    """Plot the data we received from the meteo API request"""
    # time = data.get('hourly', {}).get('time')
    temperature = data.get('hourly', {}).get('temperature_2m')

    # x=time[:24] not needed actually
    y = temperature[:24]

    x = list(range(0, 24))

    plt.plot(x, y)

    plt.xlabel("Hour")
    plt.ylabel("Temperature")

    plt.xticks(x)
    plt.yticks(np.arange(int(min(y)), int(max(y)) + 1, 1.0))

    plt.show()