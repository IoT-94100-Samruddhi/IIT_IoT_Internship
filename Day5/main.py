from operations.arithmetic import add, mul
from operations.string_ops import reverse_string, count_vowels

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))

print(add(a,b))
print(mul(a,b))
print(reverse_string("Hello"))
print(count_vowels("Hello"))

