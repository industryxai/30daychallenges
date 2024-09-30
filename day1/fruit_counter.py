from collections import Counter

def count_fruits(fruits: list[str]) -> dict[str, int]:
    return dict(Counter(fruits))
