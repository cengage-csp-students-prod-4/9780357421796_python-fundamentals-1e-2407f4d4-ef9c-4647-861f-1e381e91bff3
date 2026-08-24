<!-- practice -->

# Aim

Suppose you would like to create a dictionary of the first five planets, as shown in _Snippet 8.77_:

```python
planets = {
    "Mercury":1,
    "Venus":2,
    "Earth":3,
    "Mars":4,
    "Jupiter":5,
}
```

<sup>_Snippets 8.77_</sup>

# Steps for Completion

1. Import the `csv` module, as shown in _Snippet 8.78_:

```python
>>> import csv
```

<sup>_Snippet 8.78_</sup>

2. Use the `with` command to write the fields to the _planets.csv_ file, as shown in _Snippet 8.79_:

```python
>>> with open('planets.csv', 'w') as f:
        fields = ['planet', 'position']
        planet_writer = csv.DictWriter(f, fieldnames=fields)
        planet_writer.writeheader()
        planet_writer.writerow({'planet': 'Mercury', 'position': 1})
        planet_writer.writerow({'planet': 'Venus', 'position': 2})
        planet_writer.writerow({'planet': 'Earth', 'position': 3})
        planet_writer.writerow({'planet': 'Mars', 'position': 4})
        planet_writer.writerow({'planet': 'Jupiter', 'position': 5})
```

<sup>_Snippet 8.79_</sup>

Your CSV file will look similar to _Snippet 8.80_:

```
planet,position
Mercury,1
Venus,2
Earth,3
Mars,4
Jupiter,5
```

<sup>_Snippet 8.80_</sup>
