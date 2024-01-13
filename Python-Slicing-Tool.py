import re

def reverse_file(source_file, target_file):
    with open(source_file, "r") as original_file:
        original_lines = original_file.readlines()

    reversed_lines = reversed(original_lines)

    with open(target_file, "w") as reversed_file:
        reversed_file.writelines(reversed_lines)
        
def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

variableDependency = []
lines = []
lineNumber = []
excluded_vars = ["i", "j", "k"]
variables = ["arrivalTime", "burstTime", "startTime", "endTime", "waitTime", "turnaroundTime", "numProcess"]

sourceCode = "fifo.py"
targetFile = "reversedfifo.py"
reverse_file(sourceCode, targetFile)
line_count = count_lines(targetFile) + 1

print("\033[1;34mWelcome to our Static Variable Slicing Tool (Backwards Technique)! 🚀✨")
print("Here, we'll display variable dependencies and line numbers. Let's get started!🔥\033[0m")
print("\033[1;90mNote: This tool has some restrictions:\033[0m")
print("1. The code should be written in Python.")
print("2. Shorthand methods like 'i += 1' are not supported. Please use complete assignment statements.")
print("3. Unassigned variables are not supported, and any initialized variable must be assigned a value.")
print("4. Print statements are disregarded.")

print("\033[1;34mBelow is the list of variables 👇 :\033[0m")
for i, variable in enumerate(variables, start=1):
    print(f"{i}. {variable}")


choice = input("\033[1;34mEnter a one variable you'd like to slice from the List: \033[0m")

if choice in variables:
    variableDependency.append(choice)
else:
    print("\033[1;90m⚠️  The chosen variable is not in the list. Please select a variable from the available options next time.\033[0m") 
    exit(0)

for var in variableDependency:
    with open(targetFile, "r") as file:
            for j, line in enumerate(file, start=1):
                i = line_count - j
                if var in line:
                    if "=" in line and var in line.split('=')[0]:
                        lines.append(line)
                        lineNumber.append(i)

            for i, line in enumerate(lines):
                    delimiters = r"(?=[- + * / = ])" 
                    tokens = re.split(delimiters, line)
                    tokens = [token.rstrip('\n') for token in tokens if token.strip()]
                    for i, token in enumerate(tokens): 
                        if '=' == token:
                            var_part = tokens[i + 1].replace(" ", "")
                            if "." in var_part:
                                var_part = var_part.split(".")[1]
                            if var_part.isidentifier() and var_part not in variableDependency:
                                variableDependency.append(var_part)
                        
                        if token in "+-*/":
                            prev_token = tokens[i - 1]
                            if "." in prev_token:
                                prev_token = prev_token.split(".")[1]
                            next_token = tokens[i + 1]
                            if "." in next_token:
                                next_token = next_token.split(".")[1]
                            
                            if prev_token.isidentifier() and prev_token not in variableDependency:
                                variableDependency.append(prev_token)
                            if next_token.isidentifier() and next_token not in variableDependency:
                                variableDependency.append(next_token)

print("\033[1;34mVariable Dependencies:\033[0m")
print(variableDependency)
print("\033[1;34mLine Numbers:\033[0m")
print(lineNumber)

print("\033[1;35mHappy slicing! ✂️\033[0m")






