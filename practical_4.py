def change_case(text: str, style: str) -> str:
    if style.lower() == 'c':  # Convert to uppercase
        return text.upper()
    elif style.lower() == 's':  # Convert to lowercase
        return text.lower()
    elif style.lower() == 'r':  # Reverse the case
        return text.swapcase()
    elif style.lower() == 'u':  # Alternate the case starting from the first letter
        result = []
        for i, char in enumerate(text):
            if i % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
        return ''.join(result)
    else:
        return "Invalid style option."

# Test cases
print(change_case("hello world", "C"))  # Should print HELLO WORLD
print(change_case("Hello World", "S"))  # Should print hello world
print(change_case("Hello World", "R"))  # Should print hELLO wORLD
