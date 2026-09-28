"""MCP stdio server for SDE Solvers."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import SDESolver

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "simulate_gbm",
                        "description": "Simulate Geometric Brownian Motion path via Euler or Milstein scheme",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "s0": {"type": "number"},
                                "mu": {"type": "number"},
                                "sigma": {"type": "number"},
                                "t_max": {"type": "number", "default": 1.0},
                                "steps": {"type": "integer", "default": 100},
                                "scheme": {"type": "string", "enum": ["euler", "milstein"], "default": "milstein"},
                                "seed": {"type": "integer", "default": 42}
                            },
                            "required": ["s0", "mu", "sigma"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "simulate_gbm":
            s0 = float(args.get("s0"))
            mu = float(args.get("mu"))
            sigma = float(args.get("sigma"))
            t_max = float(args.get("t_max", 1.0))
            steps = int(args.get("steps", 100))
            scheme = args.get("scheme", "milstein")
            seed = int(args.get("seed", 42))
            if scheme == "euler":
                path = SDESolver.simulate_gbm_euler(s0, mu, sigma, t_max, steps, seed)
            else:
                path = SDESolver.simulate_gbm_milstein(s0, mu, sigma, t_max, steps, seed)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"path": path, "terminal_value": path[-1]}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
