# Character encoding
-------

## Example:

REMARK Glenn: Encoding of dangerous characters is to transform them to non dangerous characters. The approach for this depends on the context you are using it. For HTML we encode them to HTML Entity and JSON to JSON Entity. Please adjust the code to reflect this. More info can be found here: 
https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet#HTML_entity_encoding

    """
    This is the encoder class for whenever you have to allow certain
    possibly dangerous characters into your code for i.e names such as O'reily
	"""

	def encoder(allowed, input, count):
	    
	    """
	        As you can see you can specify allowed characters in your function
	    """
	    
	    flag = True
	    match = re.findall("/^[a-zA-Z0-9 " + allowed+"]+$/", input)
	    if match:

	        """
	        Set a log for whenever there is unexpected userinput with a threat level
	        See "audit logs" code example for more information:
	        """

	        setLog(session['id'], "Bad userinputssss", "FAIL", datetime.utcnow(), "HIGH")
	        
	        """
	        Set counter if counter hits 3 the users session must terminated
	        After 3 session terminations the user account must be blocked
	        See "audit logs" code example for more information:
	        """
	        
	        counter.increment()
	        flag = False
	        return escape(input)
