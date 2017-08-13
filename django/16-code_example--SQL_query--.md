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



	from flask_sqlalchemy import SQLAlchemy
	
	#Will track modifications of objects and emit signals
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	#Database URI is used for connection
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
	#Create object of SQL Alchemy
	db = SQLAlchemy(app)

	#Class Model that is a declarative base which can be used to declare models
	class User(db.Model):
    	id = db.Column(db.Integer, primary_key=True)
    	username = db.Column(db.String(80), unique=True, nullable=False)
    	password = db.Column(db.String(120), unique=True, nullable=False)

    	def __repr__(self):	
        	return '<User %r>' % self.username

    """
    create the tables and database
    """
    from yourapplication import db
	db.create_all()

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

