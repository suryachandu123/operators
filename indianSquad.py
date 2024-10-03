'''
It were the days of domination from the traditional metros in the team selections and everytime the team is announced for the Indian Squad, mere disappointment was left with this small town player. Dhoni’ill fate continued even during the team selections for the India A squad to tour to Zimbabwe.3 new players from Mumbai were on the list for the Indian team and it was claimed by the selectors that Dhoni was a bit younger than the 3 selected players.
  Assume the 3 players are Named X,Y and Z. The ages of the players X and Y are the same and the age of the Z is 10 more than other 2 players. Given the total age of the 3 players, find the age of the 3 players.
Input format:
First line of the input is an integer that corresponds to the total age of the 3 players.
Output format:
Output should display the ages of the three players in 3 lines. The age of the eldest player should be displayed in the last line.
Sample input and output 1:
70
20
20
30
Sample input and output 2:
100
30
30
40
'''
# Function to find the ages of the players
def find_player_ages(total_age):
    # Let age of players X and Y be a
    # Age of player Z will then be a + 10
    # The equation becomes: 2a + (a + 10) = total_age
    # Simplifying: 3a + 10 = total_age
    # Therefore, a = (total_age - 10) / 3
    a = (total_age - 10) / 3
    x_age = int(a)   # Age of player X
    y_age = int(a)   # Age of player Y
    z_age = x_age + 10  # Age of player Z
    return x_age, y_age, z_age

# Input: Total age of the three players
total_age = int(input())

# Calculate ages
x_age, y_age, z_age = find_player_ages(total_age)

# Output the ages
print(x_age)
print(y_age)
print(z_age)
