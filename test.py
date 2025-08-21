"""
Author: 4FTSQRL

Usage: test.py

Description: The test script for the guessing game for testing functionality of the game
"""

# Import statements

# Main function for testing
def main():
    # Call results
    print(results())
    return 0

# Answer function
def answer():
    # Stores the answer as such to call the function in different files
    answer = 203
    # Returns answer
    return answer

# Guess Function
def guesses():
    # Function for the guesses
    # Dictionary for it
    playerGuesses = {
        "John Doe": 0,
        "John Deer": 0,
        "Jane Doe": 0,
        "Joe Momma": 0
    }
    return playerGuesses

# Math Function
def results():
    # Calculates results
    # call the other functions
    playerGuesses = guesses()
    realnum = answer()
    
    # Store difference
    diff = [90000]
    i = 1
    # Store winner
    winner = ""
    print (playerGuesses.items())
    # For loop to loop through all playerGuess values to find the winnner
    for g in playerGuesses.items():
        diff.insert(i, abs(g[1] - realnum))
        if (diff[i] <= diff[i-1]):
            winner = g[0]
        # iterate i
        i += 1
        
    # Sort the difference
    diff.sort()
    
    return winner
# Python incantation
if __name__ == "__main__":
    main()