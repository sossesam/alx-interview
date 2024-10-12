#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
Each box may contain keys to other boxes. The function checks if starting from the
first box, all other boxes can eventually be opened.
"""

from collections import deque

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened starting from the first box.

    This function uses a breadth-first search (BFS) approach to explore the boxes.
    It begins with the first box (index 0) and uses a queue to manage the boxes
    that need to be checked. As keys are found, they are used to open new boxes
    and add them to the queue for further exploration.

    Args:
        boxes (list of list of int): A list where each element is a list of integers representing keys
                                     to other boxes. The index of the list represents the box number.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Example:
        boxes = [[1], [2], [3], [4], []]
        canUnlockAll(boxes) -> True

        boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        canUnlockAll(boxes) -> True

        boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        canUnlockAll(boxes) -> False
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    queue = deque([0])

    while queue:
        current = queue.popleft()
        for key in boxes[current]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)
















"""def create_boxes(array):
    all_boxes = {}
    count = 0
    for box in array:
        
        all_boxes[count] = {}
        all_boxes[count]['boxes'] = box
        if count == 0:
            all_boxes[count]['open']=True
        else:
            all_boxes[count]['open']=False
        count+=1
    return all_boxes




def canUnlockAll(boxes):
    new_box =create_boxes(boxes)"""
    
    



    
    


