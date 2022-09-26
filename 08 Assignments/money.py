kara_per_glass = 5
rani_per_glass = 7

k = int(input("Enter nio of glasses sold by kara : "))
r = int(input("Enter no of glasses sold by rani : "))

total_money_kara = kara_per_glass * k
total_money_rani = rani_per_glass * r

if total_money_kara == total_money_rani:
    print("\nKara and Rani makes same money")
elif total_money_kara > total_money_rani:
    difference = total_money_kara - total_money_rani
    print(f"\nKara makes most money by {difference} cents")
else:
    difference = total_money_rani - total_money_kara
    print(f"\nRani makes most money by {difference} cents")
