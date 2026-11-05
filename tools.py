"""Utility tools module."""

def calculate_stats(data: list[int]) -> dict[str, float]:
    """Calculate basic statistics from a list of numbers."""
    if not data:
        return {"count": 0, "mean": 0.0, "total": 0.0}
    total = sum(data)
    mean = total / len(data)
    return {"count": len(data), "mean": mean, "total": float(total)}

if __name__ == "__main__":
    sample = [10, 20, 30, 40, 50]
    print("Sample stats:", calculate_stats(sample))
