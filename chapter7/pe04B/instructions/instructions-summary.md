<!-- practice -->

# Aim

Our aim here is to thoroughly understand class attributes. In this exercise, we're going to create a counter that will be incremented each time a new `WebBrowser` object is instantiated:

# Steps for Completion

Add the class attribute `number_of_web_browsers`, which will serve as the counter and will start at 0 as shown in _Snippet 7.41_:

```python
class WebBrowser:
	number_of_web_browsers = 0
	connected = True
	def __init__(self, page):
		self.history = [page]
		self.current_page = page
		self.is_incognito = False
```

<sup>_Snippet 7.41_</sup>

2. Modify the constructor to increment the counter each time a new instance is created by adding the line `WebBrowser.number_of_web_browsers += 1` as shown in _Snippet 7.42_. This increments the `number_of_web_browsers` attribute of our class by 1 and will be called each time a new instance is initialized:

```python
class WebBrowser:
	number_of_web_browsers = 0
	connected = True
	def __init__(self, page):
		self.history = [page]
		self.current_page = page
		self.is_incognito = False
		WebBrowser.number_of_web_browsers += 1
```

<sup>_Snippet 7.42_</sup>

Let's test it out:

3. First, check that the `number_of_web_browsers` counter is at 0 as shown in _Snippet 7.43_:

```
>>> from main import WebBrowser
>>> WebBrowser.number_of_web_browsers
0
>>>
```

<sup>_Snippet 7.43_</sup>

4. Next, instantiate a new object and check the counter as shown in _Snippet 7.44_:

```
>>> opera = WebBrowser("opera.com")
>>> WebBrowser.number_of_web_browsers
1
>>>
```

<sup>_Snippet 7.44_</sup>

5. The counter increments with every other instance we create. Check this, as shown in _Snippet 7.45_:

```
>>> edge = WebBrowser("microsoft.com")
>>> WebBrowser.number_of_web_browsers
2
>>>
```

<sup>_Snippet 7.45_</sup>

Besides the use cases we've seen, class attributes should be used when you have variables that are common to all instances, such as constants for the class.
