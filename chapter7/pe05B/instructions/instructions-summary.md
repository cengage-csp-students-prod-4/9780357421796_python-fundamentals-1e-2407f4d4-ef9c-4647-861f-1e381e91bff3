<!-- practice -->

# Aim

Class methods also have access to class attributes. They can get and set class attributes. Most browsers today have a geolocation API. We will simulate this functionality in our class.

In this exercise, we will create a `geo_coordinates` attribute in the `WebBrowser` class that holds the current latitude and longitude. We will also add a class method called `change_geo_coordinates()` that will change the coordinates when called.

# Steps for Completion

1. Add the `geo_coordinates` class attribute and change the `geo_coordinates()` class method, as shown in _Snippet 7.58_:

```python
class WebBrowser:
	geo_coordinates = {"lat": -4.764813, "lng": 16.131331 }
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
	@classmethod
	def change_geo_coordinates(cls, new_coordinates):
		if new_coordinates["lat"] > 90 or new_coordinates["lat"] < -90:
			print("Invalid value for latitude. Should be within the range from -90 to 90 degrees.")
			return None
		if new_coordinates["lng"] > 180 or new_coordinates["lng"] < -180:
			print("Invalid value for longitude. Should be within the range from -180 to 180 degrees.")
			return None
		cls.geo_coordinates = new_coordinates
```

<sup>_Snippet 7.58_</sup>

Our class method, `change_geo_coordinates`, takes the `new_coordinates` parameter, which is a dictionary. It checks whether the latitude and longitude provided in the parameters are valid and then changes the class attribute `geo_coordinates` to reflect the new coordinates that have been provided. We can test this out.

2. Create a `WebBrowser` instance, `firefox`, and check its geocoordinates. It fetches the attribute from the class as shown in _Snippet 7.59_:

```
>>> from main import WebBrowser
>>> firefox = WebBrowser("www.org")
>>> firefox.geo_coordinates
{'lat': -4.764813, 'lng': 16.131331}
```

<sup>_Snippet 7.59_</sup>

3. Calling `change_geo_coordinates` on the class, as we do in _Snippet 7.60_, changes the `geo_coordinates` attribute for all of the class's instances (since they fetch the attribute from the class), and hence this change reflects for the `firefox` instance:

```
>>> WebBrowser.change_geo_coordinates({"lat": 31, "lng": 123})
>>> firefox.geo_coordinates
{'lat': 31, 'lng': 123}
>>> WebBrowser.change_geo_coordinates({"lat": 31, "lng": 190})
Invalid value for longitude. Should be within the range from -180 to 180 degrees.
>>> WebBrowser.change_geo_coordinates({"lat": -100, "lng": 123})
Invalid value for latitude. Should be within the range from -90 to 90 degrees.
>>>
```

<sup>_Snippet 7.60_</sup>
