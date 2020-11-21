# Words Concatenation (hard) #
# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.
#
# Example 1:
#
# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".
# Example 2:
#
# Input: String="catcatfoxfox", Words=["cat", "fox"]
# Output: [3]
# Explanation: The only substring containing both the words is "catfox".


def find_word_concatenation(str, words):
    re = []
    for i in range(len(str)):
        l = len(words[0])
        s = i
        e = i + l

        tmp_words = words.copy()
        loop = 0
        while e <=len(str) and loop < len(words):
            if str[s:e] in tmp_words:
                tmp_words.remove(str[s:e])
            s = e
            e = e + l
            loop += 1
        if tmp_words == []:
            re.append(i)
    return re

print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))