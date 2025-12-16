km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda feet: feet * 12
inches_to_cm = lambda inches: inches * 2.54


def distance_converter(distance, conversion_type, func):
    result = func(distance)
    print(f"{conversion_type}: {result}")


distance = float(input("Enter distance: "))

distance_converter(distance, "Kilometers to Meters", km_to_m)
distance_converter(distance, "Meters to Centimeters", m_to_cm)
distance_converter(distance, "Centimeters to Millimeters", cm_to_mm)
distance_converter(distance, "Feet to Inches", feet_to_inches)
distance_converter(distance, "Inches to Centimeters", inches_to_cm)
