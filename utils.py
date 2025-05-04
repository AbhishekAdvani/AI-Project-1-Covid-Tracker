import pandas as pd
import matplotlib.pyplot as plt
import os

def download_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None

def filter_country_data(data, country):
    country_data = data[data['location'].str.lower() == country.lower()]
    if country_data.empty:
        return None

    # Select relevant columns
    country_data = country_data[['date', 'new_cases', 'total_cases']]
    country_data['date'] = pd.to_datetime(country_data['date'])
    return country_data

def plot_cases(df, country):
    import os

    # Ensure the visuals folder exists
    output_dir = "visuals"
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['new_cases'], label='New Daily Cases', color='orange')
    plt.plot(df['date'], df['total_cases'], label='Total Cases', color='red')

    plt.title(f'COVID-19 Case Trends in {country}')
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save plot to visuals folder
    output_path = os.path.join(output_dir, f"{country.lower().replace(' ', '_')}_cases.png")
    plt.savefig(output_path)
    print(f"✅ Plot saved to: {output_path}")

    plt.show()
