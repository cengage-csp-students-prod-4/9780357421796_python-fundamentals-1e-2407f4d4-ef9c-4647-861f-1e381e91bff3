<!-- practice -->

# Aim

Load a CSV file and count the number of rows in the file.

# Steps for Completion

1. In _main.py_, import the CSV module:

```python
import csv
```

2. Open the CSV folder as a reader object “f”:

```python
with open('MOCK_DATA.csv', 'r') as f:
    mock_data_reader = csv.reader(f)
```

3. After assigning the reader to the CSV file, on the next line within the reader object **f**, start a line count at **1** and loop through the rows, printing each one as shown in _Snippet 8.70_:

```python
    line_count = 1

    for row in mock_data_reader:
        if line_count > 1: #skipping line 1 which is the header row
            print(row)

        line_count += 1
```

<sup>_Snippet 8.70_</sup>
