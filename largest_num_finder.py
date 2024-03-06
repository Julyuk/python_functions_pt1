def largest_num(num1, num2):
    """
        Finds and returns the largest number between two given numbers.

        Parameters:
        - num1 (float or int): The first number.
        - num2 (float or int): The second number.

        Returns:
        - float or int: The largest number between num1 and num2.

        Example:
        print(largest_num(5, 8))
        8
        print(largest_num(-3, 0))
        0
        """
    return max(num1, num2)


print(largest_num(5, 8))
print(largest_num(-3, 0))