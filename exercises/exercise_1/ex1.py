v = (80 * 1000) / 3600 # m / s^2
m = 1500 # kg
drag_coeff = 0.31
cs_area = 1.97 # m^2
rr_coeff = 0.015 
g = 9.81 # m / s^2 

F_drag = 0.5 * 1.2 * drag_coeff * cs_area * (v**2)
F_rolling = rr_coeff * m * g

power = (F_drag + F_rolling) * v
print(f"Power comsuption is: {round(power, 2)} W")