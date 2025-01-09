def is_even(value):
    return value % 2 == 0

def is_even_too(value):
    return value & 1 == 0

#Test
print(is_even(7))
print(is_even(16))
print(is_even(0))
print(is_even(-1))

print(is_even_too(7))
print(is_even_too(16))
print(is_even_too(0))
print(is_even_too(-1))