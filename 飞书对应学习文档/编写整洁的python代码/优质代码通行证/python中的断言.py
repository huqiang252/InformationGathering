

try:
    assert condition.holds(), "Condition is not satisfied"
except AssertionError:
    alternative_procedure()




result = condition.holds()
assert result > 0, f"Error with {result}"