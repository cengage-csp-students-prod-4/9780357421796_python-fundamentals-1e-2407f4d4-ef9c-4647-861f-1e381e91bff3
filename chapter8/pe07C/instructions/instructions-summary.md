<!-- practice -->

# Aim

In this exercise, we will create a json variable and write it to a file.

# Steps for Completion

1. Import the `json` library, as shown in _Snippet 8.85_:

```python
>>> import json
```

<sup>_Snippet 8.85_</sup>

2. Create the `json` variable shown in _Snippet 8.86_:

```python
>>> flower = {
...    "flower": "Rose",
...    "size": "Large",
...    "color": "Red"
}
```

<sup>_Snippet 8.86_</sup>

3. Add it to the variable `flower_json`, as shown in _Snippet 8.87_:

```python
>>> flower_json = json.dumps(flower)
```

<sup>_Snippet 8.87_</sup>

4. Print the `flower_json` variable, as shown in _Snippet 8.88_:

```python
>>> print(flower_json)
```

<sup>_Snippet 8.88_</sup>

The output is as shown in _Snippet 8.89_:

```
{"flower": "Rose", "size": "Large", "color": "Red"}
```

<sup>_Snippet 8.89_</sup>

5. Print the type of `flower_json`, as shown in _Snippet 8.90_:

```python
>>> print(type(flower_json))
```

<sup>_Snippet 8.90_</sup>

The output is as follows:

```
<class 'str'>
```

6. Create a file named _dict.json_ and write the `flower_json` to it, as shown in _Snippet 8.92_:

```python
>>> f = open("dict.json", "w")
>>> f.write(flower_json)
51
>>> f.close()
```

<sup>_Snippet 8.92_</sup>

Check the _dict.json_ file for the proper contents.
