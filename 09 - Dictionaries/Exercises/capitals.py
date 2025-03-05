country_names = input().split(", ")
country_capitals = input().split(", ")

# print(dict(zip(country_names, country_capitals)))

merged = {country: capital for country, capital in zip(country_names, country_capitals) }

for country, capital in merged.items():
    print(f"{country} -> {capital}")