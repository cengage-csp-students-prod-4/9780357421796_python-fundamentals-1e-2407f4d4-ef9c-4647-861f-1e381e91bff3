## Make it your own

_This part involves techniques to solve real-world problems such as pattern string matching, you will need this ability as a software developer._

In the bonus project, we will challenge you to solve problems that are real-world demands in software development. For the first part, you will work with a text pattern-matching technique called regular expressions (or regexes). Then, for the second part, you will create a second user-defined exception that will be used to validate whether a user’s email contains a provider that is blacklisted (this blacklist is based on length, explained later in part 2) due to characteristics in the name.

Your solution has been working well for a couple of weeks. After a few iterations, the TargetCRM’s CTO has collected the mailing list data again to check whether the email address data quality has increased. As expected, the number of incorrect emails has decreased significantly, and the company is happy with the initial improvements that your contribution has brought to the platform.

However, after a few weeks of iterations and tests, the CTO realized that far more complicated errors were present in the email address data that a simple **@** symbol check was not covering. They then realized that the feature was not capturing the more complex incorrect format inputs.

Here are a couple of the bad email formats that were passed in the initial validation:

- john@gmail
- @email.com

These invalid email addresses had incorrectly passed our current validation. Therefore, to create a more robust validator, we will need to implement a more complex technique. Implement a solution using regexes to create a more complex email validator.

> Python has a built-in library for working with regexes, called `re.`. Take a look at the regex patterns to validate email formats.

After some time running your code, the company found out that the system is sending notifications to users that contain emails with reportedly malicious providers. Your solution is not accounting for that right now, and so you will need to implement this functionality.

The company identified a pattern in the email addresses that were reported to be spammers/malicious. They found that a provider with less than five characters is probably an email provider to whom we want to avoid sending notifications.

Create a second custom exception to be raised when an email address with a provider with less than five characters is found.

Once you have filtered the emails that are invalid (in our scenario), return the IDs of the users that are able to receive our communication.

Once you have the email address as an entire string value, you will need to extract only the provider fraction to compute its length. Try to find a way to split the string by a common delimiter, then retrieve only the part you are interested in, which is the provider
