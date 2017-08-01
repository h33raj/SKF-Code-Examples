
Content type headers
-------

**Example:**

REMARK Glenn: Please explain when you would use this header and add the header for JSON and you need to enforce the JSON header because of XSS etc.

	#Content Type Header
	response.headers["Content-Type"] = "text/html; charset=UTF-8"
    return response
