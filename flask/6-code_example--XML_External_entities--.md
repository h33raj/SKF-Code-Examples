
XML External entities
-------

**Example:**

REMARK Glenn: Maybe add load_dtd=False and explain why and the impact if this is on? Also add a valid XML string in the line 18 

	    ```
	    The overall prevention method for loading external entities is adding the following line of code:
            To be safe from loading external entities you have to turn off the entities in the parser.
	    ```
	    
	    #If you are using lxml 

	    from lxml import etree
	    parser = etree.XMLParser(resolve_entities=False)
	    root = etree.XML("<root><a/><b></b></root>", parser)
	    

	    


	    





	
