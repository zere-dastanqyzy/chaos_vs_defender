import numpy as np


def calculate_independence(p_fail_1, p_fail_2, common_cause_prob, is_independent):
    """
    Уровень 5: Независимые события и совместный отказ.
    """
    if is_independent:
        p_both_fail = p_fail_1 * p_fail_2
    else:
        p_both_fail = p_fail_1 * p_fail_2 + common_cause_prob * (1 - p_fail_1 * p_fail_2)
        p_both_fail = min(p_both_fail, 1.0)

    return {"p_both_fail": p_both_fail}


def simulate_independence(p_fail_1, p_fail_2, common_cause_prob, is_independent, n_sims=10000):
    if is_independent:
        s1_fail = np.random.rand(n_sims) < p_fail_1
        s2_fail = np.random.rand(n_sims) < p_fail_2
        both = s1_fail & s2_fail
    else:
        common = np.random.rand(n_sims) < common_cause_prob
        s1_fail = (np.random.rand(n_sims) < p_fail_1) | common
        s2_fail = (np.random.rand(n_sims) < p_fail_2) | common
        both = s1_fail & s2_fail

    return {"sim_p_both_fail": float(np.mean(both))}