# HTML output
-------

## Example:

REMARK Glenn: Looks good, please also add output encoding for HTML and JSON, check HTML en JSON Entity encoding https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet#HTML_entity_encoding

    """
    Whenever user input is displayed in the application, whether, as content or a parameter value
    submitted towards the url, all user input should be properly escaped to prevent XSS injections.
    """

    #For normal output this escaping will do the trick
    from flask import escape
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return escape(request.form['name'])

    #This also applies, for instance, when retrieving content from a database:
    @app.route('/')
        admin = User.query.filter_by(username='admin').first()
        return escape(admin.email)
    
    """
    Security consists of different layers of protection, in order to guarantee the integrity
    of your application. This means that the value submitted from the user should
    already be sanitized before being submitted towards the database in order to prevent XSS.
    As an example, you are expecting only alphanumerical value here:
    """
    match = re.findall("^[a-zA-Z0-9]+$", value)
    if match:
        return True
    else:
        raise Exception("User supplied value not in the range " + range)

    """
    This type of approach should be used whenever you are allowing userinput in
    your DOM like for example, let's say a user was allowed to upload an image and
    set an alt text. when you do not sanitize his input a possible attack string could be:
    """
    
    this is an image" onload="alert('XSS');"

    """
    whenever this string now is added to the users image this will be the outcome, leading
    to xss:
    """

    <img src="http://image.com/image.jpg" alt="this is an image" onload="alert('XSS')"" />

    """
    After this sanitation malicious code can no longer exist in the $_POST['value'] variable.

    Another possibility for attackers to execute an XSS injection, is to pass malicious code directly
    into the URL by means of a "href", e.g.:
    javascript:alert(document.cookie);
    or
    data:text/html;base64,base64xssinjection

    In the following scenario escaping with htmlspecialchars() is not sufficient to block the injection.
    By checking the URL to see if it starts with either http:// or https:// whenever a link has
    been submitted to the web application by a user.

    def before_request(url):
        if url.startswith('http://') or url.startswith('https://'):
            return True
        else:
            raise Exception("Not a valid URL : " + url)

    
