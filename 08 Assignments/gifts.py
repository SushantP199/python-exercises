# Approach important that direct output

c_sweater = 68
u_sweater = 3
c_game = 75
u_game = 1
c_bracelet = 43
u_bracelet = 2

refund_bracelete = 1
rebate_game = 10

total_cost = (c_sweater * u_sweater) + (c_game * u_game) + (c_bracelet * u_bracelet)
reducecost = (refund_bracelete * c_bracelet) + rebate_game

net_cost = total_cost - reducecost

print(f"Total cost of gifts is {net_cost}$")

""" O/P:
Total cost of gifts is 312$
"""
