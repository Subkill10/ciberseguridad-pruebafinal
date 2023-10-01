import requests

def get_wind_spped(ticker: str, verbose: bool = False) -> dict:
    url = f"https://openweathermap.org/data/2.5/onecall?lat=-0.2299&lon=-78.5249&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02"

    user_agent = {'user-agent': 'Mozila/5.0'}
    r = requests.get(url).json()

    wind_speed = r['current']['wind_speed']
    sunrise = r['current']['sunrise']
    if verbose:
     print(f"{ticker}: {wind_speed} {sunrise}")
    return {
        "ticker": ticker,
        "wind_speed": wind_speed,
        "sunrise": sunrise
    }
