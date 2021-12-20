# Bayesian-Inference

Bayesian network is a directed acyclic graphical representation of a set of variables and their conditional dependencies. Each variable is represented as a node in the graph and a directed edge between the nodes represents the parent-child relationship between the considered nodes. In this assignment we will estimate probability distributions or parameters of a given network. For this, we will make use of a dataset containing samples of values observed for different variables. <br/>

**Input:** 
- Line 1: n : no. of variable or nodes (N1, N2, ...., Nn) <br/>
- Line 2 to Line n + 1: Comma separated list of all possible values of variables N1 to Nn <br/>
- Line n + 2 to Line 2n + 1: n × n matrix of 1’s and 0’s representing conditional dependencies, e.g. a value 1 at location (3,2) shows that N2 is conditionally dependent on N3 <br/>
- Line 2n + 2: m : no. of samples <br/>
- Line 2n + 3 to Line 2n + 2 + m: Comma separated values observed for all variables (N1, N2, ...., Nn) for each sample. It may have some missing values denoted by ‘?’. <br/>

**Sample input:**<br/>
3 <br/>
TRUE, FALSE <br/>
TRUE, FALSE <br/>
TRUE, FALSE <br/>
0 0 1 <br/>
0 0 1 <br/>
0 0 0 <br/>
100 <br/>
TRUE, FALSE, TRUE <br/>
FALSE, TRUE, FALSE <br/>
. <br/>
. <br/>
. <br/>
. <br/>
There are three binary variables (N1, N2, N3) in this Bayesian network where N3 is conditionally dependent on N1 and N2. In other words, N1 and N2 are the parents of N3. <br/>

**Output:**<br/> 
Your program should learn the parameters (probability distributions of each variable) of the given network and return them in the following format <br/>

**Output format:**<br/>
Print n lines where Line 1 will contain probability distribution of variable N1, Line 2 will contain probability distribution of variable N2 and so on. Round off the probability value upto 4 decimal places. <br/>
For the above problem the output is <br/>
0.2 0.8 <br/>
0.4 0.6 <br/>
0.2 0.4 0.3 0.5 0.8 0.6 0.7 0.5 <br/>
This implies P(N1=TRUE) = 0.2, and P(N1=FALSE) = 0.8. Similarly P(N2=TRUE) = 0.4, and P(N2=FALSE) = 0.6. Further, P(N3=TRUE|N1=TRUE, N2=TRUE) = 0.2, P(N3=TRUE|N1=TRUE, N2=FALSE) = 0.4, P(N3=TRUE|N1=FALSE, N2=TRUE) = 0.3 and so on.


