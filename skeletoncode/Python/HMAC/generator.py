import sys
from random import randint

while True:
    try:

        length = int(input("Please enter your length: "))
        filename = str(length)
    except EOFError as error:
        print(error)
        sys.exit()

    content = ""
    while length > 0:
        content += str(randint(0, 9))
        length -= 1

    with open(f"{filename}.txt", "w") as file:
        file.write(content)
