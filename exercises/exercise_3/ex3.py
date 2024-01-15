class Car:
    def __init__(self, brand, mass_kg, cross_sectional_area, velocity_kph):
        self.brand = brand
        self.mass_kg = mass_kg
        self.cross_sectional_area = cross_sectional_area
        self.velocity_kph = velocity_kph

    def __iter__(self):
        return self

    def __str__(self):
        return f"{self.brand}"

    def calculate_power_consumption(self, drag_coefficient, roll_resistant_coefficient):
        velocity_mps = (self.velocity_kph * 1000) / 3600
        F_drag = 0.5 * 1.2 * drag_coefficient * self.cross_sectional_area * (velocity_mps**2)
        F_rolling = roll_resistant_coefficient * self.mass_kg * 9.81 
        return (F_drag + F_rolling) * velocity_mps


if __name__ == "__main__":
    drag_coefficient = 0.31
    roll_resistant_coefficient = 0.015

    cars = {
        Car("Opel", 1500, 1.5, 60) : 0,
        Car("Mercedes", 1700, 1.8, 80) : 0,
        Car("VW", 1600, 1.6, 90) : 0
    }

    for car in cars.keys():
        cars[car] = car.calculate_power_consumption(drag_coefficient, roll_resistant_coefficient)


POWER_THRESHOLD = 10_000
for car, power_consumtion in cars.items():
    is_energy_efficient = "yes" if power_consumtion < POWER_THRESHOLD else "no"
    print(f"Vehicle: {car} | Power consumption: {power_consumtion:.2f} W | energy-efficient: {is_energy_efficient}")
