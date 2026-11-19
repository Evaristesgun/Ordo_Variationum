# Variatio

**Which mathematical variants are worth exploring first?**

Suppose a language model has an afternoon to look for a large Sidon set of squares. It could spend the whole time on the target problem, or it could work through simpler variants and leave notes for a second attempt. Variatio asks which choice helps most. The test is what a fresh session of the same model can construct on an unseen instance using those notes.

The project is at the design stage. The first milestone is a verifier that can explain why a proposed set fails.

## The first case study

Choose roots from $1,\ldots,N$ and square them. The resulting set is *Sidon* if every unordered pair of its elements has a different sum. An element may be paired with itself. If $F(N)$ is the largest possible size of such a set, Erdős Problem 773 asks whether

$$
F(N)=N^{1-o(1)}.
$$

The experiment studies finite instances. Every valid construction gives a lower bound that a short program can check. Published values for small instances provide independent checks on that program. [Erdős Problem 773](https://www.erdosproblems.com/773) · [OEIS A390813](https://oeis.org/A390813)

Consider a variant that checks only pairs of *distinct* roots. The roots $\{1,5,7\}$ pass that test. Restoring the original condition exposes a collision at 50.

$$
1^2+7^2=5^2+5^2=50.
$$

That example gives a future solver a specific check. When adding a root $r$, compare $2r^2$ against the sums already present. A different collision, $1^2+8^2=4^2+7^2$, involves four distinct roots. Is a note about each kind of failure more useful than two more worked examples of the same kind? That is a question the experiment can answer.

## The experiment

Each strategy gets the same exploration budget and the same space for notes. The three variant-selection strategies choose the same number of problems from a common pool.

| Strategy | How it spends the exploration budget |
| --- | --- |
| Direct search | Work on small instances of the original problem and record what helps. |
| Random selection | Draw variants uniformly at random and explore them. |
| Easiest first | Choose the variants rated most tractable before exploration. |
| Complementary variants | Prefer tractable variants with an explicit connection to the target, giving priority to obstacles that earlier selections have yet to cover. |

Each note records what changed in the problem, what was tried, what evidence can be independently checked, and when the observation applies. A failed construction can earn its place by identifying an exact collision.

## What counts as success?

Before the main runs, we will fix the test instances, prompts, model version, token limits and search runtime. Each evaluation starts in a fresh session with the notes from one strategy. Two test sets measure different kinds of transfer. One increases $N$. The other changes which roots may be used.

The primary comparison is **complementary variants versus random selection**. On each instance, the score is the size of the largest verified set submitted within budget, or zero if every submission fails. We will average repeated runs within each instance and report paired differences separately for the two test sets. The direct-search comparison asks whether exploring variants was worth the time at all.

We will also rerun the evaluation after removing counterexamples from the notes. Tracking both validity and set size lets us see whether a warning prevents an invalid submission while leaving the size of valid constructions unchanged.

## First milestone

1. Write a verifier that either accepts a root set or returns two different pairs with the same square sum.
2. Check it against exhaustive search at $N=6$ and $N=7$. Both optima are 6, and among the first seven squares the only collision is the one at 50.
3. Pilot the four strategies on development instances. Use the pilot to set the budget, then freeze a separate test set for the main comparison.

