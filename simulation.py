import numpy as np
from config import initial_temperature, initial_sea_level, initial_precipitation, temperature_increase_per_year, sea_level_rise_per_year, precipitation_change_per_year, years

def simulate_climate_change():
    temperatures = np.zeros(years)
    sea_levels = np.zeros(years)
    precipitations = np.zeros(years)

    temperatures[0] = initial_temperature
    sea_levels[0] = initial_sea_level
    precipitations[0] = initial_precipitation

    for year in range(1, years):
        temperatures[year] += temperatures[year - 1] + temperature_increase_per_year
        sea_levels[year] += sea_levels[year - 1] + sea_level_rise_per_year
        precipitations[year] += precipitations[year - 1] + precipitation_change_per_year

    return years, temperatures, sea_levels, precipitations
