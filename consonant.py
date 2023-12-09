def solve(word):
  vowels = set("aeiou")
  max_value = 0
  current_value = 0
  for c in word:
    if c not in vowels:
      current_value += ord(c) - ord('a') + 1
    else:
      current_value = 0
    max_value = max(max_value, current_value)
  return max_value

# Test cases
print(solve("zodiacs")) # Output: 26
print(solve("strength")) # Output: 57

