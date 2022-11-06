'''
852. Peak Index in a Mountain Array

An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
'''

#CODE

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = len(arr)
        
        for i in range(l):
            if arr[i] < arr[i+1] and arr[i+1] > arr[i+2]:
                return i+1
