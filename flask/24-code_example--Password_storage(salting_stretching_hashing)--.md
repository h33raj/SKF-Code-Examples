# Password storage(salting/stretching/hashing)
-------

## Example:

    from flask.ext.bcrypt import Bcrypt

    #Intialise the application with Bcrypt
	app = Flask(__name__)
	bcrypt = Bcrypt(app)

	"""
		For the encryption of passwords we use php's BCRYPT encryption method.
	"""

	def createHash(pwd):
		setLog(0, "Create password Hash", "SUCCESS", str(datetime.utcnow()), "HIGH")
		return bcrypt.generate_password_hash(pwd)

	"""
		Validate your password
	"""

	def ValidatePassword(pwd):
		setLog(0, "ValidatePassword", "SUCCESS", str(datetime.utcnow()), "HIGH")
		return bcrypt.check_password_hash(pw_hash, pwd)
