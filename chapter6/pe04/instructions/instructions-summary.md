<!-- practice -->
# Aim
In this exercise, we will practice data operations on a set.

# Steps for Completion
1. Go to the `main.py` file. 
2. Create a set as shown in *Snippet 6.95*:
```python
v = set({"car", "bus", "train"})
print(v)
```
<sup>*Snippet 6.95*</sup>

The output is as shown in *Snippet 6.96*:
```
("car", "bus", "train")
```
<sup>*Snippet 6.96*</sup>

3. Add `bicycle` to the set as shown in *Snippet 6.97*:
```
v.add("bicycle")
print(v)
```
<sup>*Snippet 6.97*</sup>

The output is as shown in *Snippet 6.98*:
```
("car", "bus", "train", "bicycle")
```
<sup>*Snippet 6.98*</sup>

4. Read data from the set using iterables as shown in *Snippet 6.99*: 
```python
for veh in v:
        print(veh)
```
<sup>*Snippet 6.99*</sup>

The output is as shown in *Snippet 6.100*:
```
car
bus
train
bicycle
```
<sup>*Snippet 6.100*</sup>

5. Remove one item from the set using the `pop()` function as shown in *Snippet 6.101*:
```python
print(v.pop())
```
<sup>*Snippet 6.101*</sup>

The output is as shown in *Snippet 6.102*: 
```
'bus'
```
<sup>*Snippet 6.102*</sup>

6. Remove the `car` vehicle from the set as shown in *Snippet 6.103*:
```python
v.remove("car")
print(v)
```
<sup>*Snippet 6.103*</sup>

The output is as shown in *Snippet 6.104*: 
```
{'bicycle', 'train'}
```
<sup>*Snippet 6.104*</sup>

7. Clear the set using the `clear()` method as shown in *Snippet 6.105*:
```python
v.clear()
print(v)
```
<sup>*Snippet 6.105*</sup>

The output is as shown in *Snippet 6.106*:
```
{}
```
<sup>*Snippet 6.106*</sup>
