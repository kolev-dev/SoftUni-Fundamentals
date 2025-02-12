words = input().split()
palindrome = input()

total_palindromes = [word for word in words if word == word[::-1]]
total_palindrome_count = total_palindromes.count(palindrome)

print(total_palindromes)
print(f"Found palindrome {total_palindrome_count} times")
