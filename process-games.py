from argparse import ArgumentParser
from collections import namedtuple
from pyautogui import typewrite
from time import sleep

Entry = namedtuple("Entry", ["platform", "priority", "name"])

arg_parser = ArgumentParser()
arg_parser.add_argument(
    "-i",
    "--input-path",
    help="Input Path",
    metavar="INPUT_PATH",
    dest="input_path",
    required=True
)
args = arg_parser.parse_args()

input_path = args.input_path

with open(input_path, "r") as input_file:
    input_data = input_file.read()

entries = []

lines = input_data.splitlines()
for line in lines:
    if not line:
        continue

    if "=" in line:
        splitLine = line.split("=")

        key = splitLine[0]
        value = splitLine[1]

        if key == "platform":
            currPlatform=value
        elif key == "priority":
            currPriority=int(value)
        else:
            raise Exception("Invalid Key")
    else:
        newEntry = Entry(currPlatform, currPriority, line)
        entries.append(newEntry)


print("Get ready...starting in 5 seconds")
sleep(5)

i = 0
for entry in entries:
    progress = round(100 * i / len(entries), 2)
    status = "Processing {} ({}% complete)".format(entry.name, progress)
    print(status)

    # Tab to the game name
    typewrite(["\t"] * 8)
    typewrite(entry.name)

    # Tab to platform
    typewrite(["\t"] * 2)
    typewrite(entry.platform)

    # Tab to category
    typewrite(["\t"] * 3)
    numRights = entry.priority - 1
    typewrite(["right"] * numRights)
    typewrite(["space"])

    # Tab to Unplayed
    typewrite(["\t"] * 2)
    typewrite(" ")

    typewrite(["enter"])
    sleep(5)

    i += 1
