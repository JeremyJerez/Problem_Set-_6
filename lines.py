# Python_Intro
# Problem Set 6
#A series of exercises for CS50 hands-on projects
"""
This one"s my approach to the "Lines of Code" problem
"""
import sys

if len(sys.argv) <= 1:
    print('Too few command-line arguments')
    sys.exit(1)
elif len(sys.argv) > 2:
    print('Too many commands-line arguments')
    sys.exit(1)
elif sys.argv[1].endswith('.py') == False:
    print('Not a Python file')
    sys.exit(1)
else:
    file_name = sys.argv[1]

count = 0
try:
    with open(file_name, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            else:
                state = line.strip()
                if not state.startswith('#'):
                    count += 1
except FileNotFoundError:
    print('File does not exist')
    sys.exit(1)

print(count)
