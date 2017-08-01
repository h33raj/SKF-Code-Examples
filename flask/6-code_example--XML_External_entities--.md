XML External entities
-------

**Example:**

REMARK Glenn: Maybe add load_dtd=False and explain why and the impact if this is on? Also add a valid XML string in the line 18 

	    ```
	    The overall prevention method for loading external entities is adding the following line of code:
        To be safe from loading external entities you have to turn off the entities in the parser.
	    ```
	    
	    #If you are using lxml 

	    content = '''<?xml version="1.0" encoding="UTF-8"?>\
		<!DOCTYPE title [ <!ELEMENT title ANY >\
        <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>'''

        """
		If the dtd_validation = True and resolve_entities=True and if the attacker can control the
		XML file which is taken in the parser, he can read any file using the file protocol file:/// or use some other protocols like expect://, gopher:// to even get a shell        
        """


	    from lxml import etree
	    parser = etree.XMLParser(dtd_validation=False ,resolve_entities=False)
	    root = etree.XML("<root><a/><b></b></root>", parser)
	    

	    


	    





	
