import itertools
import numpy as np

def run():
    mu = np.array([0.12,0.10,0.08,0.07,0.06,0.05])
    Sigma = np.array([[0.10,0.02,0.01,0.00,0.00,0.00],
                      [0.02,0.09,0.02,0.01,0.00,0.00],
                      [0.01,0.02,0.08,0.02,0.01,0.00],
                      [0.00,0.01,0.02,0.07,0.02,0.01],
                      [0.00,0.00,0.01,0.02,0.06,0.02],
                      [0.00,0.00,0.00,0.01,0.02,0.05]])
    lam = 0.5
    k = 3
    def score(x):
        x = np.array(x)
        ret = mu @ x
        risk = x @ Sigma @ x
        penalty = 5.0 * (np.sum(x) - k) ** 2
        return float(ret - lam * risk - penalty), float(ret), float(risk)
    best = None
    for bits in itertools.product([0,1], repeat=6):
        sc, ret, risk = score(bits)
        if best is None or sc > best["score"]:
            best = {"score": sc, "selection": list(bits), "expected_return": ret, "risk": risk}
    return best
