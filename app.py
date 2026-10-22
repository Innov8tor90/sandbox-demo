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
