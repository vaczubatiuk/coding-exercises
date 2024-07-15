# HackerX Problem

## Miminum Path Cover Problem
Ultimately this is knowin as a Miminum path covered problem.
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

Next, add F<sub>j</sub> to both sides, transforming the condition to:

- T<sub>j</sub> - T<sub>i</sub> + F<sub>j</sub> >= F<sub>i</sub>

Lastly, add T<sub>i</sub> to both sides, transforming the condition to:

- T<sub>j</sub> + F<sub>j</sub> >= T<sub>i</sub> + F<sub>i</sub>


It is stated that we need at least one HackerX missile to cover the first missile. The question after, is how many other missiles can the first missile cover. To find this out, a linear scan through the list would display it. Then a simple check to see each subsequent value satisifies the condition. However, this is not a great solution, due to the O(n<sup>2</sup>) time of complexity. Which can be done more efficiently by using a Directed Acyclic Graph (DAG).

## Directed Acyclic Graph (DAG)

What is a DAG:
Wikipedia will tell you: "In mathematics, particularly graph theory, and computer science, a directed acyclic graph (DAG) is a directed graph with no directed cycles. That is, it consists of vertices and edges (also called arcs), with each edge directed from one vertex to another, such that following those directions will never form a closed loop."

![](https://upload.wikimedia.org/wikipedia/commons/f/fe/Tred-G.svg)

### Time to add some DAG. nLogn! nLogn!

For our purposes we are gonig to exploit the properties of a DAG to solve the HackerX solution.
Back to the Wikipedia (What is great about it, is that for nerd stuff like this, it is always correct since no one understands it):
DAG G has three properties:
- Reachability Relation: Which is the partial order ≤ on the vertices of a DAG. In the partial order, two vertices: u and v are ordered as u ≤ v exactly where there exists a directed path from u to v in the DAG; that is, when u can reach v (or v is reachable from u). Non-tech terms: The previous vertex position, rank or value should be lower than the current vertex.
- G<sub>b</sub> Transitive Reduction: The representational DAG with the least edges that has the same reachability relation as the original DAG.  It has an edge u → v for every pair of vertices (u, v) in the covering relation of the reachability relation ≤ of the DAG. It is a subgraph of the DAG, formed by discarding the edges u → v for which the DAG also contains a longer directed path from u to v. Non-Tech Terms: Creating a new DAG that has the minimum number of edges possible while still adhering to the Reachability Relation.
- G<sub>c</sub> Transitive Closure: The representational graph with the most edges that has the same reachability relation as the DAG. It has an edge u → v for every pair of vertices (u,v) in the reachability relation ≤ of the DAG, and may therefor be thought of as a direct translation of the reachability realtion ≤. Non-Tech Terms: Creating a new DAG that has the max number of edges possible while still adhering to the Reachability Relation.


![](https://files.catbox.moe/4tq6qn.jpg)

G = Original DAG
G<sub>b</sub> = Transitive Reduction
G<sub>c</sub> = Transitive Closure.

So how does that relate to the Hacker X problem?

Well lets take a sample set of couples and create a DAG out of it:
[(65,844),(70,993),(201,427),(348,899),(388,268),(440,416),(459,421),(459,796),(744,291),(870,121)]
G=(V,E)
V = T = Time
E = F = Frequency
∑<sup>n</sup><sub>G=1</sub> = [(65,844),(70,993),(201,427),(348,899),(388,268),(440,416),(459,421),(459,796),(744,291),(870,121)]

### Stipulations:

- According to the problem we need the to check if a specific object requires a new missile base on dT and dF to each other. 
- And according to the problem, the delta change ration is 1:1, 1 unit of time is required for 1 unit of frequency shift the the oncomming objects. If a missile requires more than more frequency units than the alloted time between missiles, then a new missile will take its place.
- Once a missile is in the air, it can relock onto any frequency that is one more or less than its current frequency vs time in regards subsequent objects after new missiles are fired. So three objects come in, (1,1),(2,3),(3,2). The second object requires a new missile since time only shifted one but frequency shifted by 2. However, the third object can be hit by the first missile since there is more time alloted between the first and third than frequency increase. This is our Reachability Relation.
- Now since we are looking for all possible missiles needed, our best approach is a Transitive Reduction, removing entries that don't require new missiles, and at the end, count the number of vertices in the resulting culled set.

So we build our DAG on this by first order our couples set by the time (in case it is not sorted already). Next we take the sum and difference between Time vs Frequency and generate a list: 
Original Set              Transitive Set.
(65, 844)	  =>(a+b,a-b)=>	(628, -226)
(70, 993)	  =>(a+b,a-b)=>	(656, 120)
(201, 427)	=>(a+b,a-b)=>	(856, 24)
(348, 899)	=>(a+b,a-b)=>	(880, 38)
(388, 268)	=>(a+b,a-b)=>	(909, -779)
(440, 416)	=>(a+b,a-b)=>	(991, 749)
(459, 421)	=>(a+b,a-b)=>	(1035, 453)
(459, 796)	=>(a+b,a-b)=>	(1063, -923)
(744, 291)	=>(a+b,a-b)=>	(1247, -551)
(870, 121)	=>(a+b,a-b)=>	(1255, -337)

At this point, all we really care about is the differce on Time vs Frequency, due to our Reeachability Relation, as Frequency is dependant on time.
[-226, 120, 24,38, -779, 749, 453, -923, -551, -337]

There we iterate through the the positions, checking through through one loop (Through every element in the set, O(n) and then have it go through another loop only comparing through the set only if specific conditions is met, and if the specific condition is no longer met during the search, the code will move on to the next set item for its own iterations, reducing n number of left over iterations, where the iterations could n to n<sup>2</sup>, O(logn). Since O(logn) is dependent on the O(n) portion, the final complexity is O(nlogn), one step down from O(n<sup>2</sup>).


