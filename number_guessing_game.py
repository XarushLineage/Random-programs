import random

def number_guessing_game():

    print("Welcome to the number guessing game!")
    
    # Prompt the user to enter the range of numbers to guess from
    minimum = 1
    while True:
        try:
            maximum = int(input("Enter the maximum number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Prompt the user to choose whether to play or watch the computer play
    player_choice = input("Would you like to play or watch the computer play? Enter 'p' to play or 'c' to watch the computer play: ")
    
    if player_choice == 'p':
        # The user wants to play
        print("You have chosen to play.")
    
        # Generate a random number within that range
        number = random.randint(minimum, maximum)
    
        # Set the number of attempts and the score
        attempts = 0
        score = 100
    
        # Prompt the user to guess the number
        while True:
            guess = int(input("Guess the number: "))
            attempts += 1
    
            # Check if the guess is correct
            if guess == number:
                print("Congratulations! You guessed the number in", attempts, "attempts. Your score is", score)
                break
    
            # If the guess is incorrect, provide feedback and reduce the score
            print("Wrong! Try again.")
            if guess < number:
                print("Hint: The number is higher.")
            else:
                print("Hint: The number is lower.")
            score -= 10
    
            # If the user runs out of attempts, end the game
            if score == 0:
                print("Game over. The number was", number)
                break
        
        # Ask the user if they want to play again    
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            number_guessing_game()    
    
    elif player_choice == 'c':
        # The user wants to watch the computer play
        print("You have chosen to watch the computer play.")
    
        # Generate a random number within that range
        number = random.randint(minimum, maximum)
    
        # Set the number of attempts and the score
        attempts = 0
        score = 100
    
        # Have the computer guess the number
        lower_bound = minimum
        upper_bound = maximum
        while True:
            # Use binary search to guess the number more efficiently
            guess = (lower_bound + upper_bound) // 2
            attempts += 1
    
            # Check if the guess is correct
            if guess == number:
                print("The computer's guess is", guess)
                print("The computer guessed the number in", attempts, "attempts. The score is", score)
                break
    
            # If the guess is incorrect, provide feedback and reduce the score
            print("The computer's guess is", guess)
            if guess < number:
                print("Hint: The number is higher.")
                lower_bound = guess + 1
            else:
                print("Hint: The number is lower.")
                upper_bound = guess - 1
            score -= 10
    
            # If the computer runs out of attempts, end the game
            if score == 0:
                print("Game over. The number was", number)
                break
        
        # Ask the user if they want to play again    
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            number_guessing_game()    
    
else:
        # The user entered an invalid choice
        print("Invalid choice. Please enter 'p' to play or 'c' to watch the computer play.")

#Initiate the game.
number_guessing_game()        
