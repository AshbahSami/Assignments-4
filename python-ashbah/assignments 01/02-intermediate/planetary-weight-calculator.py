print("*****Welcome to planetary weight calculator*****")
planets={
    'Mercury':0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

earth_weight=float(input("Enter your Earth weight: "))
planet=input("Enter planet name: ")

planetary_weight=earth_weight*planets[planet1]
rounded_weight = round(planetary_weight, 2)
print(f"The equivalent weight on {planet}: {rounded_weight}")