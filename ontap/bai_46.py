def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for x in num_set:
        if x - 1 not in num_set:
            curr = x
            streak = 1
            while curr + 1 in num_set:
                curr += 1
                streak += 1
            longest = max(longest, streak)
            
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))