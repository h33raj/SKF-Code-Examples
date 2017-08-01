# Directory/path traversal
-------

## Example:

REMARK Glenn: Rebuild the code below and show/create a function that can retrieve a file from different folders
	"""
		Define the whitelist pattern and validation type and input parameter, countLevel like:
		getFiles("page1,page2,etc", "alphanummeric", $_GET['filename'], "3")
	"""

	def getFiles(whiteListPattern, validationType, inputParameter, countLevel):
		
		continue = True

		"""
		First, we want to filter the filenames for expected values. For this example we use only a-z/0-9
			Whenever the values are tampered with, we can assume an attacker is trying to inject malicious input.
		for more information about validation see "input validations" in the code examples:
		"""

		if inputValidation(inputParameter, validationType, "Invalid userinput", "HIGH", countLevel) == False:
			continue = False

		"""
			Second, we want to whitelist the filenames for expected values, in this example they are,
			page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
		"""

		if whitelisting(whiteListPattern, inputParameter):
			continue = False

		if continue == False:
			return send_from_directory(app.config['UPLOAD_FOLDER'], inputParameter)
