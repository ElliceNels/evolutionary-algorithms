# MSc-Research-Notebook-EA

- **Student Names:** Ellice Nelson, Dawid Jakubowski
- **Student ID:** 23371323, 23384549
- **Proposed Research Title:** Examining the effects of dynamic versus static mutation in genetic algorithms on convergence speed and solution quality 
- **GitHub Repository Link:** https://github.com/ElliceNels/evolutionary-algorithms

------------------------------------------------------------------------

## 1. Project Overview & Evolution Track

### Current Working Research Question(s)

> *Last Updated: [17/11/2026]* \* Does adaptive mutation improve the convergence speed and solution quality of Genetic Algorithms compared to fixed mutation strageties in continuous optimization problems?

### The Pivot Log

Document any major changes in direction here. (e.g., *"Switched from quantitative survey to qualitative interviews because sample access fell through on 15/10/2026"*).

| Date | Previous Direction | New Direction | Reason for Pivot / Academic Justification |
|:-----------------|:-----------------|:-----------------|:-----------------|
|  |  |  |  |

------------------------------------------------------------------------

## 2. Critical Source Evaluation Log

Do not just copy and paste citations. For every core paper that shapes your final Introduction, document your active reading process here. Also note papers that looked promising but you decided, on review, to exclude them. Note reasons for exclusion.

### Paper 1: Mutations in GAs

- **Full IEEE/APA Citation:**
Deb, K. and Deb, D. (n.d.) ‘Analyzing Mutation Schemes for Real-Parameter Genetic Algorithms’.
- **Why did you select this paper?**
It provides a clear explanation of mutation as a single-parent variation operator and discusses how mutation maintains diversity in genetic algorithms.
- **Key Findings & Methodology:** 
In a GA, mutation operates on one chromosone and changes one or more genes to maintain diversity and enable exploration. In a binary GA, this is typically a bit flip whereas in a real-coded GA, it is usually a small numerical operation (e.g. add/subtract), commonly drawn from a Gaussian distribution.
- **Limitations/Weaknesses Identified:**
The paper explains mutation conceptually but doesn't provide a direct experimental comparison between fixed and adaptive mutation rates.
- **Direct Connection to *Your* Project:** 
This paper establishes the baseline definition of GA mutation needed for the project. 


### Paper 2: Mutations in GPs

- **Full IEEE/APA Citation:**
Burlacu, B., Yang, K., and Affenzeller, M. (2024) ‘Population diversity and inheritance in genetic programming for symbolic regression’, Natural Computing, 23(3), 531–566, available: https://doi.org/10.1007/s11047-022-09934-x.
- **Why did you select this paper?**
The paper clearly explains GP representation and describes mutation as a mechanism for maintaining diversity and avoiding premature convergence.
- **Key Findings & Methodology:**
The paper explains that GP individuals are tree-encoded. Mutation can make random changes to the tree structure, including removing subtrees, replacing subtrees or changing node types or node parameters. Its purpose is to provide genetic diversity and counteract premature convergence. This differs from a conventional GA, where mutation usually changes a gene value in a fixed-length chromosome.
- **Limitations/Weaknesses Identified:**
The paper explains GP mutation but does not directly compare fixed and adaptive mutation rates, so it is used as a definitional source rather than as evidence for the hypothesis. 
- **Direct Connection to *Your* Project:**
This paper establishes the baseline definition of GP mutation needed for the project. 

### Paper 3: Mutations in GEs

- **Full IEEE/APA Citation:**
Noorian, F., de Silva, A. M., and Bagheri, E. (2016) ‘gramEvol: Grammatical evolution in R’, Journal of Statistical Software, 71(1), 1–35.
- **Why did you select this paper?**
The paper explains how GE represents solutions and applies mutation.
- **Key Findings & Methodology:**
In GE, an individual is represented as a chromosome of binary values or codons. Mutation randomly flips individual bits with a predefined mutation probability. The mutated chromosome is then mapped through a context-free grammar to generate a program or expression. Mutation therefore changes the genotype, but its effect on the final program depends on the grammar-mapping process.
- **Limitations/Weaknesses Identified:**
The paper covers how mutations are done in GEs but doesn't provide additonal evidence for this projects hypothesis. 
- **Direct Connection to *Your* Project:**
This paper establishes the baseline definition of GE mutation needed for the project. 

### Paper 4: Fixed vs Adaptive Mutations

