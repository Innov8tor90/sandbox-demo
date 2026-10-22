from app import calculate_average_latency, handle_health_check
from calculator import compute_throughput


def test_throughput():
    assert compute_throughput(120, 60) == 2.0
    assert compute_throughput(100, 0) == 0.0


def test_average_latency():
    assert calculate_average_latency([10.0, 20.0, 30.0]) == 20.0


def test_health_check():
    res = handle_health_check()
    assert res["status"] == "healthy"
    assert res["rps"] == 8.0
