
input validation
-------

**Example:**

  
	"""
	This function is where you store all your input validation controls. 
	It makes it easy to maintain whenever you want to apply changes for 
	certain input validation roles and reduces the chance of mistakes in your regexes.
	"""

	class validate(object):
	    def __init__(self):
	        self.pattern = ""

	    def inputValidation(self, type, value, level):
	        switcher = {
	            "alphanumeric": "^[a-zA-Z0-9]+$",
	            "nummeric": "^[0-9]*$",
	            "bool": "^(true|false)$"
	        }
	        self.pattern = switcher.get(type, "nothing")
	        match = re.findall(self.pattern, value)
	        if match:
	            return True
	        else:
	            raise Exception("User supplied value not in the range " + range)