- **Full IEEE/APA Citation:**
Eiben, A.E., Hinterding, R., and Michalewicz, Z. (1999) ‘Parameter control in evolutionary algorithms’, IEEE Transactions on Evolutionary Computation, 3(2), 124–141, available: https://doi.org/10.1109/4235.771166.
- **Why did you select this paper?**
The paper clearly explains parameter-control strategies in evolutionary algorithms and distinguishes between fixed, deterministic, adaptive and self-adaptive mutation control, making it a good comparison of mutation strategies
- **Key Findings & Methodology:**
Fixed mutation: the mutation parameters remains constant throughout the run.
Deterministic mutation: the mutation parameters follows a preset schedule, such as decreasing as generations increase.
Adaptive mutation: the mutation parameters changes in response to search feedback, such as stagnation or low population diversity.
Self-adaptive mutation: each individual carries its own mutation parameters.
- **Limitations/Weaknesses Identified:**
The paper is a conceptual survey rather than an empirical study of mutation strategies. It does not directly compare the four mutation-control approaches on continuous optimisation benchmarks, so it should be used to establish definitions as apposed to provide evidence. 
- **Direct Connection to *Your* Project:**
This paper clearly explains all the independent variable that can be used in this research project. 

### Paper 5: Fitness based adaptive mutation

- **Full IEEE/APA Citation:**
Marsili Libelli, S. and Alba, P. (2000) ‘Adaptive mutation in genetic algorithms’, Soft Computing, 4(2), 76–80, available: https://doi.org/10.1007/s005000000042.
- **Why did you select this paper?**
It proposes a clear fitness-based adaptive mutation mechanism and directly compares it with the common approach of assigning a constant mutation probability. Therefore, it is a strong example of an adaptive mutation strategy.
- **Key Findings & Methodology:**
The paper argues that a constant mutation probability gives every chromosome the same chance of mutation, regardless of fitness. Its proposed mechanism makes mutation depend on fitness, high-fitness chromosomes are less likely to be disrupted, while low-fitness chromosomes receive higher mutation probabilities to support exploration. The authors evaluate the approach using numerical examples.
- **Limitations/Weaknesses Identified:**
The paper also does not provide a broad modern benchmark comparison or detailed analysis of convergence speed.
- **Direct Connection to *Your* Project:**
This paper is useful as an example of an adaptive mutation.

### Paper 6: Stagnation based adaptive mutation

- **Full IEEE/APA Citation:**
Kanwal, M.S., Ramesh, A.S., and Huang, L.A. (2013) ‘A novel pseudoderivative-based mutation operator for real-coded adaptive genetic algorithms’, F1000Research, 2, 139, available: https://doi.org/10.12688/f1000research.2-139.v2.
- **Why did you select this paper?**
Explains another adaptive mutation method and directly compares an adaptive mutation rate with fixed mutation rates. Therefore it is relevant to this project. 
- **Key Findings & Methodology:**
The paper proposes an adaptive mutation rate based on the derivative of fitness with respect to generations. When fitness remains unchanged across generations, the algorithm is considered to be stagnating at a local optimum, hence the mutation rate is then increased to add randomness and help the population escape. The study compares the adaptive GA against GAs using fixed mutation rates.
- **Limitations/Weaknesses Identified:**
The study is relatively small and uses a limited set of test problems, so its results may not generalise to all continuous optimisation problems.
- **Direct Connection to *Your* Project:**
This is one of the most directly relevant papers for the project because it tests adaptive mutation in a real-coded GA and reports better performance than fixed mutation rates.


### Paper 7: Two-loop Real-coded genetic algorithm with Adaptive control of Mutation Step Sizes

- **Full IEEE/APA Citation:**
Herrera, F. and Lozano, M. (2000) ‘Two-Loop Real-Coded Genetic Algorithms with Adaptive Control of Mutation Step Sizes’, Applied Intelligence, 13(3), 187–204, available: https://doi.org/10.1023/A:1026531008287.
- **Why did you select this paper?**
This paper was selected because it focuses specifically on controlling mutation step size in real-coded genetic algorithms for continuous optimisation. It is relevant to the project because it demonstrates a different adaptive mutation method that doesn't focus on mutation rate. 
- **Key Findings & Methodology:**
The paper proposes TRAMSS, a two-loop real-coded genetic algorithm that adaptively controls mutation step sizes. In a real-coded GA, solutions are represented directly as real-valued variables and mutation changes these variables by adding a numerical perturbation. The mutation step size determines how large that perturbation is, a larger step size supports exploration, while a smaller step size supports local refinement near promising solutions.
TRAMSS uses two loops with different mutation strengths. The inner loop applies smaller mutation steps to refine solutions within promising regions of the search space. The outer loop uses a restart mechanism with larger mutation steps to reinitialise the population and encourage exploration of different promising regions. The paper reports that this approach improves both reliability and accuracy compared with other mutation-step-size control methods.
- **Limitations/Weaknesses Identified:**
TRAMSS is more complex than a standard GA because it uses two loops.
- **Direct Connection to *Your* Project:**
This paper demonstrates another adaptive mutation method by showing that adaptive mutation in continuous optimisation can involve changing the mutation step size, not only the mutation probability. 

### Paper 8 — A Review on Genetic Algorithms / Katoch et al. (2021)

