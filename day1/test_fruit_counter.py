import pytest
from fruit_counter import count_fruits

def test_count_fruits():
    assert count_fruits(["apple", "banana", "apple", "orange", "banana", "apple"]) == {
        "apple": 3,
        "banana": 2,
        "orange": 1,
    }
    assert count_fruits([]) == {}
    assert count_fruits(["grape"]) == {"grape": 1}
    assert count_fruits(["apple", "apple", "apple"]) == {"apple": 3}
    assert count_fruits(["banana", "banana", "apple"]) == {"banana": 2, "apple": 1}

# This allows pytest to discover the test cases.
if __name__ == "__main__":
    pytest.main()
