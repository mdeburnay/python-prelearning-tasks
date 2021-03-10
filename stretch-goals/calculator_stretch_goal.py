def calculator(a, b, operator):
    # ==============
    # Your code here

    if operator == "+":
        strBinary = str(bin(a + b))
        binaryResult = int(strBinary[2:])
        return binaryResult
    if operator == "-":
        strBinary = str(bin(a - b))
        binaryResult = int(strBinary[2:])
        return binaryResult
    if operator == "*":
        strBinary = str(bin(a * b))
        binaryResult = int(strBinary[2:])
        return binaryResult
    if operator == "/":
        strBinary = str(bin(a // b))
        binaryResult = int(strBinary[2:])
        return binaryResult

    # ==============


print(calculator(2, 4, "+"))  # Should print 110 to the console
print(calculator(10, 3, "-"))  # Should print 111 to the console
print(calculator(4, 7, "*"))  # Should print 11100 to the console
print(calculator(100, 2, "/"))  # Should print 110010 to the console
