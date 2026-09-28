"""Example simulating GBM paths."""
from client import SDESolver

def main():
    path = SDESolver.simulate_gbm_milstein(s0=100.0, mu=0.05, sigma=0.2, t_max=1.0, steps=20)
    print("Simulated Milstein GBM Path (20 steps):")
    print(path)

if __name__ == "__main__":
    main()
