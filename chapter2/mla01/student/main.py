import requests

def validate_url(url):
	"""Validates the given url passed as string.
	
	Arguments:
	url -- String, A valid url should be of form <Protocol>://<hostmain>/<fileinfo>
	
	Protocol = [http, https, ftp]
	Hostname = string
	Fileinfo = [.html, .csv, .docx]
	"""
	# your code starts here.
	
	# Task #01: allow-lists for the two things we validate
	valid_protocols = ["http", "https", "ftp"]
	valid_fileinfo = [".html", ".csv", ".docx"]
	
	# Split the protocol away from the rest of the URL.
	# A well-formed URL yields exactly two parts: ["https", "www.site.com/page.html"]
	parts = url.split("://")
	if len(parts) != 2:
		return False
	
	protocol = parts[0]
	remainder = parts[1]
	
	# Task #02, condition 1: protocol must be on the allow-list
	if protocol not in valid_protocols:
		return False
	
	# Task #02, condition 2: the final path segment must carry a valid extension.
	# split("/")[-1] grabs the filename no matter how deep the path is.
	# If the URL ends in "/", this is "" and no extension will match -> False.
	fileinfo = remainder.split("/")[-1]
	for extension in valid_fileinfo:
		if fileinfo.endswith(extension):
			return True
	
	return False # return True if url is valid else False


if __name__ == '__main__':
	url = input("Enter an Url: ")
	print(validate_url(url))