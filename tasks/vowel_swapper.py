def vowel_swapper(string):
    # ==============
    # Your code here
    # dict = {'a': '4', 'A': '4', 'e': '3', 'E': '3', 'i': '!',
    #         'I': '!', 'o': 'ooo', 'O': '000', 'u': '|_|', 'U': '|_|'}

    # for char in string:
    #     if char in dict:
    #         print(dict[char], end='')
    #     else:
    #         print(char, end='')

    string = string.replace("a", "4")
    string = string.replace("A", "4")
    string = string.replace("e", "3")
    string = string.replace("E", "3")
    string = string.replace("i", "!")
    string = string.replace("I", "!")
    string = string.replace("o", "ooo")
    string = string.replace("O", "000")
    string = string.replace("u", "|_|")
    string = string.replace("U", "|_|")

    return string
    # ==============


# Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("aA eE iI oO uU"))
# Should print "H3llooo Wooorld" to the console
print(vowel_swapper("Hello World"))
# Should print "3v3ryth!ng's 4v4!l4bl3" to the console
print(vowel_swapper("Everything's Available"))
