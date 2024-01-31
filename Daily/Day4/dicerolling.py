import random

response = input ("what do you want to roll: ")
while response != "done":
    #do Dice
    nums = response.split("d")
    dice_count = int(nums[0])
    dice_type = int(nums[1])

    result = 0
    for i in range(dice_count):
        result += random.randint(1, dice_type)
    print("You got a", result)
    response = input("gimme another: ")
