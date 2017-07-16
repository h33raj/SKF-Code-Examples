# Open forwards & redirects
-------

## Example:


    """
    	When using forwards & redirects you should make sure the URL is being explicitly
    	declared in the code and cannot be manipulated by an attacker like:
    """

        header("location:redirectpage.php");

    """
    	Generally you should avoid getting input into the redirect which could contain
    	user-input by any means. if for any reason this may not be feasible than you
    	should make a whitelist input validation for the redirect like so:
    	send("value1,value2,etc", redirectParam, "3")
    """

        def send(whitelisting, input, count):
        """
        We want to whitelist the paged for expected values, in this example they are,
        page1,page2 etc.. for more information about whitelisting see "white-listing" in the code examples:
        """
            if whitelisting(whitelisting, input, count) == True:
                response.headers['location'] = input
                return response 