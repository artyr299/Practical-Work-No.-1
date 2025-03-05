import math

a = float(input("Введіть a (a ≠ 0): "))
b = float(input("Введіть b: "))

if a == 0:
    print("Помилка: a не може дорівнювати 0.")
else:
    result = a * b + 5
    if result < 0:
        print("Рівняння не має дійсних коренів")
    else:
        x1 = math.sqrt(result)
        x2 = -math.sqrt(result)
        print(f"x1 = {x1}, x2 = {x2}")
