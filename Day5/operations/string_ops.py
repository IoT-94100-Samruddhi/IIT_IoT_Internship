def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in 'aeiou':
            count += 1
    return count
