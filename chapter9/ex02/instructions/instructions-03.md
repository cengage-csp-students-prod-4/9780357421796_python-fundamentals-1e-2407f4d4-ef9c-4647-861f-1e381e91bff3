To generate an `AttributeError`:

1. Import the `string` module.

2. Use an attribute that’s not defined in the `string` module.

Running the script with _python3 main.py_ should result in only one console error similar to the example below:

```
AttributeError: module 'string' has no attribute 'asciiletters'
```
