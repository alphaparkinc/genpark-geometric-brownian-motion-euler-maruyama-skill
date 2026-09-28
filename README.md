# Euler-Maruyama & Milstein SDE Solvers Skill

High-order numerical integration schemes for Itô stochastic differential equations with Brownian increments.

```mermaid
flowchart LR
    S0["Initial Value S_0"] --> Drift["Drift μ S Δt"]
    S0 --> Diff["Diffusion σ S ΔW"]
    S0 --> Milstein["Higher Order Term: 0.5 σ^2 S (ΔW^2 - Δt)"]
    Drift --> Step["Combine Next Step S_{t+1}"]
    Diff --> Step
    Milstein --> Step
    Step --> Trajectory["Complete Discrete Stochastic Trajectory"]
```

## Features
- **100% Python Standard Library**: Box-Muller Gaussian generation.
- **Order 1.0 Strong Convergence**: Milstein scheme eliminates discretization bias.
- **MCP Server Ready**: Instant stdio simulation for agent forecasting.
