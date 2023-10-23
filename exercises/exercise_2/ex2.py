import numpy as np

drag_coeff = 0.31
rr_coeff = 0.015 
g = 9.81 # m / s^2 

cars = {
    "Bobbycar" : 0,
    "Traktor" : 0,
    "Bagger" : 0,
    "LKW" : 0
}

for car in cars.keys():
    mass_kg = np.random.randint(1000, 5000)
    cs_area = np.random.randint(1.8, 3.5)
    velocity_kph = (np.random.randint(30, 100) * 1000) / 3600 # m / s

    F_drag = 0.5 * 1.2 * drag_coeff * cs_area * (velocity_kph ** 2)
    F_rolling = rr_coeff * mass_kg * g
    power = (F_drag + F_rolling) * velocity_kph

    cars[car] = power

POWER_THRESHOLD = 10000
for car, power_consumtion in cars.items():
    is_energy_efficient = "yes" if power_consumtion < POWER_THRESHOLD else "no"
    print(f"Vehicle: {car} | Power consumption: {power_consumtion:.2f} W | energy-efficient: {is_energy_efficient}")


