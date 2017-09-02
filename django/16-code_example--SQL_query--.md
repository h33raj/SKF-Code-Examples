SQL query
-------

**Example:**

    """
    Django supports almost most of the database backends.  

    A model contains the essential fields and behaviors of the data you’re storing.
    Each model maps to a single database table.

    CREATE TABLE myapp_person (
    	"id" serial NOT NULL PRIMARY KEY,
    	"first_name" varchar(30) NOT NULL,
    	"last_name" varchar(30) NOT NULL
	);

	Model for the above SQL query
	"""

	from django.db import models

	class Person(models.Model):
    	first_name = models.CharField(max_length=30)
    	last_name = models.CharField(max_length=30)


    """
    In order to add your model to django, you have to add the app in INSTALLED_APP
    """

    INSTALLED_APPS = [
    	#...
    	'myapp',
    	#...
	]


	"""
	After adding the application, inorder to make the changes we need to make migrations
	and migrate - For creating tables 
	"""

	$ python manage.py makemigrations

	$ python manage.py migrate

	# Needs to be added
	"""
	Inserting data into the database - create, add and commit
	"""
	admin = User(username='admin', password='9u3$$_m3_1f_y0u_C@n')
	db.session.add(admin)
	db.session.commit()

	"""
	Delete entries from the table
	"""
	db.session.delete(admin)
	db.session.commit()

	"""
	Querying Records
	"""
	#Retrieve the user with username
	admin = User.query.filter_by(username='admin').first()
	admin.id

REMARK Glenn: Also add raw SQL string and approach, check best practise on this site, bind userinput to columns 
https://www.quantifiedcode.com/knowledge-base/security/Prevent%20SQL%20injections%20by%20avoiding%20string%20interpolations/3cObiWuF

	"""
	SQL raw string approach
	"""
	from sqlalchemy import text

	sql = text('select name from penguins')
	result = db.engine.execute(sql)

	print result[0]

