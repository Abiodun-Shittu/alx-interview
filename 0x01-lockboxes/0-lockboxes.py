#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    for i in range(n):
        if unlocked[i]:
            for key in boxes[i]:
                if key < n and not unlocked[key]:
                    unlocked[key] = True
                    keys.extend(boxes[key])

    return all(unlocked)
