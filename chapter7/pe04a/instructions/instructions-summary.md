<!-- practice -->

# Aim

In this activity, we'll declare a `WebBrowser` class that has the attributes for history, the current page, and a flag that shows whether it's incognito or not. It can be initialized with a page.

> The attributes that we will declare inside the constructor will be added as instance attributes The binding of the attributes to the instance happens in the `__init__` method, where we add attributes to `self` .

# Steps for Completion

1. Define the `WebBrowser` class as shown in _Snippet 7.30_:

```python
class WebBrowser:
	def __init__(self, page):
		self.history = [page]
		self.current_page = page
		self.is_incognito = False
```

<sup>_Snippet 7.30_<sup>

2. Then, initialize the objects from the class as shown in _Snippet 7.31_:

```
>>> from main import WebBrowser
>>> firefox = WebBrowser("google.com")
>>> chrome = WebBrowser("facebook.com")
>>>
```

<sup>_Snippet 7.31_</sup>

3. Every `WebBrowser` instance will have a different `current_page` attribute. This happens because these attributes are bound to the instance and not to the class; they are instance attributes. Check this by getting the `current_page` attribute on different `WebBrowser` instances as shown in _Snippet 7.32_:

```
>>> firefox.current_page
'google.com'
>>> chrome.current_page
'facebook.com'
>>>
```

<sup>_Snippet 7.32_</sup>
