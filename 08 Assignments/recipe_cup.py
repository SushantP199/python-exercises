cup5, cup3 = 0, 0
cap5, cap3 = 500, 300
print(f"We have two cups \n1) cup5 with capacity of {cap5}ml \n2) cup3 with capacity of {cap3}ml")
cup5 = cap5
print(f"\nNow cup5 is filled with {cup5}ml water....")
cup5 = cup5 - cap3
cup3 = cup3 + cap3
print("\nNow 300ml water from cup5 is poured in cup3....") 
print(f"\ncup5 contains remaining exactly {cup5}ml water which can be used for recipe")

""" O/P :
We have two cups 
1) cup5 with capacity of 500ml 
2) cup3 with capacity of 300ml

Now cup5 is filled with 500ml water....

Now 300ml water from cup5 is poured in cup3....

cup5 contains remaining exactly 200ml water which can be used for recipe
"""


""" LCO : 
cup5 = 500
cup3 = 300
req_water = cup5 - cup3
print(req_water)
"""
