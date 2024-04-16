def print_staircase(n):
    for i in range(1, n + 1):
        # Print spaces
        spaces = " " * (n - i)
        # Print hashtags
        hashtags = "#" * i
        # Print the staircase row
        print(spaces + hashtags)

# Citirea numărului de la tastatură
n = int(input("Introduceți dimensiunea scării: "))

# Afișarea scării
print_staircase(n)