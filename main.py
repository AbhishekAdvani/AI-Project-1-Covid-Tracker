from utils import download_data, filter_country_data, plot_cases

def main():
    # Download COVID-19 dataset
    data = download_data()

    # Ask user for a country
    country = "united states"

    # Filter country data
    country_data = filter_country_data(data, country)

    if country_data is not None:
        # Plot cases
        plot_cases(country_data, country)
    else:
        print(f"No data found for {country}. Please check the spelling.")

if __name__ == "__main__":
    main()
