<!-- practice -->

# Aim

In this exercise, we'll try out our factory method from our `WebBrowser` class, included in the `main.py` file and shown below:

# Steps for Completion

```python
class WebBrowser:
	def __init__(self, page):
		self.history = [page]
		self.current_page = page
		self.is_incognito = False

	def navigate(self, new_page):
		self.current_page = new_page
		if not self.is_incognito:
			self.history.append(new_page)

	def clear_history(self):
		self.history[:-1] = []

	@classmethod
	def with_incognito(cls, page):
		instance = cls(page)
		instance.is_incognito = True
		instance.history = []
		return instance
```

<sup>_The WebBrowser class_</sup>

1. Print out the class method as shown in _Snippet 7.53_. The output tells us that it is a bound method of the `WebBrowser` class. This illustrates what we said earlier regarding class methods and how they are bound to the class itself:

```
>>> from main import WebBrowser
>>> WebBrowser.with_incognito
<bound method WebBrowser.with_incognito of <class 'main.WebBrowser'>>
```

<sup>_Snippet 7.53_</sup>

2. Create a `WebBrowser` instance that starts off in incognito mode. Note that we call `with_incognito` through the class. Despite not passing the `cls` argument in this call, Python implicitly passes the `WebBrowser` class to the function. All we need to pass in is the `page` parameter as shown in _Snippet 7.54_:

```
>>> chrome = WebBrowser.with_incognito("shady-website.com")
>>> chrome.is_incognito
True
```

<sup>_Snippet 7.54_<sup>

3. Print out the current page of our instance to check whether it was set as shown in _Snippet 7.55_:

```
>>> chrome.current_page
'shady-website.com'
```

<sup>_Snippet 7.55_</sup>

4. Confirm that the history was not tracked as shown in _Snippet 7.56_:

```
>>> chrome.history
[]
>>>
```

<sup>_Snippet 7.56_</sup>

5. Additionally, you can call class methods through instances for the same effect as shown in _Snippet 7.57_:

```
>>> opera = WebBrowser("foobar.com")
>>> netscape = opera.with_incognito("secret.net")
>>> netscape.current_page
'secret.net'
>>> netscape.is_incognito
True
>>>
```

<sup>_Snippet 7.57_</sup>

> You should only call class methods through an instance in situations where it won't raise any confusion as to what kind of method it is you're calling (instance or class method).
