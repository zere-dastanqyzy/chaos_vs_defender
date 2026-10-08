import numpy as np


def calculate_geometric_probability(req_duration_sec=5, time_window_sec=60):
    """
    Уровень 3: Геометрическая вероятность коллизии запросов.
    """
    if req_duration_sec >= time_window_sec:
        return {"prob_collision": 1.0}

    safe_ratio = (time_window_sec - req_duration_sec) / time_window_sec
    prob_collision = 1.0 - (safe_ratio ** 2)

    return {
        "prob_collision": prob_collision,
        "safe_ratio": safe_ratio
    }


def simulate_geometric(req_duration_sec=5, time_window_sec=60, n_sims=10000):
    t1 = np.random.uniform(0, time_window_sec, n_sims)
    t2 = np.random.uniform(0, time_window_sec, n_sims)
    collisions = np.abs(t1 - t2) < req_duration_sec
    return {"sim_prob_collision": float(np.mean(collisions))}