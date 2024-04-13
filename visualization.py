import matplotlib.pyplot as plt

def plot_results(years, temperatures, sea_levels, precipitations):
    plt.figure(figsize=(10, 8))

    plt.subplot(311)
    plt.plot(range(years), temperatures, label='Temperature')
    plt.title('Climate Change Simulation Over 100 Years')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plt.subplot(312)
    plt.plot(range(years), sea_levels, label='Sea Level', color='green')
    plt.ylabel('Sea Level Change (mm)')
    plt.legend()

    plt.subplot(313)
    plt.plot(range(years), precipitations, label='Precipitation', color='blue')
    plt.xlabel('Years')
    plt.ylabel('Precipitation Change (mm)')
    plt.legend()

    plt.tight_layout()
    plt.show()
