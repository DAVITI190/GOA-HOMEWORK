def can_reach_pump(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

print(can_reach_pump(50, 25, 2))  # ➞ True (25 * 2 = 50)
print(can_reach_pump(60, 25, 2))  # ➞ False (25 * 2 = 50 < 60)
