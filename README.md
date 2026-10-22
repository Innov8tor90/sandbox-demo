# DefyCode Sandbox Demo (Innov8tor90/sandbox-demo)

Official sandbox repository for testing **DefyCode** (by **IoT Junkie**) mobile code inspection, AI-assisted bug fixing, unified Git diffs, and Password / Face ID push authorization.

## Included Files
- pp.py — Sample API service with a known division-by-zero edge case on line 18 for AI Agent debugging.
- calculator.py — Core telemetry & metrics math helpers.
- 	est_calculator.py — Unit test suite.
- AGENT.md — Project-specific AI agent directives.

## Quick Prompts to Try in DefyCode Agent Tab
1. "Inspect app.py and fix the zero-division bug in calculate_average_latency"
2. "Add input validation to calculator.py and run unit tests"
"@

Set-Content -Path "C:\Users\cczar\.gemini\antigravity\brain\3824ba3a-180c-42f6-98b8-ba21a97be68a\scratch\sandbox-demo\app.py" -Encoding UTF8 -Value @"
"""
DefyCode Sandbox Demo Service
A sample microservice for testing mobile AI code inspection and bug fixes.
"""
from calculator import compute_throughput, format_Summary


def calculate_average_latency(samples: list[float]) -> float:
    """
    Calculates average request latency in milliseconds.
    NOTE: Contains an intentional bug when samples is empty for AI Agent demo.
    """
    total = sum(samples)
    # BUG: ZeroDivisionError if samples is empty []
    return round(total / len(samples), 2)


def handle_health_check() -> dict:
    latencies = [12.4, 15.1, 9.8, 11.2]
    avg_ms = calculate_average_latency(latencies)
    throughput = compute_throughput(total_requests=480, window_seconds=60)
    return {
        "service": "sandbox-demo",
        "status": "healthy",
        "avg_latency_ms": avg_ms,
        "rps": throughput,
        "summary": format_Summary("sandbox-demo", avg_ms, throughput),
    }


if __name__ == "__main__":
    print(handle_health_check())
