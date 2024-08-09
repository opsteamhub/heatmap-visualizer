import csv
import random

# Coordinates for populous cities worldwide
cities = {
    "Bangkok": "13.7563,100.5018",
    "Beijing": "39.9042,116.4074",
    "Belém": "-1.4550,-48.5024",
    "Berlin": "52.5200,13.4050",
    "Bogotá": "4.7110,-74.0721",
    "Brasília": "-15.8267,-47.9218",
    "Buenos Aires": "-34.6037,-58.3816",
    "Cairo": "30.0444,31.2357",
    "Campo Grande": "-20.4697,-54.6201",
    "Caracas": "10.4806,-66.9036",
    "Curitiba": "-25.4293,-49.2719",
    "Cuiabá": "-15.6014,-56.0979",
    "Delhi": "28.6139,77.2090",
    "Dhaka": "23.8103,90.4125",
    "Fortaleza": "-3.7172,-38.5434",
    "Goiânia": "-16.6869,-49.2648",
    "Ho Chi Minh City": "10.8231,106.6297",
    "Istanbul": "41.0082,28.9784",
    "Jakarta": "-6.2088,106.8456",
    "Karachi": "24.8607,67.0011",
    "Kolkata": "22.5726,88.3639",
    "Lagos": "6.5244,3.3792",
    "Lima": "12.0464,-77.0428",
    "London": "51.5074,-0.1278",
    "Los Angeles": "34.0522,-118.2437",
    "Manila": "14.5995,120.9842",
    "Manaus": "-3.1190,-60.0217",
    "Mexico City": "19.4326,-99.1332",
    "Montevideo": "-34.9011,-56.1645",
    "Moscow": "55.7558,37.6173",
    "Mumbai": "19.0760,72.8777",
    "New York": "40.7128,-74.0060",
    "Paris": "48.8566,2.3522",
    "Porto Alegre": "-30.0346,-51.2177",
    "Porto Velho": "-8.7612,-63.9039",
    "Quito": "-0.1807,-78.4678",
    "Recife": "-8.0476,-34.8770",
    "Rio de Janeiro": "-22.9068,-43.1729",
    "Rome": "41.9028,12.4964",
    "Salvador": "-12.9714,-38.5014",
    "Santiago": "-33.4489,-70.6693",
    "São Paulo": "-23.5505,-46.6333",
    "Seoul": "37.5665,126.9780",
    "Shanghai": "31.2304,121.4737",
    "Singapore": "1.3521,103.8198",
    "Tehran": "35.6892,51.3890",
    "Tokyo": "35.6895,139.6917"
    # Continue adding more cities...
}

# Define the group for each city
groups = {
    "Bangkok": "Asia",
    "Beijing": "Asia",
    "Belém": "South America",
    "Berlin": "Europe",
    "Bogotá": "South America",
    "Brasília": "South America",
    "Buenos Aires": "South America",
    "Cairo": "Africa",
    "Campo Grande": "South America",
    "Caracas": "South America",
    "Curitiba": "South America",
    "Cuiabá": "South America",
    "Delhi": "Asia",
    "Dhaka": "Asia",
    "Fortaleza": "South America",
    "Goiânia": "South America",
    "Ho Chi Minh City": "Asia",
    "Istanbul": "Europe",
    "Jakarta": "Asia",
    "Karachi": "Asia",
    "Kolkata": "Asia",
    "Lagos": "Africa",
    "Lima": "South America",
    "London": "Europe",
    "Los Angeles": "North America",
    "Manila": "Asia",
    "Manaus": "South America",
    "Mexico City": "North America",
    "Montevideo": "South America",
    "Moscow": "Europe",
    "Mumbai": "Asia",
    "New York": "North America",
    "Paris": "Europe",
    "Porto Alegre": "South America",
    "Porto Velho": "South America",
    "Quito": "South America",
    "Recife": "South America",
    "Rio de Janeiro": "South America",
    "Rome": "Europe",
    "Salvador": "South America",
    "Santiago": "South America",
    "São Paulo": "South America",
    "Seoul": "Asia",
    "Shanghai": "Asia",
    "Singapore": "Asia",
    "Tehran": "Asia",
    "Tokyo": "Asia"
    # Continue adding more groups...
}

# Function to generate samples of cities
def generate_samples(cities, min_samples=1, max_samples=50):
    data = []
    for city, coord in cities.items():
        group = groups[city]
        num_samples = random.randint(min_samples, max_samples)
        for _ in range(num_samples):
            # Format the output as specified
            data.append((group, f"({coord})"))
    return data

# Generate samples
data_samples = generate_samples(cities)

# Save the data to a CSV file
with open('sample-data.csv', 'w', newline='') as file:
    writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Group', 'Coordinates'])
    for item in data_samples:
        writer.writerow(item)

print("File 'sample-data.csv' generated successfully.")
