#Symbolic regression
* **Selection** using tournament Selection
* Operations are the functions, add(a, b), div(a, b)...
* random selected crossover points might lead to large tree-depth,
---
1. Swap subtrees:
2. **Be careful about the mutation** it has to be the same arity
3. have a generic concept within the rules of evlution to diminish the impact of unlimitedly increase in _expression complexety_
4. Pareto optimality: Prefer simpler models with same predictuve properties
---
* initalization: parameters: max tree depth, initial population size
* weight the fitness based on the depth of a tree to prevent overfitting
----
Initializing in GP population
> two methods, Full and growth

> Growth: tree nodes are ramdomly selected from both ternimal and function sets but does not exceed the tree depth
