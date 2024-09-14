import random

# Initialize overall statistics
total_games_won = 0
highest_dice_counts = {}
total_tries_for_wins = 0

# Get user inputs
cycles = int(input('Enter the number of cycles to run: '))
tries_per_cycle = int(input('Enter the number of tries per cycle: '))

dice_sides = [4, 6, 8, 10, 12, 20]

for cycle in range(1, cycles + 1):
    number_of_tries = 0
    highest_dice = 0
    took_tries = 0
    game_won = False

    for _ in range(tries_per_cycle):
        level = 0
        while level < len(dice_sides):
            sides = dice_sides[level]
            dice_value = random.randint(1, sides)
            number_of_tries += 1

            if dice_value == sides:
                if sides > highest_dice:
                    highest_dice = sides
                    took_tries = number_of_tries
                level += 1
                if level == len(dice_sides):
                    print(f"Cycle {cycle}: Game won!")
                    total_games_won += 1
                    total_tries_for_wins += number_of_tries
                    game_won = True
                    break
            else:
                break  # Stop the current attempt if the maximum isn't rolled

        if game_won:
            break  # Exit the loop if the game is won

    # Record highest dice counts
    highest_dice_counts[highest_dice] = highest_dice_counts.get(highest_dice, 0) + 1

    # Optionally, print per-cycle results
    print(f"### Cycle {cycle} Over ###")
    print("Number of tries:", number_of_tries)
    print("The highest dice reached:", highest_dice)
    print("It took", took_tries, "tries to reach it.")
    print("There were", number_of_tries - took_tries, "tries after without a higher dice.\n")

# After all cycles, print the report
print("\n### Overall Report ###")
print("Total cycles run:", cycles)
print("Total games won:", total_games_won)
print("\nHighest dice counts:")
for dice in sorted(highest_dice_counts.keys()):
    print(f"Dice {dice}: {highest_dice_counts[dice]} time(s)")

if total_games_won > 0:
    average_tries_for_wins = total_tries_for_wins / total_games_won
    print(f"\nAverage number of tries to win a game: {average_tries_for_wins:.2f}")
else:
    print("\nNo games were won.")
