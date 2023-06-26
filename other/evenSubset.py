# Even Length Subsets
# Given a set of numbers k, find all subsets of k such
# that each has an even number of integers, and then
# return the sum of all these subsets.
# A subset is a contiguous subsequence of k.

# Example:
# Input: k = [1,4,2,5]
# Output: 30
# Explanation: The possible subarrays
# of k and their sums are:
# [1,4] = 5
# [4,2] = 6
# [2,5] = 7
# [1,4,2,5] = 12
# The sum of all above subarrays = 5
# + 6 + 7 + 12 = 30

# Constraints:
# • 1 <= k.length <= 100
# • 1 <= k[i] <= 1000



import itertools

def solution(k):
    lists = []
    res = 0

    for i in range(2, len(k)+1, 2):
        lists.extend(list(itertools.combinations(k, i)))

    print(lists)
    for comb in lists:
        res += sum(list(comb))

    return res

print(solution([1, 4, 2, 5]))