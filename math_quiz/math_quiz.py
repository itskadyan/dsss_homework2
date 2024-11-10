import random

# Function to generate a random integer within a given range
def function_A(min, max):
    """
    Returns a random integer between min and max (inclusive).
    """
    return random.randint(min, max)

# Function to randomly select a mathematical operator
def function_B():
    '''
    Returns a random operator from the list of supported operations.
    '''
    return random.choice(['+', '-', '*'])

# Function to create a math problem and compute the answer
def function_C(n1, n2, o):
    # Format the problem as a string, e.g., "3 + 4"
    p = f"{n1} {o} {n2}"
    
    # Calculate the result based on the chosen operator
    if o == '+': 
        a = n1 + n2
    elif o == '-': 
        a = n1 - n2
    else: 
        a = n1 * n2
    
    # Return both the problem string and the answer
    return p, a

# Main function to run the math quiz game
def math_quiz():
    s = 0  # Initialize score counter
    t_q = 5  # Total number of questions in the quiz

    # Display game introduction
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through each question in the quiz
    for _ in range(t_q):
        # Generate two random numbers and a random operator for the problem
        n1 = function_A(1, 10)
        n2 = function_A(1, 10)
        o = function_B()

        # Create the math problem and calculate the correct answer
        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        
        # Get the user's answer and convert it to an integer
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Skip to the next question if input is invalid

        # Check if the user's answer matches the correct answer
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1  # Increment score if the answer is correct
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # Display the final score after the quiz is over
    print(f"\nGame over! Your score is: {s}/{t_q}")

# Run the math quiz game if the script is executed directly
if __name__ == "__main__":
    math_quiz()
