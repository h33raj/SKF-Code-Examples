
input validation
-------

**Example:**

REMARK Glenn: i would advice to remove the logMessage and threatlevel from the input validation, make seperate methods for input validation for Alphanumeric, Nummeric, Alpha, Bool. Then use the Audit log function in the input validation.   
  
	"""
	This function is where you store all your input validation controls. 
	It makes it easy to maintain whenever you want to apply changes for 
	certain input validation roles and reduces the chance of mistakes in your regexes.
	"""

	def inputValidation(input, type, logMessage, threatLevel, countLevel):
	    switcher = {
	        "alphanumeric": "^[a-zA-Z0-9]+$",
	        "nummeric": "^[0-9]*$",
	        "bool": "^(true|false)$"
	    }
	    pattern = switcher.get(type, "nothing")
	    match = re.findall(pattern, input)
	    if match:
	    	setLog(session["id"], "Regex matched", "Success", str(datetime.utcnow()), session['privilege'])
	        return True
	    else:
	    	setLog(session["id"], logMessage, "FAIL", str(datetime.utcnow()), session['privilege'])
	    	counter.increment(1)
	        raise False
