# Simulated Annealing

Simulated annealing is a global search method for finding global maxima in 
(un)constrained optimisation problems. It attempts to mimic the process of 
annealing in real life, which is the process of heating a material to decrease
hardness. During this process atoms in the crystal lattice migrate, and then 
recrystallise, the resulting structure can be less brittle. From a computer 
science perspective this process amounts to randomly sampling points across a 
space we are optimising in and then iteratively improving from our initial 
point by eagerly taking improvements and probabilistically taking suboptimal 
points. Gradually we reduce the probability that it takes 
suboptimal points, and eventually settle on a point that is hopefully the global 
maxima/minima in the space.

## Some Algorithmic Details

The process for simulated annealing is relatively simple. We have some function 
`f` that we are attempting to minimise, that takes as input an assignment to 
each variable we're and produces a real number associated 
with that input. Our goal is to find an assignment to these variables that 
produces the minimum (or maximum) function value. We start by selecting some 
random point (a random assignment of variables to values in their domain). Each iteration we mutate a single variable in this point to a 
random value in it's domain and compare this new point last point we had before 
mutation. If the new assignment performs better according to `f` we immediately 
adopt it, otherwise we adopt it according to a probability function. The typical probability function is the following,

![](https://quicklatex.com/cache3/25/ql_8bfc0c4b1dbe92b2bbd087cc76531325_l3.png)

Where `n` is the current input vector, `n'` is the mutated input vector and `T` 
is a temperature variable that decreases over time. As the temperature 
decreases, the fraction becomes larger and as it becomes larger the probability 
decreases (for negative inputs, as is the case if `f(n) < f(n')`). Thus the 
temperature parameter aptly performs the role of "cooling" the optimisation 
process so that the algorithm accepts fewer suboptimal mutations and instead 
focuses on finding the local maxima. The hope is that by the time this takes 
effect the initial rapid displacement will happen across the valley 
corresponding to the global maxima, so that this fine tuning process narrows in 
on the global maxima for this problem.

## Practical Example

For a practical example we are going to try writing a function to compute the 
TSP for a set of 100 cities. This is computationally infeasible for brute 
force, so hopefully we will get an idea of how simulated annealing can help us 
when exact methods fail. The code for this example is given in the repository.
Some notes about this practical example:

- The temperature decreases in a linear fashion, this is not the only way to do this I presume.
- The animation really illustrates the random displacement process "cooling" over time.
- If you download the repository and try this yourself notice that by playing around with the `max_iterations` variable you can see that allocating more time to the computation typically yields better results.
- If the temperature had started from a higher initial value (it is initially `T = 10`), then you would need longer for the optimisation process to "cool".
- The random mutation process in this case was randomly swapping the order of 
cities in the path, since we cannot independently mutate the nth city to visit in the path
whilst guaranteeing the property that the resulting walk is a cycle.

![Animated image of simulated annealing solving TSP on 100 points in the plane](simulated-annealing.gif)
