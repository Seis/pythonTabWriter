import re
import os

e1String: list = []
a1String: list = []
d1String: list = []
g1String: list = []
b1String: list = []
e2String: list = []

def listToStr(a: list):
    return "".join(a)

def fretExtract(string: str, userInput: str):
    search: str = listToStr(re.findall(string + "\d*", userInput))
    if (search == string):
        return 0
    elif (search == ""):
        return "-"
    else:
        print(listToStr(re.findall(string + "(\d)*", search)))
        return int(listToStr(re.findall(string + "(\d)*", search)))

def timingInserter(timing: int, fret: str):
    return str(fret) + "-" * timing

def teta(input: str, timing: int):
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

def main():
    keepRunning: bool = True
    insist: bool = True
    validInputs: str = "(E|A|D|G|B|e)\d*"


    timing: int = int(input("type the timing: "))
    while(keepRunning | insist):
        insist = keepRunning
        keepRunning = False
        line: str = input()


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

            teta(line, timing)
            present()

main()
