def number_input(message):
    try:
        return int(input(message))
    except ValueError:
        return number_input(message)

no = number_input("type only number")
print("no: " + str(no))
