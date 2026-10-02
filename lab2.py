import math

# Task 1
print("Завдання 1:")
step = 0.05
start = 0.3
end = 0.9
x = start
while x <= 0.9:
    result = 0
    if x <= 0.4:
        try:
            result = math.log(math.log10(x) + math.log(x, 3))
        except ValueError:
            result = "Помилка (від'ємне число під логарифмом)"
    elif x > 0.4 and x < 0.6:
        result = math.cos(math.sin(x**2))
    else:
        result = math.pow((x**3 + 0.5), 1 / 7)
    x += step
    print(f"{x:.2f} (x): {result}")

# Task 2
print("\nЗавдання 2:")
start = 0.0
end = 0.5
step = 0.05
mistake = 0.001

x = start
while x <= end + 1e-9:
    n = 1
    term = x
    series_sum = 0.0
    
    while abs(term) >= mistake:
        series_sum += term
        n += 1
        term = ((-1) ** (n + 1)) * (x ** n) / n

    print(f"{x:.2f} (x): Сума ряду = {series_sum:.6f}; Кількість доданків (n) = {n - 1}")
    x += step