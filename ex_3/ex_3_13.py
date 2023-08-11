day, month, year = [int(x) for x in input(
    "Ingrese una nueva fecha dd/mm/aaaa: ").split("/")]
ok = True

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day < 1 or day > 31:
        ok = False
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day < 1 or day > 30:
        ok = False
elif month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        if day < 1 or day > 29:
            ok = False
    else:
        if day < 1 or day > 28:
            ok = False
else:
    ok = False

print("(" + str(day) + "/" + str(month) + "/" + str(year) + ") Fecha", end=" ")

if (ok):
    print("valida")
else:
    print("invalida")
