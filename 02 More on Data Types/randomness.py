import random

# print(random.choice(range(7)))
# print(random.choice("Sushant"))
# print(random.randrange(10))
#
# random.seed(11)
# print(random.random())

# list_nums = [1,2,3,4,5]
# random.shuffle(list_nums)
# print(list_nums)
#

dice_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

dice_number=random.choice(range(1,7))

if dice_number==1:
    dice_list[4]='.'
elif dice_number==2:
    dice_list[0] = '.'
    dice_list[8] = '.'
elif dice_number==3:
    dice_list[0] = '.'
    dice_list[4] = '.'
    dice_list[8] = '.'
elif dice_number==4:
    dice_list[0] = '.'
    dice_list[2] = '.'
    dice_list[6] = '.'
    dice_list[8] = '.'
elif dice_number==5:
    dice_list[0] = '.'
    dice_list[0] = '.'
    dice_list[2] = '.'
    dice_list[6] = '.'
    dice_list[8] = '.'
# elif dice_number==6:
else:
    dice_list[3] = '.'
    dice_list[5] = '.'
    dice_list[0] = '.'
    dice_list[2] = '.'
    dice_list[6] = '.'
    dice_list[8] = '.'

dice = f"""
{dice_list[0]} {dice_list[1]} {dice_list[2]} 
{dice_list[3]} {dice_list[4]} {dice_list[5]}
{dice_list[6]} {dice_list[7]} {dice_list[8]} 
"""

print(dice)
