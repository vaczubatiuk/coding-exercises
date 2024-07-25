# Left Rotation

A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. Given an integer, d, rotate the array that many steps left and return the result.0

#### Example
```css
d = 2
arr = [1, 2, 3, 4, 5]
After n rotations the list is now [3, 4, 5, 1, 2]
```

Function Description

Complete the rotateLeft function in the editor below.

rotateLeft has the following parameters:

- int d: the amount to rotate by
- int arr[n]: the array to rotate
Returns

- int[n]: the rotated array

### Input Format

The first line contains two space-separated integers that denote n, the number of integers, and d, the number of left rotations to perform.
The second line contains n space-separated integers that describe arr[ ].

### Constraints
$1 \leq n \leq 10<sup>5</sup>$
1 ≤ d ≤ n
1 ≤ a[i] ≤ 10<sup>6</sup>

### Sample Input
```css
5 4
1 2 3 4 5
```
### Sample Output
```css
5 1 2 3 4
```
### Explanation
To perform d = 4 left rotations, the array undergoes the following sequence of changes:
```css
[1, 2, 3, 4, 5] --> [2, 3, 4, 5, 1] --> [3, 4, 5, 1, 2] --> [4, 5, 1, 2, 3] --> [5, 1, 2, 3, 4]
```
