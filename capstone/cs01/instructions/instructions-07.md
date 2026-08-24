## Make it your own

We now have a testing platform and some useful tests for our company’s website. The tests we have done are not maintainable and hard, which is not very pythonic.

Pythonic can be thought of as simple, and straightforward way to write and read. The next task is to refactor two of our tests, so that they use the parametrize functionality of pytest.

```python
import pytest
@pytest.mark.parametrize("<first_input>,<second_input>,", [
    ("String1", true),
    ("String2", false),
    ("String3",true),
    ])
def test_eval((<first_input>,<second_input>):
    ….

```

Tests to refactor:

1. Validate the HTTP status code is **200**.
2. Validate that the response time should be less than one minute.
