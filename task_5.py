load = [10, 50, 20, 80, 30, 90, 40, 60, 10, 20]
print("Исходная нагрузка:", load)

smoothed_load = []

for i in range(len(load) - 2):
    window = load[i:i+3]
    average = int(sum(window) / 3)
    smoothed_load.append(average)

print("Сглаженный тренд:", smoothed_load)