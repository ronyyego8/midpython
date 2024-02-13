def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", " ").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Test the function
string = input("Enter a string:")
if is_palindrome(string):
    print("Yes, its a palindrome.")
else:
    print("No, its not a palindrome.")
