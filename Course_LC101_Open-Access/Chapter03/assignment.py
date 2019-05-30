"""
You have a thermostat that allows you to set the room to any temperature between 40 and 89 degrees.

The thermostat can be adjusted by turning a circular dial. For instance, if the temperature is set to 
50 degrees and you turn the dial 10 clicks toward the left, you will set the temperature to 40 degrees. 
But if you keep turning 1 click to the left (represented as -1) it will circle back around to 89 degrees. 
If you are at 40 degrees and turn to the right by one click, you will get 41 degrees. As you continue to 
turn to the right, the temperature goes up, and the temperature gets closer and closer to 89 degrees. 
But as soon as you complete one full rotation (50 clicks), the temperature cycles back around to 40 degrees.

Write a program that calculates the temperature based on how much the dial has been turned. The number of 
clicks (from the starting point of 40 degrees) is contained in a variable. You should print the current 
temperature for each given click variable so that your output is as follows:
"""

#Starter Code
"""
#For each click variable, calculate the temperature and print it as shown in the instructions

click_1 = 0
# TODO calculate the temperature, and report it back to the user

click_2 = 49
# TODO calculate the temperature, and report it back to the user

click_3 = 74
# TODO calculate the temperature, and report it back to the user

click_4 = 51
# TODO calculate the temperature, and report it back to the user

click_5 = -1
# TODO calculate the temperature, and report it back to the user

click_6 = 200
# TODO calculate the temperature, and report it back to the user
"""

#For each click variable, calculate the temperature and print it as shown in the instructions
starting_temperature = 40

# TODO calculate the temperature, and report it back to the user
click_1 = 0
click_1_deflection = click_1 % 50
final_temperature = starting_temperature + click_1_deflection

#print(click_1_deflection)
print("The temperature is",final_temperature)

# TODO calculate the temperature, and report it back to the user
click_2 = 49
click_2_deflection = click_2 % 50
final_temperature = starting_temperature + click_2_deflection

#print(click_2_deflection)
print("The temperature is",final_temperature)

# TODO calculate the temperature, and report it back to the user
click_3 = 74
click_3_deflection = click_3 % 50
final_temperature = starting_temperature + click_3_deflection

#print(click_3_deflection)
print("The temperature is",final_temperature)

# TODO calculate the temperature, and report it back to the user
click_4 = 51
click_4_deflection = click_4 % 50
final_temperature = starting_temperature + click_4_deflection

#print(click_4_deflection)
print("The temperature is",final_temperature)

# TODO calculate the temperature, and report it back to the user
click_5 = -1
click_5_deflection = click_5 % 50
final_temperature = starting_temperature + click_5_deflection

#print(click_5_deflection)
print("The temperature is",final_temperature)

# TODO calculate the temperature, and report it back to the user
click_6 = 200
click_6_deflection = click_6 % 50
final_temperature = starting_temperature + click_6_deflection

#print(click_6_deflection)
print("The temperature is",final_temperature)