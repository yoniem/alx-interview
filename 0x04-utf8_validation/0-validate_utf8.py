#!/usr/bin/python3
def validUTF8(data):
    """
    Validate if a given list of integers is a valid UTF-8 encoding.
    
    Args:
    data (List[int]): List of integers representing bytes.
    
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining in the current UTF-8 character
    num_bytes = 0
    
    # Masks for checking the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6
    
    # Iterate through each integer in the data list
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1
            
            # For 1 byte character
            if num_bytes == 0:
                continue
            
            # If the number of bytes is more than 4 or 1, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For subsequent bytes, they must start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        # Decrement the number of bytes remaining
        num_bytes -= 1
    
    # If there are remaining bytes expected, it's invalid
    return num_bytes == 0

# Example usage
if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
