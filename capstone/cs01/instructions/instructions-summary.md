# Scenario

REST APIs are ubiquitous, and Python is the go-to tool for testing REST APIs. The goal of this capstone is to mimic a real-world scenario of API testing. You must write several unit tests that validate an example website’s endpoints. Unit tests are a testing method in which individual units of code are tested to determine if that unit is fit for use and working as expected. To guarantee stability over time, several JSON files will be accessible to represent the website under test. You will combine the skills learned in the course with some new skills. The application will use the requests package and `pytest` for basic unit testing.

Implement the class `AccessApi` that will access a REST API using the `requests` package and perform basic functionality. The `requests` package has been installed in the environment for you; however, if you needed to, you can install the package by using the following command: `sudo pip3 install requests`. You will need to write several unit tests with `pytest`, implementing the `AccessApi` class you create. Lastly, you will need to refactor two of the unit tests so they are parametrized.

Use annotations to give type hints. Some languages are strongly typed meaning the interpreter will force every variable, method, object etc., to be declared as a type and will throw an error when a different type is used. Python is not a strongly typed language, which could be beneficial because this allows for flexibility in the code. Python does allow for “hinting” of types beginning with version 3. A developer can give type hints that all IDEs will use and when a type is passed that doesn’t match the one defined, the IDE will give an error. This increases readability and reduces errors in your code with only minor functionality being given up. There is a limitation to this “hinting”, as the types are not enforced at runtime. In other words, these hints are used only by third party tools as an aid to the developer in writing the code.

Example:

```python
def function(arg: <type>) -> <return_type>:
my_variable: <type> = <value>
```

Docstrings are very helpful in decreasing the effort required to become familiar with a body of code. When possible, always try to add useful information, but do not over-document.

This topic is not limited to Python but is relevant to any written software. Software is typically written in phases or iterations. Some functionality is added, tested, bugs corrected, additional functionality, etc., Unfortunately, the process of “enhancing” or “fixing” software sometimes has the unwanted side effect of breaking existing functionality. One way to determine if this has happened is for a person in the test organization to exercise all known tests with every software change. This is impractical, however so often the development team writes automated Unit Tests which test basic functionality. Every time the project is built, automated unit tests are executed against the build. If some functionality fails, the team knows that something has been inadvertently broken and needs to be corrected.

Unit tests are “low-level” tests that exercise the software at a functional level with a pass or fail result. In the case of Python, a simple unit test implementation is to put assert statements in the code to verify that the run time state is as expected. For example, suppose there is a Boolean variable called `myValue` that should be `True` at a certain point in a program’s execution. You could do the following statement at that point:
`assertTrue(myValue == True, “ERROR: myValue is False”)`. When the previous statement is executed, if `myValue` is `False` an `AssertionError` is generated, the message is printed, and execution stops. This is a simple example of unit test step, but there are a number of packages available to assist in writing unit tests.
