from currentweather_data_fetcher import get_wind_spped

tickers = ["Quito,Ec", "Guayaquil,Ec", "Cuenca,Ec"]



for t in tickers:
    #quito#
    get_wind_spped(ticker=t, verbose=True)










