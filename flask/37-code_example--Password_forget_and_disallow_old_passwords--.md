# Password forget & Disallow old passwords
-------

## Example:

    """
    	Whenever you are developing a password forget function, these are the steps to follow
    	in order to create hardened defenses.

    	 TABLE users
        -----------------------------------------------------------------
        | userID   | userName | password |   EmailAdress	 |  access  |
        -----------------------------------------------------------------   
        |   1	   | Admin	  | Csdar323 | info@admin.com	 | 	   TRUE |
        -----------------------------------------------------------------    	
        |	  2	   | User	  | Adf4fsv  | info@user.com     |  FALSE   |
        -----------------------------------------------------------------    
        |	  3	   | Guest	  | dff4fKr  | info@guest.com	 |	   TRUE |
        -----------------------------------------------------------------    


        TABLE passwordForget
        -----------------------------------------------------------------------------------------   
        | forgotPasswordID | 		Token 	    | 	UserID |   Active	|	  olPasswords	    |
        -----------------------------------------------------------------------------------------
        |      1  	 	   | c3ab8ff13720e....  |	  1	   | 	YES		|	   Csdar323	      	|
        -----------------------------------------------------------------------------------------
        |	     2	 	   | 7dd39466b3c89....  |	  1	   | 	NO		  |		ef0c4f2         |
        -----------------------------------------------------------------------------------------
        |	     3	 	   | 83d4a3960714c....	|	  3	   | 	NO		  |		dff4fKr	        |
        -----------------------------------------------------------------------------------------


    	As you can see we also store the old passwords into the password forget table, this
    	we do in order to prevent the user from using old passwords later on in the process.

    	Also use a cron job to make sure the generated tokens for the password reset are
    	expire after a certain amount of time like 20 minutes.

    """

    def checkValidity(email):

        user = Members.query.filter_by(email=email).first()

        # Here we select the old password as well as the userid from the members table
        password = user.password
        userID = user.id
        email = user.email

        # If the select was not empty we will be sending an email to the user as well as 
        # preparing the password forget function

        if user is None:
            """
            We show the user the same message in order to prevent the enumeration of
            valid email addresses.
            """
            return "An email was sent to your email for password reset"

        else:

            """
            Before we do anything we first set all other possible active statuses to NO
            in order to prevent an attacker creating a whole lot of tokens and than fuzz
            the password reset token.
            """

            active = "No"

            user.active = active
            db.session.commit()

            # Here we generate the password forget token
            token = base64.b64encode(rand.bytes(128))

            passwordChange = forgetPassword(token=token, userID=userID, active=active, oldPasswords=password)
            db.session.add(passwordChange)
            db.session.commit()            


    		# Here we send an email to the user with the needed reset function
    		msg = "follow this link to reset your password http://example.com/reset/"" + "token"
    		mail(email,"Password reset", msg)


    def resetPassword(resetLink, password):		

    	"""
    	Imagine the user clicked on his link with the token included and is redirected towards
    	the page where he can enter his new password.

    	Now we select the information from the forgot password function where the
    	forgot tokens matches the token in the database.
    	"""

    	active = "YES"

        data = forgetPassword.query.join(members, forgetPassword.userID==members.userID).filter_by(token=resetLink,Active=active).all()

        # We select token and users id
        token = data.token
        userID = data.userID

        if token == resetLink:
            
            """
            First we pull the password through our function which enforces the input of
            secure passwords.(see "Enforce secure passwords" in code examples for more
            detailed information)
            """

            if checkPassword(password) == True:

                """
                Than we encrypt our password
                (see "Password storage" in code examples for more
                detailed information)    
                """

                createHash
    	
    			if($token === $_GET['resetLink']){

    				/*
    				First we pull the password through our function which enforces the input of
    				secure passwords.(see "Enforce secure passwords" in code examples for more
    				detailed information)
    				*/

    				if($pwd->createPassword($_POST['password']) === true);

    				/*
    				Than we encrypt our password
    				(see "Password storage" in code examples for more
    				detailed information)
    				*/

    				$hash->createHash($_POST['password']);

    				/*
    				Finally we compare the password against other old passwords from the
    				password reset database in order to prevent the user from using old passwords
    				which could already be compromised by any means.
    				*/

    				$stmt = $db->prepare("SELECT oldPasswords FROM forgetPassword where userID=?");
    				$stmt->execute(array($userID));
    				$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

    				foreach($rows as $row){

    					if($newpassword === $row['oldPasswords']){
    						echo "This was an old password please do not use this password";
    					}else{

    						//First we update the new password for the user
    						$active = "NO";
    						$stmt = $db->prepare("UPDATE members SET password=? WHERE userID=?");
    						$stmt->execute(array($newPassword, $userID));
    						$affected_rows = $stmt->rowCount();

    						//Then we destroy the reset token by setting it's value to NO
    						$stmt = $db->prepare("UPDATE forgetPassword SET active=? WHERE userID=?");
    						$stmt->execute(array($active, $userID));
    						$affected_rows = $stmt->rowCount();

    					}
    				}
    			}
    		}
    	}

    ?>
