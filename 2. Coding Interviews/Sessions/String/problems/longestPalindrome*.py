"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

# Requirement O(n^2)
# Key hint
# Type 1: aba
# Type 2: abba

# O(n^2)
import math
def longestPalindrome(s):
    maxl = -math.inf
    for i in range(len(s)):
        l1 = getPalindromLen(s, i, i)
        l2 = getPalindromLen(s, i , i+ 1)
        maxl = max(maxl,l1, l2)
    return maxl

def getPalindromLen(str, i, j):
    s, e =i, j
    while s >= 0 and e < len(str) and str[s] == str[e]:
        s -= 1
        e += 1
    return e -1  - (s + 1) + 1
print(longestPalindrome("babad"))
print(longestPalindrome("babab"))
print(longestPalindrome("aabab"))

# import timeit
# w = "uhrfjotnewtodhmbplsaolnpcdaohiytmfllukijouxipvqohtsgxbtfoxyfkfczkfwhzimbefiohmtimrcxbpgcxogystdkcqujvbxsgirpccdnvejtljftwkdpsqpflzwruwwdzovsbmwbcvlftkjnxqaguvtsycylqzquqkbnybnbaeahbxejhphwrpmymcemuhljwtuvxefqfzjhskuqhifydkxpnfwfxkpeexnjltfqwfvchphmtsrsyayxukvmlqodshqwbeaxhcxdbssnrdzvxtusngwqdxvluauphmmbwmgtazjwvolenegwbmjfwprfuswamyvgrgshqocnhirgyakbkkggviorawadzhjipjjgiwpelwxvtaegauerbwpalofrbghfhnublttqtcmqskcocwwwxpnckrnbepusjyohsrretrqyvgnbezuvwmzizcefxyumtdwnqjkgsktyuacfpnqocqjxcurmipjfqmjqrkdeqsfseyigqlwmzgqhivbqalcxhlzgtsfjbdbfqiedogrqasgmimifdexbjjpfusxsypxobxjtcwxnkpgkdpgskgkvezkriixpxkkattyplnpdbdifforxozfngmlgcunbnubzamgkkfbswuqfqrvzjqmlfqxeqpjaqayodtetsecmfbplscmslpqiyhhykftzkkhshxqvdwmwowokpluwyvavwvofwqtdilwqjgrprukzyhckuspyzaoe"
# start = timeit.timeit()
# print(longestPalindrome(w))
# end = timeit.timeit()
# print(end - start)
#
# print("DP approach")
# Dynamic Approach O(n^2)
# If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

# We define F(i, j) = True, if Substring Si .... Sj is a Palrindrome
#                     False, Otherwise
#
# Therefore, F(i, j) = F(i-1, j+1) and Si == Sj

# It is o(n^2) but Expand Around Center seems better solution.
# Becasue it got time out
def longestPalindrome_dp(s):
    dp = [[True]*(len(s) +1) for _ in range(len(s) + 1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0 :
                dp[i][j] = True
            if i >= j:
                dp[i][j] = True

    for j in range(1, len(dp[0])):
        for i in range(0, j):
            if s[i-1] == s[j-1]:
                if dp[i+1][j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                dp[i][j] = False

    maxd = (0, 0, 0)

    #for l in dp:
    #    print(l)
    for j in range(1, len(dp[0])):
        for i in range(1, j):
            if dp[i][j] == True and maxd[0] < j - i:
                maxd = (j-i, i-1, j-1)
    return s[maxd[1] : maxd[2] +1]


# print(longestPalindrome_dp("babad"))
# print(longestPalindrome_dp("babab"))
# print(longestPalindrome_dp("aabab"))
# print(longestPalindrome_dp("cbbd"))
# print(longestPalindrome_dp("bb"))
# print(longestPalindrome_dp("a"))

# This had timeout
# w = "uhrfjotnewtodhmbplsaolnpcdaohiytmfllukijouxipvqohtsgxbtfoxyfkfczkfwhzimbefiohmtimrcxbpgcxogystdkcqujvbxsgirpccdnvejtljftwkdpsqpflzwruwwdzovsbmwbcvlftkjnxqaguvtsycylqzquqkbnybnbaeahbxejhphwrpmymcemuhljwtuvxefqfzjhskuqhifydkxpnfwfxkpeexnjltfqwfvchphmtsrsyayxukvmlqodshqwbeaxhcxdbssnrdzvxtusngwqdxvluauphmmbwmgtazjwvolenegwbmjfwprfuswamyvgrgshqocnhirgyakbkkggviorawadzhjipjjgiwpelwxvtaegauerbwpalofrbghfhnublttqtcmqskcocwwwxpnckrnbepusjyohsrretrqyvgnbezuvwmzizcefxyumtdwnqjkgsktyuacfpnqocqjxcurmipjfqmjqrkdeqsfseyigqlwmzgqhivbqalcxhlzgtsfjbdbfqiedogrqasgmimifdexbjjpfusxsypxobxjtcwxnkpgkdpgskgkvezkriixpxkkattyplnpdbdifforxozfngmlgcunbnubzamgkkfbswuqfqrvzjqmlfqxeqpjaqayodtetsecmfbplscmslpqiyhhykftzkkhshxqvdwmwowokpluwyvavwvofwqtdilwqjgrprukzyhckuspyzaoe"
# start = timeit.timeit()
# print(longestPalindrome_dp(w))
# end = timeit.timeit()
# print(end - start)