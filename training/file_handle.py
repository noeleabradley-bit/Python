from pathlib import Path
#Connects to 'data/my_file.txt' relative to the script

# open
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
 
print("Welcome to File Handle")
print("Opening file test.txt")

file_path = Path("data") / "test.txt"
f = open(file_path, "r")
print(f.read())
f.close

