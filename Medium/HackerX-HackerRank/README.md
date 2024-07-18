# Hacker X

Evil Nation A is angry and plans to launch N guided-missiles at the peaceful Nation B in an attempt to wipe out all of Nation B’s people. Nation A’s missile i will arrive in nation B at the time ti. Missile i communicates with its headquarters by unique radio signals with a frequency equal to fi. Can you help the peaceful Nation B survive by building a defensive system that will stop the missiles dead in the sky?

## Defensive system:

The only way to defend Nation B from the attacking missile is by counter attacking them with a hackerX missile. You have a lot of hackerX missiles and each one of them has its own radio frequency. An individual hackerX missile can destroy Evil Nation A’s attacking missile if the radio frequency of both of the missiles match. Each hackerX missile can be used an indefinite number of times. Its invincible and doesn’t get destroyed in the collision.

The good news is you can adjust the frequency of the hackerX missile to match the evil missiles’ frequency. When changing the hackerX missile’s initial frequency `fA` to the new defending frequency `fB`, you will need `|fB - fA|` units of time to do.

What is the minimum number of hackerX missiles you must launch to keep Nation B safe?

## Input Format:
The first line contains a single integer N denoting the number of missiles. 
This is followed by N lines each containing two integers ti and fi denoting the time & frequency of the ith missile.

## Output Format:
A single integer denoting the minimum number of hackerX’s you need to defend the nation.

## Constraints:
```
1 ≤ N ≤ 100000
0 ≤ ti ≤ 100000
0 ≤ fi ≤ 100000
t1 ≤ t2 ≤ … ≤ tN
```

## Sample Input:

```
4
1 1
2 2
3 1
5 1
```

## Sample Output:

```
1
```

## Explanation:

A HackerX missile is launched at t = 1 with a frequency f = 1, and destroys the first missile. It re-tunes its frequency to f = 2 in 1 unit of time, and destroys the missile that is going to hit Nation B at t = 2. It re-tunes its frequency back to 1 in 1 unit of time and destroys the missile that is going to hit the nation at t = 3. It is relaunched at t = 5 with f = 1 and destroys the missile that is going to hit nation B at t = 5. Hence, you need only 1 HackerX to protect nation B.

## Sample Input:

```
4
1 1
2 3
3 1
5 1
```

## Sample Output:

```
2
```

## Explanation:

Destroy 1 missile at t = 1, f = 1, now at t = 2, there is a missile with frequency 3. The launched missile takes 2 units of time to destroy this, hence we need a new hackerX missile to destroy this one. The first hackerX missile can destroy the 3rd missile which has the same frequency as itself. The same hackerX missile destroys the missile that is hitting its city at t = 5. Thus, we need atleast 2 hackerX missiles.

# Solution Explanation

## Miminum Path Cover Problem

Ultimately this is known as a Miminum path cover problem.
A path cover is a directed graph G=(V,E) is a set P of vertex-disjointed paths such that every vertex in V is included in exactly one path in P. Paths may start and end anywhere, and they may be of any length, including 0. A minimum path cover of G is a path cover conatining the fewest possible points

Given an efficient algorithm to find a minimum path cover of a directed acyclic graph G=(V,E). Assuming that V = {1,2,...,n} number of vertices/nodes and E = {0,1,2 ... n-1} edges, construct the graph G'=(V',E'), where :
```
V′​={ x<sub>0​,</sub>, x<sub>1</sub>​, … , x<sub>n</sub> ​} ∪ { y<sub>0</sub>​, y<sub>1​</sub>, … , y<sub>n</sub> ​},

E′={ ( x<sub>0​</sub>, x<sub>i</sub>​ ) : i ∈ V } ∪ { ( y<sub>i</sub>​, y<sub>0</sub> ​) : i ∈ V } ∪ { ( x<sub>i​</sub>, y<sub>j</sub>​ ) : (i,j) ∈ E },​
```

And run a maximum-flow algorithm.

