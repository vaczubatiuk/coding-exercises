# Min Max Sum

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#### Example

&emsp;`arr = [1, 3, 5, 7, 9, ]`
&emsp;The minimum sum is `1 + 3 + 5 + 7 = 16` and the maximum sum is `3 + 5 + 7 + 9 = 24`. The function prints

&emsp;`16 24`

#### Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

- arr: an array of 5 integers

#### Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

#### Input Format

A single line of five space-separated integers.

#### Constraints
```
1 ≤ arr[i] ≤ 10<sup>9</sup>
```
#### Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

#### Sample Input

&emsp;`1 2 3 4 5`

#### Sample Output

&emsp;`10 14`

### Explanation

The numbers are 1, 2, 3, 4, and 5. Calculate the following sums using four of the five integers:

- &emsp;Sum everything except `1`, the sum is `2 + 3 + 4 + 5 = 14`.
- &emsp;Sum everything except `2`, the sum is `1 + 3 + 4 + 5 = 13`.
- &emsp;Sum everything except `3`, the sum is `1 + 2 + 4 + 5 = 12`.
- &emsp;Sum everything except `4`, the sum is `1 + 2 + 3 + 5 = 11`.
- &emsp;Sum everything except `5`, the sum is `1 + 2 + 3 + 4 = 10`.