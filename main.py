from apicall import open_meteo
from plot import plot_data

if __name__ == "__main__":
    # get input data
    lat = input("Enter latitude")
    lon = input("Enter longitude")

    # create the meteo request with the input data
    meteo_data = open_meteo(latitude=lat, longitude=lon)

    plot_data(meteo_data)
    