# Directory listing
-------

## Example:


    """
    To disable or prevent directory access, add following line in your .htaccess file. If
    user points the browsers to a directory that does not have an index file, then a
    "403 Forbidden" error will be displayed:

    Add this line of code to your .htaccess file:
    """

    Options -Indexes

	"""
	Python code to display the files from the uploads folder
	"""

	# Views.py

    def gallery(request, dir_name):
        path = os.path.join(settings.MEDIA_ROOT, dir_name)   
        images = []
        for f in os.listdir(path):
            if f.endswith("jpg") or f.endswith("png"):
                images.append("%s%s/%s" % (settings.MEDIA_URL, dir_name, f))
        return render_to_response('gallery.html', {'images': images})

    # gallery.html

    {% for image in images %}
    <img src='/static/{{image}}' />
    {% endfor %}


