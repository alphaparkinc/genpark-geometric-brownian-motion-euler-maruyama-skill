"""Euler-Maruyama & Milstein SDE Solvers.
100% Python Standard Library.
"""

import math
import random

class SDESolver:
    """Numerical discretization schemes for Itô stochastic differential equations."""
    @staticmethod
    def simulate_gbm_euler(s0, mu, sigma, t_max, steps, seed=42):
        rng = random.Random(seed)
        dt = t_max / steps
        sqrt_dt = math.sqrt(dt)
        path = [s0]
        s = s0
        for _ in range(steps):
            dw = rng.gauss(0.0, 1.0) * sqrt_dt
            ds = mu * s * dt + sigma * s * dw
            s += ds
            path.append(round(s, 5))
        return path

    @staticmethod
    def simulate_gbm_milstein(s0, mu, sigma, t_max, steps, seed=42):
        rng = random.Random(seed)
        dt = t_max / steps
        sqrt_dt = math.sqrt(dt)
        path = [s0]
        s = s0
        for _ in range(steps):
            dw = rng.gauss(0.0, 1.0) * sqrt_dt
            ds = mu * s * dt + sigma * s * dw + 0.5 * (sigma**2) * s * (dw**2 - dt)
            s += ds
            path.append(round(s, 5))
        return path
