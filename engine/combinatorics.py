from scipy.special import comb
import numpy as np


def calculate_combinatorics(total_servers=10, chaos_pick=3, defender_pick=3):
    """
    Уровень 2: Элементы комбинаторики C(n, k).
    """
    total_combinations = comb(total_servers, chaos_pick, exact=True)

    if total_servers - chaos_pick >= defender_pick:
        no_overlap = comb(total_servers - chaos_pick, defender_pick, exact=True)
    else:
        no_overlap = 0

    prob_no_overlap = no_overlap / total_combinations
    prob_at_least_one_overlap = 1.0 - prob_no_overlap

    return {
        "total_combinations": total_combinations,
        "no_overlap_combinations": no_overlap,
        "prob_overlap": prob_at_least_one_overlap
    }


def simulate_combinatorics(total_servers=10, chaos_pick=3, defender_pick=3, n_sims=10000):
    overlaps = 0
    servers = np.arange(total_servers)
    for _ in range(n_sims):
        c_pick = set(np.random.choice(servers, chaos_pick, replace=False))
        d_pick = set(np.random.choice(servers, defender_pick, replace=False))
        if len(c_pick.intersection(d_pick)) > 0:
            overlaps += 1
    return {"sim_prob_overlap": overlaps / n_sims}