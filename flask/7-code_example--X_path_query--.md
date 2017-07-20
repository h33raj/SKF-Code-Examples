# X-path query
-------

## Example:


    """
        Define the allowed characters and input parameter and countlevel for the
        user lockout like:
        controller("<'>&", $_GET['filename'], "3")
    """
    
    def controller(allowed, input, count):
        """
        First we build our encoding method, see "input validation" code example for
        more detailed information about encoding and escaping.
        """
        
        return = encoder(allowed, input, count)

        # If the encoder came back false we do not process the function!

        if return != False:
            # Start a new Document
            root = etree.parse("test.xml")

            find = etree.XPath("//lemonade[@supplier=" + return +"]/price")

            for x in find(root):
                print x.text