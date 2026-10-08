import numpy as np


def calculate_bayes(traffic_shares: list[float], failure_rates: list[float]):
    """
    Уровень 4: Условная вероятность и формула Байеса.
    """
    P_S = np.array(traffic_shares) / np.sum(traffic_shares)
    P_F_given_S = np.array(failure_rates)

    P_Total_Failure = np.sum(P_S * P_F_given_S)

    if P_Total_Failure == 0:
        P_S_given_F = np.zeros_like(P_S)
    else:
        P_S_given_F = (P_S * P_F_given_S) / P_Total_Failure

    return {
        "p_total_failure": P_Total_Failure,
        "posterior_probs": P_S_given_F.tolist()
    }