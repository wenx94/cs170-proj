import random
import math
import copy

def swap(wizards):
    neighbor = copy.deepcopy(wizards)
    index1 = random.randomint(0, len(wizards))
    index2 = random.randomint(0, len(wizards))
    neighbor[index1], neighbor[index2] = neighbor[index2], neighbor[index1]
    return neighbor

def cost(wizards, constraints):
    failed = 0
    for c in constraints:
        lowerBound = min(wizards.index(c[0]), c[1])
        upperBound = max(wizards.index(c[0]), c[1])
        if (lowerBound < wizards.index(c[2]) < upperBound):
            failed += 1
    return len(constraints) - failed

def acceptance_probability(old_cost, new_cost, T):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / T)

def anneal(wizards, constraints):
    random.shuffle(wizards)
    curr = wizards
    old_cost = cost(curr, constraints)
    T = 1.0
    T_min = 0.0001
    alpha = 0.90
    while T > T_min:
        i = 0
        while i < 1000:
            neighbor = swap(curr)
            new_cost = cost(neighbor, constraints)
            if new_cost == 0:
                return neighbor
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                curr = neighbor
                old_cost = new_cost
            i += 1
        T = T * alpha
    return curr


def solve(wizards, constraints, filename):
    solution = anneal(wizards, constraints)
    write_output(filename, solution)


def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))