import random
import time

names = ["Roger", "Nadal", "Novac", "Andre", "Sarena", "Mariya", "Martina", "Mark", "Amber", "Todd", "Anita", "Sandy"]
used = {}

for each in names:
    used[each] = 0

def printname(name, count):

    used[name] += 1

    print("\n\nRun #%s:\nChosen name: %s\n-------------" % (count, name))
    print("Hello %s... (used %s times)\n" % (name, used[name]))

    tally = dict(sorted(used.items(), key=lambda item: item[1], reverse=True))
    print("Tally\n-------------")
    for k, v in tally.items():
        print (k, v)

if __name__ == '__main__':

    max = 250
    count = 0

    while count < max:

        count += 1

        index = random.randrange(0, len(names))
        printname(names[index], count)

        time.sleep(1)




