import time

def test_recursive(i: int) -> None:
    """
    This function made to demonstrate the recursive function. 
    Prints the value of i, waits for 1 second, and recursively calls itself with i decremented by 1 until i becomes 0.
    test_recursive(i) -> test_recursive(i-1) -> ... -> test_recursive(0)

    Args:
        i (int): The value of i.

    Returns:
        None
    """
    print(i)  # Print the value of i
    time.sleep(1)  # Wait for 1 second
    i -= 1  # Decrement i by 1
    if i > 0:
        test_recursive(i)  # Recursively call test function with i decremented by 1
    return  # Return None

if __name__=='__main__':
    test_recursive(5)