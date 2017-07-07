
XML External entities
-------

**Example:**

	    

	    ```
	    The overall prevention method for loading external entities is adding the following line of code:
            To be safe from loading external entities you have to turn off the entities in the parser.
	    ```
	    
	    #If you are using lxml 

	    from lxml import etree
	    parser = etree.XMLParser(resolve_entities=False)
	    root = etree.XML("<root><a/><b></b></root>", parser)
	    

	    


	    





	
