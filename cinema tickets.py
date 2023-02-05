amt = int(input("Введите количество билетов:"))
ages = []

for i in range(0, amt):
    input_value = int(input(f"Введите возраст {i+1} посетителя:"))
    ages.append(input_value)

def amt_prise(ages):
    if ages < 18:
        return 0
    elif 18 <= ages < 25:
        return 990
    elif 25 <= ages:
        return 1390

total_ = sum(map(amt_prise, ages))

disc_perc = 0.1

disc = int(total_ * disc_perc)

disc_prise = int(total_ - disc)

if amt > 3:
    print("Полная стоимость билетов: ", total_, "руб.");
    print("Сумма скидки за более, чем 3 посетителя: ", disc, "руб.");
    print("Итоговая цена (с учётом скидки): ", disc_prise, "руб.");
else:
    print("Общая стоимость:", total_, "руб.");
