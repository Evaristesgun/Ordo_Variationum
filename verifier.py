#!/usr/bin/env python
# coding: utf-8

# - `verify(roots)`: `roots` is an iterable of distinct positive integers. Return `None` if their squares are Sidon. Otherwise return `((a, b), (c, d))` with $a < b$, $c < d$ and $a^2 + b^2 = c^2 + d^2$. Scan pairs in this order: sort the roots, then for each $a$ take each $b > a$ in sorted order. At the first repeated sum, return the earlier pair and then the current pair. Raise `ValueError` on a duplicate or non-positive root.
# - `collision_type(p, q)`: return `"self-pair"` or `"four distinct"`.
# - `largest_sidon(N)`: return `(F(N), roots)`, where `roots` is one optimal subset of $\{1, \dots, N\}$.


import numpy as np

def verify(roots):
    roots = np.asarray(list(roots))
    l = roots.size
    if l < 2: # non-empty
        return None
    if l != np.unique(roots).size or np.any(roots <= 0):
        raise ValueError("No duplicate or non-positive root")
    r = np.sort(roots)
    d = {}
    for i in range(l):
        for j in range(i, l):
            n = r[i]**2 + r[j]**2
            if n in d:
                return (d[n], (r[i], r[j]))
            else:
                d[n] = (r[i], r[j])

def collision_type(p, q):
    if p[0] == p[1] or q[0] == q[1]:
        return "self-pair"
    else:
        return "four distinct"

def largest_sidon(N):
    B = []
    D = set() # possible square sums
    S = [] # The selected element

    def track(r):
        nonlocal B
        l = len(S)
        if l + N-r+1 <= len(B):
            return # Prune
        if r > N:
            B = S.copy()
            return 
        
        # left node of the tree
        notin = True
        for i in range(l):
            if r**2 + S[i]**2 in D:
                notin = False
                break
        if notin:
            S.append(r)
            # We already include 2r^2 in new
            new = [r**2 + s**2 for s in S] # We look through the already-selected Sidon set
            D.update(new)
            track(r+1)
            D.difference_update(new)
            S.pop()
            
        # right node of the tree
        track(r+1)
    track(1)
    return (len(B), B)



