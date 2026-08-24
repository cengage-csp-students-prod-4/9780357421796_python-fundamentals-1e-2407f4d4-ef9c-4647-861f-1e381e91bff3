# Scenario

It's the year 2017. You're working for an electronics company and have been tasked with modeling out the software for a cutting-edge tablet that will have a built-in face recognition front camera: a biometric tablet.

# Aim

Create a class called `TabletCamera` and a class called `Facial_recognition` that will be the base classes of a derived class called `BioTablet`.

# Steps for Completion

1. Create a `TabletCamera` class that will be initialized with a `pixels` attribute.

2. Create a `Facial_recognition` class with a `scan_face` method that prints the message, **Scanning Face...**

3. Create a `BioTablet` class that inherits from both the `TabletCamera` and `Facial_recognition` classes.

4. At the bottom of the script initialize an instance of the `BioTablet` class and pass it the value **"12MP"**. Then we call the `scan_face` method and also print out the `pixels` attribute.

Run the script with _python3 main.py_ command and we should have an output that looks like _Snippet 7.91_:

```
Scanning Face...
12MP
```

<sup>_Snippet 7.91_</sup>
