import json
from pathlib import Path

class Car:
    power_consumption = 0
    def __init__(self, type, mass_kg, cross_sectional_area, velocity_kph, roll_resistant_coefficient, drag_coefficient):
        self.type = type
        self.mass_kg = mass_kg
        self.cross_sectional_area = cross_sectional_area
        self.velocity_kph = velocity_kph
        self.roll_resistant_coefficient = roll_resistant_coefficient
        self.drag_coefficient = drag_coefficient

    def __iter__(self):
        return self

    def __str__(self):
        return f"{self.type}"

    def calculate_power_consumption(self):
        velocity_mps = (self.velocity_kph * 1000) / 3600
        F_drag = 0.5 * 1.2 * self.drag_coefficient * self.cross_sectional_area * (velocity_mps**2)
        F_rolling = self.roll_resistant_coefficient * self.mass_kg * 9.81 
        return (F_drag + F_rolling) * velocity_mps


if __name__ == "__main__":
    root_dir = Path(__file__).parent
    for filepath in root_dir.glob("*.json"):
        with open(filepath, 'r') as file:
            data = json.load(file)
            cars = []
            for i in range(0, len(data)):
                cars.append(Car(data[i]['type'], 
                                data[i]['mass'], 
                                data[i]['cross_sectional_area'], 
                                100, 
                                data[i]['rolling_resistance_coefficient'], 
                                data[i]['drag_coefficient']))

            POWER_THRESHOLD = 10_000
            for car in cars:
                is_energy_efficient = "yes" if car.calculate_power_consumption() < POWER_THRESHOLD else "no"
                print(f"Vehicle: {car} | Power consumption: {car.calculate_power_consumption():.2f} W | energy-efficient: {is_energy_efficient}")
