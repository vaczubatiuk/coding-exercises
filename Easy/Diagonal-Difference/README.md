# Diagonal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below: $$
\begin{bmatrix}
A & B & C \cr
D & E & F \cr
G & H & I
\end{bmatrix}
$$

| Description | Formula   |
| :----------- | :------------ |     
| The left-to-right diagonal   | $X = A + E + I$ |
| The right to left diagonal   | $C + E + G = Y$ |
| Their absolute difference is | $\| X - Y \|$ |
  


## Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int $arr[n][m]$: an array of integers

### Return

int: the absolute diagonal difference

### Input Format

The first line contains a single integer, $n$, the number of rows and columns in the square matrix .
Each of the next $n$ lines describes a row, $arr[i]$, and consists of $n$ space-separated integers $arr[i][j]$

## Constraints

### Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

### Sample Input
```
3
11 2 4
4 5 6
10 8 -12
```
### Sample Output

15

## Explanation

The primary diagonal is:

$$
\begin{bmatrix}
11 & & \cr
& 5 & \cr
& & -12
\end{bmatrix}
$$

The secondary diagonal is:

$$
\begin{bmatrix}
& & 4\cr
& 5 & \cr
11 & &
\end{bmatrix}
$$

```
     4
   5
10
```
Sum across the secondary diagonal: $4 + 5 + 10 = 19$
Difference: $|4 - 19| = 15$

Note: $|x|$ is the absolute value of $x$
