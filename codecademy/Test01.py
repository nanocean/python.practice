def is_int(x):
    while int(x) != x:
        x *= 10

        if x % 10 != 0:
            return False
    else:
        return True

# print(is_int(1.0000))

# def digit_sum(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n = int(n / 10)
#
#     return sum

# def digit_sum(n):
#     if n <= 0:
#         return n
#     else:
#         return (n % 10) + digit_sum(n // 10)
#
# print(digit_sum(12345))

# print(12//10)

# def factorial(x):
#     r = 1
#     for i in range(1, x + 1):
#         r *= i
#
#     return r

# def factorial(n):
#     if n < 2:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(4))
#
# def is_prime(x):
#     if x == 1 or x == 2:
#         return True
#
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     else:
#         return True
#
# print(is_prime(10))

# def reverse(s):
#     r = ""
#     for index, value in enumerate(s):
#         r += s[len(s) - index - 1]
#     return r
#
# print(reverse("asdf"))


# print(type(reversed("asdf")))

l = reversed("asdf")

for e in l:
    print(e),

print
