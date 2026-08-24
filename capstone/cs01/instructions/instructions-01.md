In order to access external REST APIs, for this assignment, you must use the requests package to communicate in the HTTP protocol.

Finish the implementation of the class called `AccessApi`. There are 7 method stubs that will need to be completed: 
1. A constructor that requires the developer to input a base URL as a string that will host the REST API endpoint. Example: “http://google.com”
2. A method to get the current URL base.
3. A method to set the current URL base.
4. A method to test if the URL is responding to GET requests to allow for a simple alive test.
5. A method to input an endpoint, as a string, and have that endpoint concatenated to the base URL and then send a GET request using the requests package to the combined URL. Then, return the JSON sent as a list. 
6. A method to input an endpoint and have that endpoint concatenated to the base URL and then send a GET request using the requests package to the combined URL. Then, return the status code. 
7. A method to input an endpoint and have that endpoint concatenated to the base URL and then send a GET request using the requests package to the combined URL. Then, return the total elapsed time used for the GET request. 


