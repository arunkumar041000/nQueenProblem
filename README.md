# n Queen Problem
n Queen Problem in oops


# Time Complexity: O(N!)
# Auxiliary Space: O(N2)

Optimization in is_safe() function 
The idea is not to check every element in right and left diagonal, instead use the property of diagonals: 
1. The sum of i and j is constant and unique for each right diagonal, where i is the row of elements and j is the 
column of elements. 
2. The difference between i and j is constant and unique for each left diagonal, where i and j are row and column of element respectively.
Implementation of Backtracking solution(with optimization) 