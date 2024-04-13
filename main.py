# main.py
# Entry point for the Climate Change Impact Simulator

from simulation import simulate_climate_change
from visualization import plot_results

def main():
    years, temperatures, sea_levels, precipitations = simulate_climate_change()
    plot_results(years, temperatures, sea_levels, precipitations)

if __name__ == '__main__':
    main()
