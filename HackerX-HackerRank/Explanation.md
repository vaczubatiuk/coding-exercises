# Miminum Path Cover Problem
========
A path cover is a directed graph G=(V,E) is a set P of vertex-disjointed paths such that every vertex in V is included in exactly one path in P. Pathsj may start and end anyuwhere, and they may be of any length, including 0. A minimum path cover of G is a path cover conatining the fewest possible points

Given an efficient algorithm to find a minimum path cover of a directed acyclic graph G=(V,E). Assuming that V = {1,2,...,n}, construct the graph G'=(V',E'), where :

- V′​={ x<sub>0​,</sub>, x<sub>1</sub>​, … , x<sub>n</sub> ​} ∪ { y<sub>0</sub>​, y<sub>1​</sub>, … , y<sub>n</sub> ​},

- E′={ ( x<sub>0​</sub>, x<sub>i</sub>​ ) : i ∈ V } ∪ { ( y<sub>i</sub>​, y<sub>0</sub> ​) : i ∈ V } ∪ { ( x<sub>i​</sub>, y<sub>j</sub>​ ) : (i,j) ∈ E },​


And run a maximum-flow algorithm.

Quick scientific explanation of the Minimum Path Cover problem: https://walkccc.me/CLRS/Chap26/Problems/26-2/

## Explanation

Given two missiles i and j, where as T<sub>j</sub> >= T<sub>i</sub> (missiles sorted via time of T)

A single hackerX missile can be used to stop both i and j if the difference in frequence between them is less than or equal to the amount of time between their arrivals. In the HackerX problem ratio of frequency change vs time required is 1:1 (A change of 1 in frequency F, requires 1 unit of time T). This can be mathematically described as with the following condition:

- T<sub>j</sub> - T<sub>i</sub> >= |F<sub>j</sub> - F<sub>i</sub>| 


## An O(n<sup>2</sup>) Solution
For now, For simplicity sake, lets make the assumption:

- F<sub>i</sub> > F<sub>j</sub>

To remove the absolute value, reducing the condition to:

- T<sub>j</sub> - T<sub>i</sub> >= F<sub>i</sub> - F<sub>j</sub>

Next, add F<sub>j to both sides, transforming the condition to:

- T<sub>j</sub> - T<sub>i</sub> + F<sub>j</sub> >= F<sub>i</sub>

Lastly, add T<sub>i to both sides, transforming the condition to:

- T<sub>j</sub> + F<sub>j</sub> >= T<sub>i</sub> + F<sub>i</sub>


It is stated that we need at least one HackerX missile to cover the first missile. The question after, is how many other missiles can the first missile cover. To find this out, a linear scan through the list would display it. Then a simple check to see each subsequent value satisifies the condition. However, this is not a great solution, due to the O(n<sup>2</sup>) time of complexity. Which can be done more efficiently by using a Directed Acyclic Graph (DAG)

## Directed Acyclic Graph (DAG)

What is a DAG:
Wikipedia will tell you: "In mathematics, particularly graph theory, and computer science, a directed acyclic graph (DAG) is a directed graph with no directed cycles. That is, it consists of vertices and edges (also called arcs), with each edge directed from one vertex to another, such that following those directions will never form a closed loop."

![](https://upload.wikimedia.org/wikipedia/commons/f/fe/Tred-G.svg)

For our purposes we are gonig to exploit the properties of a DAG to solve the HackerX solution.
Back to the Wikipedia (What is great about it, is that for nerd stuff like this, it is always correct since no one understands it):
DAG G has three properties:
- Reachability Relation: Which is the partial order ≤ on the vertices of a DAG. In the partial order, two vertices: u and v are ordered as u ≤ v exactly where there exists a directed path from u to v in the DAG; that is, when u can reach v (or v is reachable from u). Non-tech terms: The previous vertex position, rank or value should be lower than the current vertex.
- G<sub>b</sub> Transitive Reduction: The representational DAG with the least easts that has the same reachability relation as the original DAG.  It has an edge u → v for every pair of vertices (u, v) in the covering relation of the reachability relation ≤ of the DAG. It is a subgraph of the DAG, formed by discarding the edges u → v for which the DAG also contains a longer directed path from u to v. Non-Tech Terms: Creating a new DAG that has the minimum number of edges possible while still adhering to the Reachability Relation.
- G<sub>c</sub> Transitive Closure: The representational graph with the most edges that has the same reachability relation as the DAG. It has an edge u → v for every pair of vertices (u,v) in the reachability relation ≤ of the DAG, and may therefor be thought of as a direct translation of the reachability realtion ≤. Non-Tech Terms: Creating a new DAG that has the max number of edges possible while still adhering to the Reachability Relation.
- 
![](https://files.catbox.moe/4tq6qn.jpg)

G = Original DAG
G<sub>b</sub> = Transitive Reduction
G<sub>c</sub> = Transitive Closure.
