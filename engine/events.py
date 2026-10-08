import numpy as np


def calculate_event_probabilities(chaos_pattern: list[int], defender_mask: list[int]):
    """
    Уровень 1: Алгебра событий. 4 сервера -> 2^4 = 16 исходов.
    """
    omega_size = 16
    event_A = set()
    event_B = set()

    for i in range(16):
        state = [(i >> bit) & 1 for bit in range(4)]
        if any(state[j] == 1 and chaos_pattern[j] == 1 for j in range(4)):
            event_A.add(i)
        if all(state[j] == 0 or defender_mask[j] == 1 for j in range(4)):
            event_B.add(i)

    p_A = len(event_A) / omega_size
    p_B = len(event_B) / omega_size
    p_union = len(event_A.union(event_B)) / omega_size
    p_intersect = len(event_A.intersection(event_B)) / omega_size
    p_not_A = 1.0 - p_A

    return {
        "p_A": p_A,
        "p_B": p_B,
        "p_union": p_union,
        "p_intersect": p_intersect,
        "p_not_A": p_not_A,
        "size_A": len(event_A),
        "size_B": len(event_B)
    }


def simulate_events(chaos_pattern, defender_mask, n_sims=10000):
    omega = np.random.randint(0, 2, size=(n_sims, 4))
    chaos_hit = np.any((omega == 1) & (np.array(chaos_pattern) == 1), axis=1)
    defender_safe = np.all((omega == 0) | (np.array(defender_mask) == 1), axis=1)

    return {
        "sim_p_A": float(np.mean(chaos_hit)),
        "sim_p_B": float(np.mean(defender_safe)),
        "sim_p_intersect": float(np.mean(chaos_hit & defender_safe))
    }