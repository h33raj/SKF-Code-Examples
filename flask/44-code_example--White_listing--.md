# White-listing
-------

## Example:


    """
    First we create a function which checks the allowed patterns:
        checkpattern("value1,value2,value3" , $input, "3")
    """

    def whitelisting(allowed, input):
        result = allowed.split(',')
        flag = False
        for x in result:
            match = re.findall("/^"+x+"$/", input)
            if match:
                #If the value is valid we send a log to the logging file
                setLog(session["id"], "Good whitelist validation", "SUCCESS", datetime.utcnow(),"HIGH")
                flag = True
                #Whenever there was a valid match we return true
                return True
            #Check for a false in order to send error to log and counter the user
            if flag == False:
                setLog(session["id"], "Bad whitelist validation", "FAIL", datetime.utcnow(), "HIGH")            
                counter.increment()
                return False    