- **Full IEEE/APA Citation:**
Katoch, S., Chauhan, S. S., & Kumar, V. (2021). A review on genetic algorithm: Past, present, and future. Multimedia Tools and Applications, 80, 8091–8126. https://doi.org/10.1007/s11042-020-10139-6
- **Why did you select this paper?**
It provides a good breakdown on the fundamentals of genetic algorithms.
- **Key Findings & Methodology:**
This paper reviews existing research on genetic algorithms. It explains how a GA starts with a population of possible solutions, checks how good each solution is, and selects parents to produce new solutions through crossover and mutation. This process repeats over many generations. The paper also explains real-valued representations, where solutions are stored directly as numbers, making them suitable for continuous optimisation problems. It covers common selection methods, such as tournament and roulette-wheel selection, along with crossover methods that combine parents’ values and mutation methods that change those values. The authors highlight that the choice of operators and their settings affects how quickly a GA improves and how good its final solution is. They also discuss premature convergence, where the search gets stuck around a poor solution, and identify adjusting mutation and crossover during a run as an area for further research.
- **Limitations/Weaknesses Identified:**
The paper covers a wide range of GA methods and applications, so some topics are explained only briefly. It does not run its own experiments comparing adaptive and fixed mutation. The studies it reviews use different problems and settings, making their results difficult to compare directly.
- **Direct Connection to *Your* Project:**
This paper supports the background section of our project by explaining how GAs work, how numerical solutions are represented, and how selection, crossover and mutation are used in continuous optimisation. Its discussion of premature convergence and the difficulty of choosing mutation settings helps explain why we are comparing adaptive and fixed mutation. It gives us a basis for understanding how these choices could affect convergence speed and solution quality.

### Paper 2 — CEC 2005 Benchmark Functions / Suganthan et al. (2005)

- **Full IEEE/APA Citation:**
Suganthan, P. N., Hansen, N., Liang, J. J., Deb, K., Chen, Y.-P., Auger, A., & Tiwari, S. (2005). Problem definitions and evaluation criteria for the CEC 2005 special session on real-parameter optimization (Technical Report; KanGAL Report No. 2005005). Nanyang Technological University.
- **Why did you select this paper?**
We selected this report because it provides established benchmark functions and clear guidance for comparing optimisation algorithms fairly. It explains the functions and their properties, and describes how to measure convergence speed and solution quality.
- **Key Findings & Methodology:**
The report defines 25 continuous optimisation benchmark functions, including shifted versions of Sphere, Rosenbrock and Rastrigin, along with rotated, noisy and combined functions. It explains their formulas, search ranges, known optima and properties. This gives researchers a range of problems that test different difficulties, such as escaping local optima or handling interacting variables. The report also sets out a common testing procedure using 25 runs per problem, with 10, 30 and 50 variables. Each run receives a maximum of 10,000 function evaluations per variable. Solution quality is measured by the difference between the best value found and the known optimum, while convergence speed is assessed through the evaluations needed to reach a target accuracy. Researchers are asked to report averages, standard deviations, best and worst results, success rates and convergence graphs.
- **Limitations/Weaknesses Identified:**
The benchmark functions are artificial mathematical problems, so good results on them may not transfer to practical applications. The suite was published in 2005 and focuses on particular dimensions and problem types. It provides guidance for running and reporting experiments, but gives limited guidance on statistical significance testing.
- **Direct Connection to *Your* Project:**
This report helps us choose benchmark functions with different properties and explain why we selected them. Its evaluation guidelines give us a basis for comparing adaptive and fixed mutation using the same search bounds, evaluation budgets and stopping rules. Repeated runs and measures of variation will help us account for randomness. Measuring both final error and the evaluations needed to reach a target will allow us to examine solution quality and convergence speed separately.

### [Paper 2 Short Title / Author Year]

- **Full IEEE/APA Citation:**
- **Why did you select this paper?**
- **Key Findings & Methodology:**
- **Limitations/Weaknesses Identified:**
- **Direct Connection to *Your* Project:**

*(Duplicate this block as you discover new literature throughout the course)*

------------------------------------------------------------------------

## 3. Generative AI & Digital Tool Transparency Log

In line with academic integrity policies, any use of digital tools (AI search engines, LLMs, translation, or advanced editing software) to support your research process must be declared below. **Note: Using AI to write your final text from scratch is prohibited. Using tools for brainstorming, search, or copy-editing must be documented.**

| Date | Tool Used (e.g., ChatGPT, Elicit, Claude) | Task Performed (e.g., Literature search, refining a sentence, brainstorming variables) | The Exact Prompt or Input Query Used | How you critically evaluated/modified the output before using it |
|:--------------|:--------------|:--------------|:--------------|:--------------|
|  |  |  |  |  |

------------------------------------------------------------------------

## 4. Weekly Activity & Reflection Logs

### Week 01: Focus Area - Topic Selection and Literature Review

- **Activities Completed:**
- **Key Insights / Discoveries:**
- **Obstacles Encountered & How You Overcame Them:**
- **Plan for Next Week:**

### Week 02: Focus Area - [e.g., Refining the Research Question]

- **Activities Completed:**
- **Key Insights / Discoveries:**
- **Obstacles Encountered & How You Overcame Them:**
- **Plan for Next Week:**