Source: https://walkccc.me/CLRS/Chap26/Problems/26-2/

## Explanation of the Problem

Given two missiles i and j, where as T<sub>j</sub> >= T<sub>i</sub> (missiles sorted via time of T)

A single hackerX missile can be used to stop both i and j if the difference in frequence between them is less than or equal to the amount of time between their arrivals. In the HackerX problem ratio of frequency change vs time required is 1:1 (A change of 1 in frequency F, requires 1 unit of time T). This can be mathematically described as with the following condition:
```
T<sub>j</sub> - T<sub>i</sub> >= |F<sub>j</sub> - F<sub>i</sub>| 
```

## An O(n<sup>2</sup>) Solution

For now, For simplicity sake, lets make the assumption:
```
F<sub>i</sub> > F<sub>j</sub>
```
To remove the absolute value, reducing the condition to:
```
T<sub>j</sub> - T<sub>i</sub> >= F<sub>i</sub> - F<sub>j</sub>
```
Next, add F<sub>j</sub> to both sides, transforming the condition to:
```
T<sub>j</sub> - T<sub>i</sub> + F<sub>j</sub> >= F<sub>i</sub>
```
Lastly, add T<sub>i</sub> to both sides, transforming the condition to:
```
T<sub>j</sub> + F<sub>j</sub> >= T<sub>i</sub> + F<sub>i</sub>
```

It is stated that we need at least one HackerX missile to cover the first missile. The question after, is how many other missiles can the first missile cover. To find this out, a linear scan through the list would display it. Then a simple check to see each subsequent value satisifies the condition. However, this is not a great solution, due to the O(n<sup>2</sup>) time of complexity. Which can be done more efficiently by using a Directed Acyclic Graph (DAG).

## Directed Acyclic Graph (DAG)

What is a DAG:
Wikipedia will tell you: "In mathematics, particularly graph theory, and computer science, a directed acyclic graph (DAG) is a directed graph with no directed cycles. That is, it consists of vertices and edges (also called arcs), with each edge directed from one vertex to another, such that following those directions will never form a closed loop."

