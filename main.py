import re
import os

# reserves the arrays for the fret/string representation
e1String: list = []
a1String: list = []
d1String: list = []
g1String: list = []
b1String: list = []
e2String: list = []

def listToStr(a: list):
    return "".join(a)

# extract the frets from input
# userInput: input from user containing multiple strings and frets
# string: string regex for the desired fret will be extracted
# returns: the fret number of "-"
def fretExtract(string: str, userInput: str):
    search: str = listToStr(re.findall(string + "\d*", userInput))
    if (search == string):
        return 0
    elif (search == ""):
        return "-"
    else:
        print(listToStr(re.findall(string + "(\d)*", search)))
        return int(listToStr(re.findall(string + "(\d)*", search)))

# format the output to fret number (or "-") plus "timing"
def timingInserter(timing: int, fret: str):
    return str(fret) + "-" * timing

# if the input is empty just skips one "beat", else process the input to
# extract all the frets in the user input
# input: user input of frets/empty
# timing: how many "-" are placed after each fret in the tab
def processInput(input: str, timing: int):
    if input == "":
        e1String.append("-")
        a1String.append("-")
        d1String.append("-")
        g1String.append("-")
        b1String.append("-")
        e2String.append("-")
    else:
        e1String.append(timingInserter(timing,fretExtract("E", input)))
        a1String.append(timingInserter(timing,fretExtract("A", input)))
        d1String.append(timingInserter(timing,fretExtract("D", input)))
        g1String.append(timingInserter(timing,fretExtract("G", input)))
        b1String.append(timingInserter(timing,fretExtract("B", input)))
        e2String.append(timingInserter(timing,fretExtract("e", input)))

# presents the current state of the arrays storing the tab
def present():
    e1 = "E|-"
    a1 = "A|-"
    d1 = "D|-"
    g1 = "G|-"
    b1 = "B|-"
    e2 = "e|-"
    for time in range(len(e1String)):
        e1 += str(e1String[time])
        a1 += str(a1String[time])
        d1 += str(d1String[time])
        g1 += str(g1String[time])
        b1 += str(b1String[time])
        e2 += str(e2String[time])
    os.system('clear')
    print(e2)
    print(b1)
    print(g1)
    print(d1)
    print(a1)
    print(e1)

# main loop
# exits upon 2 invalid inputs
def main():
    # valid inputs from user
    # an invalid would set insist to false, two will end the program
    validInputs: str = "(E|A|D|G|B|e|a|d|g|b)\d*"
    keepRunning: bool = True
    insist: bool = True

    #requests "timing" aka. the "-" between each fret
    timing: int = int(input("type the timing: "))

    # while dont receive 2 back to back inputs from user, keeps running
    while(keepRunning | insist):
        insist = keepRunning
        keepRunning = False
        line: str = input()

        # removes the previous tempo stored if an "(u|U)" are inserted
        if line == "u" or line == "U":
            keepRunning = True
            e1String.pop()
            a1String.pop()
            d1String.pop()
            g1String.pop()
            b1String.pop()
            e2String.pop()
            present()
            continue

        # validate input, if false twice ends the program
        isValid = re.search("[^" + validInputs + "]",line)
        if (isValid):
            keepRunning = False
            if (insist):
                continue
            else:
                break
        else:
            # Append the input to the tab
            keepRunning = True
            # extract data from input
            processInput(line, timing)
            # present data extracted
            present()

main()
