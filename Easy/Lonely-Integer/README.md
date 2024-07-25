# Lonely Integer

Given an array of integers, where all elements but one occur twice, find the unique element.

### Example
&emsp;`arr = [1, 2, 3, 4, 3, 2, 1]`

&emsp;The unique element is `4`

### Function Description

#### Complete the lonelyinteger function in the editor below.

&emsp;lonelyinteger has the following parameter(s):

- &emsp;`int` $a[n]$: an array of integers

### Returns
- &emsp;`int`: the element that occurs only once

### Input Format
&emsp;A line contains $n$ space-separated integers that describe the values in .

### Constraints
- &emsp;&emsp; $1 \leq n \leq 100$
- &emsp;&emsp; $n \mod 2  \neg  0$ 
- &emsp;&emsp; $n_i  \neg  n_(i+1) where n_(i+l) \leq n$ 
- &emsp;&emsp; $n_i  \neg  n_(i-1) where n_(i-1) \geq 1$
- &emsp;&emsp; $0 \leq arr[i] \leq 100$, where $0 \leq i \leq n$
