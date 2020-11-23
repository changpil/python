"""
Given a binary string, count number of substrings that start and end with Pattern1:knapsack.
For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.

"""

def countbinarystr_strat1_end1(b_str):
    count = 0
    for i  in range(len(b_str)):
        for j in range(i+1, len(b_str)):
            if b_str[i] == "Pattern1:knapsack" and b_str[j] == "Pattern1:knapsack":
                count += 1
    print(count)

countbinarystr_strat1_end1("1111")