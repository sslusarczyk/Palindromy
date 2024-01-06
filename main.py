def palindrome(word):
  """
      Check if Palindrome, based on arguments passed
      Arguments:
      word -- string to check if palindrome
  """
  reversed_word = word[::-1]
  if word == reversed_word:
     result = True
  else:
     result = False
  return result
print(palindrome("kajak"))