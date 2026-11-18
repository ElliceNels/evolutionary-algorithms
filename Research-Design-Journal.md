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

### Paper 9 — CEC 2005 Benchmark Functions / Suganthan et al. (2005)

- **Full IEEE/APA Citation:**
Suganthan, P. N., Hansen, N., Liang, J. J., Deb, K., Chen, Y.-P., Auger, A., & Tiwari, S. (2005). Problem definitions and evaluation criteria for the CEC 2005 special session on real-parameter optimization (Technical Report; KanGAL Report No. 2005005). Nanyang Technological University.
- **Why did you select this paper?**
We selected this report because it provides established benchmark functions and clear guidance for comparing optimisation algorithms fairly. It explains the functions and their properties, and describes how to measure convergence speed and solution quality.
- **Key Findings & Methodology:**
The report defines 25 continuous optimisation benchmark functions, including shifted versions of Sphere, Rosenbrock and Rastrigin, along with rotated, noisy and combined functions. It explains their formulas, search ranges, known optima and properties. This gives researchers a range of problems that test different difficulties, such as escaping local optima or handling interacting variables. The report also sets out a common testing procedure using 25 runs per problem, with 10, 30 and 50 variables. Each run receives a maximum of 10,000 function evaluations per variable. Solution quality is measured by the difference between the best value found and the known optimum, while convergence speed is assessed through the evaluations needed to reach a target accuracy. Researchers are asked to report averages, standard deviations, best and worst results, success rates and convergence graphs.
- **Limitations/Weaknesses Identified:**
The benchmark functions are artificial mathematical problems, so good results on them may not transfer to practical applications. The suite was published in 2005 and focuses on particular dimensions and problem types. It provides guidance for running and reporting experiments, but gives limited guidance on statistical significance testing.
- **Direct Connection to *Your* Project:**
This report helps us choose benchmark functions with different properties and explain why we selected them. Its evaluation guidelines give us a basis for comparing adaptive and fixed mutation using the same search bounds, evaluation budgets and stopping rules. Repeated runs and measures of variation will help us account for randomness. Measuring both final error and the evaluations needed to reach a target will allow us to examine solution quality and convergence speed separately. These benchmarks are all available in the Python library opfunu.

### Paper 10: Population diversity

- **Full IEEE/APA Citation:**
Liu, K., Teng, Y., and Liu, F. (2025) ‘A study of gene expression programming algorithm for dynamically adjusting the parameters of genetic operators’, PLOS One, 20(6), e0321711, available: https://doi.org/10.1371/journal.pone.0321711.
- **Why did you select this paper?**
Provides a clear definiton of population diversity and how it is beneficial
- **Key Findings & Methodology:**
"Population diversity measures the degree of variation among individuals in a population and is critical for maintaining the global search capability of the algorithm. A higher diversity means that the population contains more varied solutions, thereby increasing the probability of finding the global optimum." 
- **Direct Connection to *Your* Project:**
Paper provides a clear definition of population diversity and encourages higher population diversity which can be achieved through mutations

### Paper 11: Exploration vs. Exploitation

- **Full IEEE/APA Citation:**
Črepinšek, M., Liu, S.-H., and Mernik, M. (2013) ‘Exploration and exploitation in evolutionary algorithms: A survey’, ACM Computing Surveys (CSUR), 45(3), 35:1-35:33, available: https://doi.org/10.1145/2480741.2480752.
- **Why did you select this paper?**
Provides a clear definition of exploration and exploitation and the importance of both
- **Key Findings & Methodology:**
"Exploration is the process of visiting entirely new regions of a search space,
whilst exploitation is the process of visiting those regions of a search space within
the neighborhood of previously visited points. In order to be successful, a search algorithm needs to establish a good ratio between exploration and exploitation."
- **Direct Connection to *Your* Project:**
Provides baseline definition of exploration and exploitation

### Paper 12: Quantum-Inspired Evolutionary Algorithm / Talbi & Draa (2017)

- **Full IEEE/APA Citation:**
Talbi, H., & Draa, A. (2017). A new real-coded quantum-inspired evolutionary algorithm for continuous optimization. Applied Soft Computing, 61, 765–791. https://doi.org/10.1016/j.asoc.2017.07.046
- **Why did you select this paper?**
We selected this paper as an example of how researchers test continuous optimisation algorithms. It shows how benchmark functions, evaluation budgets, target accuracy and statistical tests can be used to compare performance.
- **Key Findings & Methodology:**
The authors combine quantum-inspired evolutionary search with local search and gradually narrow the search region around promising solutions. They test three versions using different local-search methods and select the trust-region version for comparison with 14 other algorithms. They use the Black-Box Optimization Benchmarking (BBOB) collection through the COmparing Continuous Optimisers (COCO) platform, testing 24 functions with 2, 3, 5, 10 and 20 variables and 15 instances of each function at each dimension. Each run receives a maximum of 10,000 function evaluations per variable. Performance is measured using the evaluations needed to reach target solution values, success rates and expected running time, which accounts for unsuccessful runs. The authors also use rank-sum significance tests and corrections for multiple comparisons. Their method performs competitively overall, although its results depend on the function and dimension.
- **Limitations/Weaknesses Identified:**
The proposed algorithm combines several methods, making it difficult to identify which component is responsible for improvements. It also has many parameters, and the authors acknowledge that suitable settings can differ between function categories. Testing focuses on mathematical benchmarks, with noisy functions and practical applications left for future work. The experiments provide limited direct evidence about adaptive versus fixed mutation in GAs.
- **Direct Connection to *Your* Project:**
- This paper gives us an example of evaluating convergence speed and solution quality across different benchmark problems. It supports using equal evaluation budgets, reporting success rates and measuring how many evaluations are needed to reach a target accuracy. It also shows why unsuccessful runs should be included when judging performance. Its experimental approach can help us design a fair comparison between adaptive and fixed mutation.

