# Miminum Path Cover Problem
========
A path cover is a directed graph G=(V,E) is a set P of vertex-disjointed paths such that every vertex in V is included in exactly one path in P. Pathsj may start and end anyuwhere, and they may be of any length, including 0. A minimum path cover of G is a path cover conatining the fewest possible points

Given an efficient algorithm to find a minimum path cover of a directed acyclic graph G=(V,E). Assuming that V = {1,2,...,n}, construct the graph G'=(V',E'), where :
```
        V′​={ x0​, x1​, … , xn ​} ∪ { y0​, y1​, … , yn ​},
        E′={ (x0​,xi​) : i ∈ V } ∪ { (yi​,y0​) : i ∈ V } ∪ { (xi​,yj​) : (i,j) ∈ E },​
```
And run a maximum-flow algorithm.

Quick scientific explanation of the Minimum Path Cover problem: https://walkccc.me/CLRS/Chap26/Problems/26-2/

## Explanation

Given two missiles i and j, where as Tj >= Ti (missiles sorted via time of T)

A single hackerX missile can be used to stop both i and j if the difference in frequence between them is less than or equal to the amount of time between their arrivals. In the HackerX problem ratio of frequency change vs time required is 1:!(A change of 1 in frequency F, requires 1 unit of time T). This can be mathematically described as with the following condition:
```
        Tj - Ti >= |Fj - Fi| 
```

## An O(n<sup>2</sup>) Solution
For now, For simplicity sake, lets make the assumption:
```
        Fi > Fj
```
To remove the absolute value, reducing the condition to:
```
        Tj - Ti >= Fi - Fj
```
Next, add Fj to both sides, transforming the condition to:
```
        Tj - Ti + Fj >= Fi
```
Lastly, add Ti to both sides, transforming the condition to:
```
      Tj + Fj >= Ti + Fi
```

It is stated that we need at least one HackerX missile to cover the first missile. The question after, is how many other missiles can the first missile cover. To find this out, a linear scan through the list would display it. Then a simple check to see each subsequent value satisifies the condition. However, this is not a great solution, due to the O(n<sup>2</sup>) time of complexity. Which can be done better.

###Finding the Correct Way###
