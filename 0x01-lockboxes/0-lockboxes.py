def can_unlock_all(boxes):
    """
    Determine if all the boxes can be unlocked.

    Args:
        boxes (list of list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Set to keep track of unlocked boxes
    unlocked_boxes = {0}
    
    # List to keep track of boxes yet to be checked
    boxes_to_check = [0]

    while boxes_to_check:
        current_box = boxes_to_check.pop()
        keys = boxes[current_box]

        for key in keys:
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                boxes_to_check.append(key)

    return len(unlocked_boxes) == len(boxes)
