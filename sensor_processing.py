def calculate_average(values):
    return sum(values) / len(values)

data = [72, 55, 101, 90]
average = calculate_average(data)
print("Average:", average)

stations = [["A1", 62], ["B2", 97], ["C3", 85], ["D4", 110]]

for station in stations:
    print(station[0], "->", station[1])

def report_status(stations, threshold):
    for station in stations:
        status = "OK" if station[1] <= threshold else "ALERT"
        print(f"{station[0]}: PM2.5 = {station[1]} -> {status}")

report_status(stations, 100)
