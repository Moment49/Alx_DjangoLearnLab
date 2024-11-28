# Implemented the best security principles 
# First checked if the security middleware is installed and available
# Next set your the following flags Debug = False this is to hide the errors which might be visible to the users or attacker allowing them to see what is wrong with the application
# Set up the following below
# SECURE_BROWSER_XSS_FILTER = True - This is to filter for an malicious code that can be injected to our site to steal info
# X_FRAME_OPTIONS = 'DENY' - This is to prevent clickjacking of our application so that malicious code won't be run on the background
# SECURE_CONTENT_TYPE_NOSNIFF = True - This is to ensure that the client upon recieving the request from the server does not alter the file content or content type of resources
# CSRF_COOKIE_SECURE = True - This is to ensure that the CSRF cookie(token) sent is secure on encrypted 
# SESSION_COOKIE_SECURE = True - This is tp ensure that the session is secure

# Next the Django-csp (Content security policy) was configured
# The flag set is to ensure that the only resources coming from the application or allowing third-app references can be loaded

# Content Security Policy
# CSP_IMG_SRC = ("'self'", 'https://html.sammy-codes.com')

# CSP_STYLE_SRC = ("'self'")

# CSP_SCRIPT_SRC = ("'self'")