![Wikepedia](https://upload.wikimedia.org/wikipedia/commons/f/fe/Tred-G.svg)

A good example of a DAG in action: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8821727/

### Time to add some DAG. nLogn! nLogn!

For our purposes we are gonig to exploit the properties of a DAG to solve the HackerX solution.
Back to the Wikipedia (What is great about it, is that for nerd stuff like this, it is always correct since no one understands it):
DAG G has three properties:
- Reachability Relation: Which is the partial order ≤ (conditional statement) on the vertices of a DAG. In the partial order, two vertices: u and v are ordered as u ≤ v exactly where there exists a directed path from u to v in the DAG; that is, when u can reach v (or v is reachable from u). Non-tech terms: The previous vertex position, rank or value should be lower than the current vertex.
- G<sub>b</sub> Transitive Reduction: The representational DAG with the least edges that has the same reachability relation as the original DAG.  It has an edge u → v for every pair of vertices (u, v) in the covering relation of the reachability relation ≤ of the DAG. It is a subgraph of the DAG, formed by discarding the edges u → v for which the DAG also contains a longer directed path from u to v. Non-Tech Terms: Creating a new DAG that has the minimum number of edges possible while still adhering to the Reachability Relation.
- G<sub>c</sub> Transitive Closure: The representational graph with the most edges that has the same reachability relation as the DAG. It has an edge u → v for every pair of vertices (u,v) in the reachability relation ≤ of the DAG, and may therefor be thought of as a direct translation of the reachability realtion ≤. Non-Tech Terms: Creating a new DAG that has the max number of edges possible while still adhering to the Reachability Relation.


![](https://files.catbox.moe/4tq6qn.jpg)

G = Original DAG
G<sub>b</sub> = Transitive Reduction
G<sub>c</sub> = Transitive Closure.

So how does that relate to the Hacker X problem?

Well lets take a sample set of couples and create a DAG out of it:
[(65,844),(70,993),(201,427),(348,899),(388,268),(440,416),(459,421),(459,796),(744,291),(870,121)]
```
G=(V,E)

V = T = Time

E = F = Frequency

dT = delta Time = Change in time between the previous time and the current time.

dF = delta Frequency = Change in frequency between the previous time and the current time.
```
∑<sup>n</sup><sub>G=1</sub> = [(65,844),(70,993),(201,427),(348,899),(388,268),(440,416),(459,421),(459,796),(744,291),(870,121)]

### Stipulations:

- According to the problem we need the to check if a specific object requires a new missile base on dT and dF to each other. 
- And according to the problem, the delta change ration is 1:1, 1 unit of time is required for 1 unit of frequency shift the the oncomming objects. If a missile requires more than more frequency units than the alloted time between missiles, then a new missile will take its place.
- Once a missile is in the air, it can relock onto any frequency that is one more or less than its current frequency vs time in regards subsequent objects after new missiles are fired. So three objects come in, (1,4),(2,6),(3,3). The second object requires a new missile since time only shifted one but frequency shifted by 2. However, the third object can be hit by the first missile since there is more time alloted between the first and third than frequency increase. This is our Reachability Relation.
- Now since we are looking for all possible missiles needed, our best approach is a Transitive Reduction, removing entries that don't require new missiles, and at the end, count the number of vertices in the resulting culled set.

So we build our DAG on this by first order our couples set by the time (in case it is not sorted already). Next we take the sum and difference between Time vs Frequency and generate a list: 
```
Original Set              Transitive Set.
  (a, b)                      (x, y)
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
```
This allows us to compare a single value instead of two since we will only care about the difference value, y
Why? The difference still represets the points x and y due to the mathematical associative rule of Addition:
```
Given vertex points
(x<sub>a</sub>,y<sub>a</sub>)
(x<sub>b</sub>,y<sub>b</sub>)

The Associative Property in action:
x<sub>a</sub> - y<sub>a</sub> = z<sub>a</sub>
x<sub>b</sub> - y<sub>b</sub> = z<sub>b</sub

x<sub>b</sub> - x<sub>a</sub> = dx<sub>a</sub>
y<sub>b</sub> - y<sub>a</sub> = dy<sub>a</sub>

z<sub>b</sub>   - z<sub>a</sub>   = dz<sub>a</sub>
dy<sub>a</sub>  - dx<sub>a</sub>  = dz<sub>a</sub>
```
So if we check the difference between the vertex points or the x-y difference we end up in the same result. Since using a single number comparison is simpler than a tuple comparison, gonig with the x-y difference solution, is much more efficient. 

At this point, all we really care about is the differce on Time vs Frequency, due to our Reeachability Relation, as Frequency is dependant on time.
[-226, 120, 24,38, -779, 749, 453, -923, -551, -337]

There we iterate through the the positions, checking through through one loop through every element in the set, O(n) and then have it go through another loop only comparing through the set only if specific conditions is met, and if the specific condition is no longer met during the search, the code will move on to the next set item for its own iterations, reducing n number of left over iterations, where the iterations could be from n to under n<sup>2</sup> number of iterations, O(logn). Since O(logn) is dependent on the O(n) portion, the final complexity is O(nlogn), one step down from O(n<sup>2</sup>).


x<sub>a</sub> - y<sub>a</sub> = z<sub>a</sub>
x<sub>b</sub> - y<sub>b</sub> = z<sub>b</sub>

z<sub>b</sub> - z<sub>a</sub> = dz<sub>a</sub>

x<sub>b</sub> - x<sub>a</sub> - dx<sub>a</sub>
y<sub>b</sub> - y<sub>a</sub> - dy<sub>a</sub>

dy<sub>a</sub> - dx<sub>a</sub> = dz<sub>a</sub>

10 5

10-5 = 5

15 7

15-7 = 8

5-8 = -3
5

15 -10 = 5
7-5 = 2
2-5 = -3
-7 - -5 