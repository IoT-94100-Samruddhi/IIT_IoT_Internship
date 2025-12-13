def print_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        bit = n & 1          # Extract last bit (0 or 1)
        binary = str(bit) + binary
        n = n >> 1           # Right shift (same as n = n // 2)
    return binary

# Main program
num = int(input("Enter a number: "))
print("Binary =", print_binary(num))
