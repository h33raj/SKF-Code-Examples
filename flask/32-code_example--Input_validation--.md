
input validation
-------

**Example:**

  
	"""
	This function is where you store all your input validation controls. 
	It makes it easy to maintain whenever you want to apply changes for 
	certain input validation roles and reduces the chance of mistakes in your regexes.
	"""

	def inputValidation(type, value):
	    switcher = {
	        "alphanumeric": "^[a-zA-Z0-9]+$",
	        "nummeric": "^[0-9]*$",
	        "bool": "^(true|false)$"
	    }
	    pattern = switcher.get(type, "nothing")
	    match = re.findall(pattern, value)
	    if match:
	        return True
	    else:
	        raise False