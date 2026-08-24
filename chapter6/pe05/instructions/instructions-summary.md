<!-- practice -->
# Aim
In this exercise, we will practice set operations.

# Steps for Completion
1. Go to the *main.py* file. 
2. Create two sets as shown in *Snippet 6.120*:
```python
l = {"lion", "tiger", "giraffe", "frog"}
w = {"frog", "fish", "octopus"}
```
<sup>*Snippet 6.120*</sup>

3. Find the union of the two sets as shown in *Snippet 6.121*:
```python
l.union(w)
```
<sup>*Snippet 6.121*</sup>

The output, when printed, is as shown in *Snippet 6.122*:
```
{'lion', 'tiger', 'giraffe', 'frog', 'fish', 'octopus'}
```
<sup>*Snippet 6.122*</sup>

4. Find the intersection of the two sets as shown in *Snippet 6.123*:
```python
l.intersection(w)
```
<sup>*Snippet 6.123*</sup>

The output, when printed, is as shown in *Snippet 6.124*:
```
{'frog'}
```
<sup>*Snippet 6.124*</sup>

5. Find the difference between the sets as shown in *Snippet 6.125*;
```python
l - w
```
<sup>*Snippet 6.125*</sup>

The output, when printed, is as shown in *Snippet 6.126*:
```
{'lion', 'tiger', 'giraffe'}
```
<sup>*Snippet 6.126*</sup>

6. Find the symmetric difference of the sets as shown in *Snippet 6.127*:
```python
l.symmetric_difference(w)
```
<sup>*Snippet 6.127*</sup>

The output, when printed, is as shown in *Snippet 6.128*:
```
{'lion', 'tiger', 'giraffe', 'fish', 'octopus'}
```
<sup>*Snippet 6.128*</sup>