
Random password/token generation
-------

**Example:**

	"""
	When needing to generate random numbers, always use proven methods 
	instead of writing your own.
	"""
REMARK Glenn: Maybe also add a way to do this on a Windows OS?
	#Generate a strong security key
	app.secret_key = open("/dev/random","rb").read(32) 

	#A random string for generating WTF CSRF token
	app.config['WTF_CSRF_SECRET_KEY'] = base64.b64encode(rand.bytes(128))
    
