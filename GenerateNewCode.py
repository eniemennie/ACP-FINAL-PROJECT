import random  # Import the random module to generate random numbers

def random_id():
    # Generates a random 8-digit number
    return random.randint(10000000, 99999999)  # Return a random integer between 10,000,000 and 99,999,999

# Example usage
print(random_id())  # Print a randomly generated 8-digit number to the console