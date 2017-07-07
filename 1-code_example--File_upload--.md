File upload
-------

**Example:**

	import os
	from flask import render_template, flash
	from flask import Flask, render_template,request, redirect
	from flask import url_for,send_from_directory
	from werkzeug.utils import secure_filename

	#Path to the upload directory
	app.config['UPLOAD_FOLDER'] = 'uploads/'
	#Extensions which are accepted to be uploaded
	app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'pdf'])

	#Check whether the file can be uploaded
	def allowed_file(filename):
	    return '.' in filename and \
	           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

	#File upload route
	@app.route('/upload', methods=['POST'])
	def upload_file():
	    # Check if the post request has the file part
	    if 'file' not in request.files:
	        flash('No file part')
	        return redirect(request.url)
	    # Get the name of the uploaded file
	    file = request.files['file']
	    # Submit a empty part without filename
	    if file.filename == '':
	        flash('No selected file')
	        return redirect(request.url)
	    # Check if the file is one of the allowed types/extensions
	    if file and allowed_file(file.filename):
	        # Make the filename safe, remove unsupported chars
	        filename = secure_filename(file.filename)
	        # Move the file form the temporal folder to
	        # the upload folder we setup
	        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	        # Redirect the user to the uploaded_file route, which
	        # will basicaly show on the browser the uploaded file
	        return redirect(url_for('uploaded_file', filename=filename))
	    else:
	        flash('Not allowed extensions')
	        return redirect(request.url)

	@app.route('/uploads/<filename>')
	def uploaded_file(filename):
	    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
	