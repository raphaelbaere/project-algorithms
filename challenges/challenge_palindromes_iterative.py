def is_palindrome_iterative(word):
    if word == '':
      return False
    is_palindrome = True
    for i in range(len(word)):
        highIndex = len(word) - 1 - i
        if i == highIndex:
            return True
        if word[i] != word[highIndex]:
            is_palindrome = False
    return is_palindrome