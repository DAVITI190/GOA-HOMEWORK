def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
print(number([[10, 0], [3, 5], [5, 8]]))  