### Paper 13: Evolutionary Programming for Continuous Optimisation / Yang et al. (2006)

- **Full IEEE/APA Citation:**
Yang, Y. W., Xu, J. F., & Soh, C. K. (2006). An evolutionary programming algorithm for continuous global optimization. European Journal of Operational Research, 168(2), 354–369. https://doi.org/10.1016/j.ejor.2004.05.007
- **Why did you select this paper?**
We selected this paper because it shows how benchmark functions can be used to assess convergence speed and solution quality. It also investigates the contribution of individual operators, making it useful for planning a controlled comparison in our project.
- **Key Findings & Methodology:**
The authors develop an evolutionary programming algorithm that combines large random mutations, local search and crossover. Large mutations explore the search space, while local search improves nearby solutions. They also use simulated annealing during selection to reduce the chance of getting stuck too early. The algorithm is tested on 12 benchmark problems, including Sphere, Rosenbrock and Rastrigin. The authors compare its results with earlier studies and then compare versions with different operators enabled. These operator experiments use 20 independent runs per problem and measure mean best fitness against the number of function evaluations, including evaluations spent on local search. The combined method performs well on many problems, but the results show that an operator’s usefulness depends on the problem’s characteristics. For example, local search improves performance on several problems but adds a cost that outweighs its benefits on some smaller problems.
- **Limitations/Weaknesses Identified:**
The main algorithm combines several techniques, so improvements in its overall performance cannot be attributed to mutation alone. Some comparisons use results reported in earlier papers, and the authors acknowledge estimating some values from published graphs. Although they discuss statistically significant differences, the statistical procedures receive limited explanation. The paper also provides no direct comparison of adaptive and fixed mutation within a GA.
- **Direct Connection to *Your* Project:**
The benchmark descriptions help us explain why different functions test different search difficulties. The operator comparisons also support keeping the rest of our GA consistent when changing the mutation strategy, so we can better identify its effect. Measuring progress against function evaluations gives us a way to compare convergence speed while accounting for computational work. The mixed results across problems reinforce the need to test whether adaptive mutation’s benefits depend on the function being optimised.

### Paper 14 — Average Convergence Rate / Chen & He (2021)

- **Full IEEE/APA Citation:**
Chen, Y., & He, J. (2021). Average convergence rate of evolutionary algorithms in continuous optimization. Information Sciences, 562, 200–219. https://doi.org/10.1016/j.ins.2020.12.076
- **Why did you select this paper?**
We selected this paper because it explains how convergence speed can be measured and investigates how adapting mutation affects convergence. It does a comparison of adaptive and fixed mutation step sizes.
- **Key Findings & Methodology:**
The authors study average convergence rate, which measures how quickly the error between the best solution found and the known optimum decreases over generations. They combine mathematical analysis with computer experiments. One experiment compares fixed and adaptive Gaussian mutation step sizes on the two-variable Sphere function. Each algorithm runs independently 1,000 times for 300 generations. The algorithm keeps one candidate, creates one mutated offspring and retains whichever is better. The adaptive version changes its mutation step size according to the current solution’s coordinates and converges faster than the fixed-step version in this experiment. The wider analysis shows that adaptation’s benefits depend on how it is designed and on the problem being solved. It also shows that increasing the number of variables can slow convergence considerably on difficult problems.
- **Limitations/Weaknesses Identified:**
The main mutation comparison uses a simple evolutionary programming algorithm with one parent and one offspring. Its behaviour may differ from a population-based GA that also uses crossover. The Sphere experiment uses a step-size rule suited to an optimum at zero, so its success may not transfer directly to other functions. The theoretical results depend on specific mathematical assumptions. The paper mainly investigates convergence speed and gives limited evidence about final solution quality under a common evaluation budget.
- **Direct Connection to *Your* Project:**
This paper gives us a way to explain and measure convergence speed and provides evidence that adapting mutation step size can improve progress in a continuous optimisation problem. It also helps us question whether those benefits hold across different functions and dimensions. Our experiments can investigate this within a GA while measuring both convergence speed and final solution quality. We should clearly distinguish changing mutation step size from changing mutation probability when discussing its relevance.

### [Paper 2 Short Title / Author Year]

- **Full IEEE/APA Citation:**
- **Why did you select this paper?**
- **Key Findings & Methodology:**
- **Limitations/Weaknesses Identified:**
- **Direct Connection to *Your* Project:**

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
