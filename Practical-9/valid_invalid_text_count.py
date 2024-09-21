def count_valid_invalid(strings, is_valid_function):
    """
    Counts the number of valid and invalid strings in a list based on a given validation function.

    Args:
        strings (list): List of strings to validate.
        is_valid_function (function): A function that takes a string and returns True if valid, False otherwise.

    Returns:
        dict: A dictionary with counts of valid and invalid strings.
    """
    valid_count = 0
    invalid_count = 0

    for string in strings:
        if is_valid_function(string):
            valid_count += 1
        else:
            invalid_count += 1

    return {"valid": valid_count, "invalid": invalid_count}

# Example usage:
def is_valid_example(string):
    # Example: Valid strings contain only alphabetic characters.
    return string.isalpha()

# Input list of strings
test_strings = ["hello", "world123", "Python", "", "1234"]

# Count valid and invalid strings
result = count_valid_invalid(test_strings, is_valid_example)
print(result)  # Output: {'valid': 2, 'invalid': 3}

