<!-- practice -->
# Aim
Suppose you have chunks of text data and you want to save the words in a dictionary with their frequency of occurrence. 

# Steps for Completion
1. Go to your *main.py* file. 
2. Create a dictionary as shown in *Snippet 6.24*:
```python
In [1]: freqDict = {"hi":45, "this":35, "the":28}    
```
<sup>*Snippet  6.24*</sup>

3. Print the values in the dictionary using the command shown in *Snippet 6.25*:
```python
In [2]: print(freqDict) 
```
<sup>*Snippet 6.25*</sup>

The output will be as shown in *Snippet 6.26*:
```text
{'this': 35, 'hi': 45, 'the': 28}
```
<sup>*Snippet 6.26*

4. Add another word `and` to the dictionary as shown in *Snippet 6.27*:
```python
In [3]: freqDict['and'] = 20
```
<sup>*Snippet 6.27*</sup>

5. Print the values in the dictionary using the command shown in *Snippet 6.28*:
```python
In [4]: print(freqDict)  
```
<sup>*Snippet 6.28*</sup>

The output is as shown in *Snippet 6.29*: 
```text
{'hi': 45, 'this': 35, 'the': 28, 'and': 20}
```
<sup>*Snippet 6.29*</sup>

6. Read the frequency of the word `this` using the `get()` function. Print the result as shown in *Snippet 6.30*:
```python
In [5]: print(freqDict.get('this')) 
```
<sup>*Snippet 6.30*</sup>

The output is as shown in *Snippet 6.31*:
```text
35
```
<sup>*Snippet 6.31*</sup>

7. Read the frequency of word `from`. Note that the word is not available in dictionary. Print the result as shown in *Snippet 6.32*:
```python
In [6]: print(freqDict.get('from'))
```
<sup>*Spippet 6.32*</sup>

The output is as shown in *Snippet 6.33*:
```text
None
```
<sup>*Snippet 6.33*</sup>

8. Specify the message to be displayed in case the word passed through the `get()` function is not in the dictionary, as shown in *Snippet 6.34*:
```python
In [7]: print(freqDict.get('from', 'Word does not exist in the dictionary')) 
```
<sup>*Snippet 6.34*</sup>

The output is as shown in *Snippet 6.35*:
```text
Word does not exist in the dictionary
```
<sup>*Snippet 6.35*</sup>

9. Print the words in the dictionary using the `keys()` method as shown in *Snippet 6.36*:
```python
In [8]: for item in freqDict.keys(): 
   ...:      print(item) 
```
<sup>*Snippet 6.36*</sup>

The output is as shown in *Snippet 6.37*:
```text
hi
this
the
and
```
<sup>*Snippet 6.37*<sup>

10. Print the frequency of the words using the `values()` method as shown in *Snippet 6.38*:
```python
In [9]: for item in freqDict.values(): 
   ...:     print(item) 
```
<sup>*Snippet 6.38*</sup>

The output is as shown in *Snippet 6.39*:
```text
45
35
28
20
```
<sup>*Snippet 6.39*<sup>

11. Print the words with the frequency of their occurrence together as shown in *Snippet 6.40*:
```python
In [10]: for key, value in freqDict.items(): 
    ...:     print(key, value) 
```
<sup>*Snippet 6.40*</sup>

The output is as shown in *Snippet 6.41*:
```text
('hi', 45)
('this', 35)
('the', 28)
('and', 20)
```
<sup>*Snippet 6.41*</sup>

12. Check if a word exists in the dictionary using the `in` keyword. *Snippet 6.42* shows some examples:
```python
In [11]: print("hi" in freqDict) 
    ...: print("hello" in freqDict)   
```
<sup>*Snippet 6.42*</sup>

The output of the statements above is shown in *Snippet 6.43*:
```text
True
False
```
<sup>*Snippet 6.43*</sup>
