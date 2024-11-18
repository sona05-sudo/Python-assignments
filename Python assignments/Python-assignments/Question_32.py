"""Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""

def capitalize_lines():
    print("Enter lines of text (press 'Enter' twice to stop):")
    lines = []
    
    while True:
        line = input()
        if line == "":  # Stop if an empty line is entered
            break
        lines.append(line)

    # Capitalize each line and print
    for line in lines:
        print(line.upper())

# Call the function to execute the program
capitalize_lines()
