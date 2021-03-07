def vowel_swapper(string):
    # ==============
    # Your code here

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
