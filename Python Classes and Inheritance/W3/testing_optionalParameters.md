# Testing Optional Parameters

If a function takes an optional parameter, one of the edge cases to test for is when no parameter value is supplied during execution. Below are some tests for the built-in sorted function.

```
assert sorted([1, 7, 4]) == [1, 4, 7]
assert sorted([1, 7, 4], reverse=True) == [7, 4, 1]
```
