<!-- practice -->
# Aim
Consider the text frequency scenario that we considered in *Practice Exercise 6.1*. We’ll now perform further operations on the dictionary we created.

# Steps for Completion
1. Go to the *main.py* file. 
2. Create the dictionary `freqDict` as shown in *Snippet 6.62*:
```python
freqDict = {"hi": 45, "this": 35, "the": 28}
```
<sup>*Snippet 6.62*</sup>

3. Update the occurrence of the word `the` to **40** using the `update()` command as shown in *Snippet 6.63*:
```python
freqDict.update({"the":40})
```
<sup>*Snippet 6.63*</sup>

4. Print the dictionary once again to verify it was updated as shown in *Snippet 6.64*:
```python
print(freqDict)
```
<sup>*Snippet 6.64*</sup>

The output is as shown in *Snippet 6.65*:
```
{'hi': 45, 'this': 35, 'the': 40}
```
<sup>*Snippet 6.65*</sup>

5. Create a copy of the dictionary using the `copy()` command as shown in *Snippet 6.66*:
```python
copyFreqDict = freqDict.copy()
print(copyFreqDict)
```
<sup>*Snippet 6.66*</sup>

The output is as shown in *Snippet 6.67*:
```
{'hi': 45, 'the': 40, 'this': 35}
```
<sup>*Snippet 6.67*</sup>

6. Remove a random item from the dictionary as shown in *Snippet 6.68*:
```python
print(copyFreqDict.popitem())
```
<sup>*Snippet 6.68*</sup>

The output will pop one of the items as shown in *Snippet 6.69*:
```
{'hi', 45}
```
<sup>*Snippet 6.69*</sup>

7. Add the word `data` into the dictionary only if the word does not exist using the `setdefault()` function as shown in *Snippet 6.70*:
```python
newFreqDict = copyFreqDict.setdefault("data", "21")
print(newFreqDict)
```
<sup>*Snippet 6.70*</sup>

The value in the second argument will be output as shown in *Snippet 6.71*:
```
'21'
```
<sup>*Snippet 6.71*</sup>

8. Remove the word `this` and its frequency from the dictionary using the `pop()` command as shown in *Snippet 6.72*:
```python
count = freqDict.pop("this")
print(count)
```
<sup>*Snippet 6.72*</sup>

The output is as shown in *Snippet 6.73*:
```
35
```
<sup>*Snippet 6.73*</sup>

9. Suppose the data in the dictionary has become incorrect and you have to empty the entire dictionary. You can do so using the `clear()` command as shown in *Snippet 6.74*:
```python
freqDict.clear()
print(freqDict)
```
<sup>*Snippet 6.74*</sup>

The output is as shown in *Snippet 6.75*:
```
{}
```
<sup>*Snippet 6.75*</sup>

10. Create a dictionary using `fromkeys()` function as shown in *Snippet 6.76*:
```python
keys = {'d', 'i', 'c', 't'}
value = [1]
newDict = dict.fromkeys(keys, value)
print(newDict)
```
<sup>*Snippet 6.76*</sup>

The output will be as shown in *Snippet 6.77*:
```
{'d': [1], 'i': [1], 'c': [1]. 't': [1]}
```
<sup>*Snippet 6.77*</sup>


