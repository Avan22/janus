# QUBO for 6-asset selection with budget k=3, maximize mu^T x - lambda x^T Sigma x
import itertools, numpy as np
np.set_printoptions(precision=3,suppress=True)
mu = np.array([0.12,0.10,0.08,0.07,0.06,0.05])             # expected returns
Sigma = np.array([[0.10,0.02,0.01,0.00,0.00,0.00],
                  [0.02,0.09,0.02,0.01,0.00,0.00],
                  [0.01,0.02,0.08,0.02,0.01,0.00],
                  [0.00,0.01,0.02,0.07,0.02,0.01],
                  [0.00,0.00,0.01,0.02,0.06,0.02],
                  [0.00,0.00,0.00,0.01,0.02,0.05]])
lam = 0.5
k = 3
def score(x):
    x=np.array(x)
    ret = mu@x
    risk = x@Sigma@x
    penalty = 5.0*(np.sum(x)-k)**2
    return ret - lam*risk - penalty
best=None
for bits in itertools.product([0,1], repeat=6):
    sc=score(bits)
    if best is None or sc>best[0]:
        best=(sc,bits)
print("best_score", round(best[0],6))
print("selection", best[1], "sum", sum(best[1]))
sel=np.array(best[1]); print("exp_return", round(mu@sel,5), "risk", round(sel@Sigma@sel,5))
