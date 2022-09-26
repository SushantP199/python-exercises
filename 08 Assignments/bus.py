def bus_carry_year(total,days):
    if days > 0:
        total += 1200000
        days -= 1
        return bus_carry_year(total,days)
    else:
        return print("Bus carries "+str(total)+" peoples each year")

bus_carry_year(0,365)

""" O/P:
Bus carries 438000000 peoples each year
"""

# tag line
""" SOMETIMES RECURSION CAN BE USED INSTEAD OF LOOPS """

