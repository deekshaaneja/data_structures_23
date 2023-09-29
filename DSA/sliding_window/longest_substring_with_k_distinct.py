
'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.


'''


def longest_substring_with_k_distinct(str1, k):
    freq = {}
    window_start = 0
    max_len = 0
    for window_end in range(len(str1)):
        if not freq.get(str1[window_end]):
            freq[str1[window_end]] = 0
        freq[str1[window_end]] += 1
        if len(freq)<=k:
            max_len = max(max_len, 1 + window_end - window_start)
        else:
            print(freq)
            freq[str1[window_start]]-=1
            if freq[str1[window_start]]==0:
                freq.pop(str1[window_start])
            window_start+=1
    return max_len

def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
