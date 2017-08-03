Secure session cookies
-------

**Example:**


    """
    Javascript cannot set or read cookie's value if the HTTPOnly attribute is set on cookie.
    It makes attacker client side attacks such as Cross Site scripting harder to exploit.
    Attacker will not be able to steal the user's cookies.
	"""

	from flask import Flask, session

	#Intialize the flask application
	app = Flask(__name__)

	# set the secret key.  keep this really secret:
	app.secret_key = open("/dev/random","rb").read(32) 

	#Name of the session cookie
	app.config['SESSION_COOKIE_NAME'] = 'hrj'
	
	#Path for the session cookie
	app.config['SESSION_COOKIE_PATH'] = '/'
	
	#Domain for the session cookie
	#Configure domains, do not use .yourdomain.com (wildcard)
	#this increases the attack surface!
	app.config['SESSION_COOKIE_DOMAIN'] = 'demo.yourdomain.com'
	
	#Controls if the cookie should be set with the secure flag
	app.config['SESSION_COOKIE_SECURE'] = True
	
	#Controls if the cookie should be set with the httponly flag
	app.config['SESSION_COOKIE_HTTPONLY'] = True
	
	#Lifetime of a permanent session
	app.config['PERMANENT_SESSION_LIFETIME'] = 3600

	#Store Value in session
	session['type'] = "value"
