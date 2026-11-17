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

### [Paper 1: Mutations in GAs]

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


### [Paper 2: Mutations in GPs]

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

### [Paper 3: Mutations in GEs]

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
