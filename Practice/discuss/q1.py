"""
The problem was a story-based problem. You are an Amazon delivery guy who needs to deliver parcels to buildings painted in different colors. Your task is to reach the end of the buildings in the minimum number of steps.

You are allowed to have the following operations standing on the ith building:

You can take a step forward or backward, i.e. (i+1) or (i-1).
You can go to the jth building with the same color as that of the ith in one move.
Eg. Input : [ 1 0 0 2 1 3 ] (Starting from 0th index -> 4th index -> last index)
Output : 2
"""

def minSteps(arr):
    n = len(arr)

    dp = [float('inf')]*n

    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if arr[i] == arr[j]:
                dp[i] = min(dp[i], dp[j]+1)
            else:
                dp[i] = min(dp[i], dp[j]+abs(i-j))

    return dp[-1]

print(minSteps([1, 0, 0, 2, 1, 3]))
