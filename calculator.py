"""
Core telemetry calculation utilities for sandbox-demo.
"""


def compute_throughput(total_requests: int, window_seconds: int) -> float:
    if window_seconds <= 0:
        return 0.0
    return round(total_requests / window_seconds, 2)


def format_Summary(service_name: str, latency_ms: float, rps: float) -> str:
    return f"[{service_name}] Avg Latency: {latency_ms}ms | Throughput: {rps} req/s"
