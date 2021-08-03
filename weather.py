

def get_temperature_by_city(city: str = "Provo"):
    temperature = "unknown!"
    # make sure text casing matches what is stored in dictionary
    city = city.lower()
    # verify that the dictionary contains the city
    if city in temperature_data:
        # change default for easier debugging
        temperature = temperature_data.get(city, 1000)
        return temperature

    return temperature
    

def convert_fahrenheit_to_celsius(ftemp):
    return round((ftemp - 32) / 1.8)


temperature_data = {
    "provo": 72,
    "orem": 78,
    "lindon": 66,
    "pleasant grove": 80
}