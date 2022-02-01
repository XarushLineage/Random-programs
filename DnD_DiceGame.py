# Needed to create random numbers to simulate dice roll
import random

# Initialise variables to 0
number_of_tries = 0
highest_dice = 0
took_tries = 0

print('Enter an aproximate number of tries:')
x = input()

# Repeat everything in this block x number of times
for i in range(int(x)): #convert string to integer.


    # Generate first dice 
    dice_value = random.randint(1, 4)
    
  
    # Selection: based on comparison of the values, take the appropriate path through the code.
    if dice_value >= 4:
        
        number_of_tries = number_of_tries + 1   # This is how we increment a variable
        if dice_value > highest_dice:           # If the current dice is larger then the highest recorded value then update variable.
            highest_dice = 4
            took_tries = number_of_tries        #record the number of tries it took to get here.
        
        dice_value = random.randint(1, 6)       #Generate next dice.
        
        if dice_value >= 6:
            number_of_tries = number_of_tries + 1  
            if dice_value > highest_dice:
                highest_dice = 6
                took_tries = number_of_tries
                
            dice_value = random.randint(1, 8)    
            
            if dice_value >= 8:
                number_of_tries = number_of_tries + 1  
                if dice_value > highest_dice:
                    highest_dice = 9
                    took_tries = number_of_tries
                    
                dice_value = random.randint(1, 10)        
            
                if dice_value >= 10:
                    number_of_tries = number_of_tries + 1  
                    if dice_value > highest_dice:
                        highest_dice = 10
                        took_tries = number_of_tries
                        
                    dice_value = random.randint(1, 12)        
                    
                    if dice_value >= 12:
                        number_of_tries = number_of_tries + 1  
                        if dice_value > highest_dice:
                            highest_dice = 12
                            took_tries = number_of_tries
                            
                        dice_value = random.randint(1, 20)        
                        
                        if dice_value >= 20:
                            number_of_tries = number_of_tries + 1  
                            highest_dice = 20
                            took_tries = number_of_tries
                            print("Game won")
                            break
    
    
    number_of_tries = number_of_tries + 1    #update outside the loop for if statement fail.
        

    

print("### Game Over ###")
print("Number of tries:" ,number_of_tries)
print("The highest dice was:" ,highest_dice)
print("It took" ,took_tries ,"tries to get it.")
print("There were:",number_of_tries - took_tries ,"tries after without a higher dice.")
