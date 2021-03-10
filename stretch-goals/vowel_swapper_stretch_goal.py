def vowel_swapper(string):
    # ==============
    # Your code here

    dict = {
        "a": "4", "A": "4", "e": "3",
        "E": "3", "i": "!", "I": "!",
        "o": "ooo", "O": "000",
        "u": "|_|", "U": "|_|"
    }

    result = []
    currentVowels = []

    split_string = string.split()
    for word in split_string:
        wordLength = len(word)
        wordArr = []
        chars = 0
        for char in word:
            if char in dict:
                currentVowels.append(char.lower())
                vowelCount = currentVowels.count(char.lower())
                if vowelCount == 2:
                    chars += 1
                    char = char.replace(char, dict[char])
                    wordArr.append(char)
                    if chars == wordLength:
                        wordStr = "".join(wordArr)
                        result.append(wordStr)
                else:
                    wordArr.append(char)
                    chars += 1
                    if chars == wordLength:
                        wordStr = "".join(wordArr)
                        result.append(wordStr)
            else:
                wordArr.append(char)
                chars += 1
                if chars == wordLength:
                    wordStr = "".join(wordArr)
                    result.append(wordStr)
    return " ".join(result)

    # ==============


# Should print "a4a e3e i!i o000o u|_|u" to the console
print(vowel_swapper("aAa eEe iIi oOo uUu"))
# Should print "Hello Wooorld" to the console
print(vowel_swapper("Hello World"))
# Should print "Ev3rything's Av4!lable" to the console
print(vowel_swapper("Everything's Available"))
