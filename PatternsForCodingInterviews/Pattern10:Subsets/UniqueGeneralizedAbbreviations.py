# Problem Statement #
# Given a word, write a function to generate all of its unique generalized abbreviations.
#
# Generalized abbreviation of a word can be generated by replacing each substring of the word by the count of characters in the substring. Take the example of “ab” which has four substrings: “”, “a”, “b”, and “ab”. After replacing these substrings in the actual word by the count of characters we get all the generalized abbreviations: “ab”, “1b”, “a1”, and “2”.
#
# Example 1:
#
# Input: "BAT"
# Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"
# Example 2:
#
# Input: "code"
# Output: "code", "cod1", "co1e", "co2", "c1de", "c1d1", "c2e", "c3", "1ode", "1od1", "1o1e", "1o2",
# "2de", "2d1", "3e", "4"

from collections import deque
def generate_generalized_abbreviation(word):
    q = deque()
    q.append([])
    for n in word:
        for _ in range(len(q)):
            tmp = q.popleft()
            newtmp = tmp.copy()
            newtmp.append(n)
            q.append(tmp)
            q.append(newtmp)
    result = []
    while q:
        tmp = q.popleft()
        i, j = 0, 0
        code = ""
        while i < len(word):
            skippedn = 0
            while i < len(word) and j < len(tmp) and word[i] != tmp[j] :
                skippedn += 1
                i += 1

            if skippedn != 0:
                code += str(skippedn)
            if j < len(tmp):
                code += tmp[j]
                j += 1
            else:
                code += str(len(word) - i)
                break
            i += 1
        result.append(code)
    return result




def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()