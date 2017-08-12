# Logout function
-------

## Example:

    """
    This way, the logout functionality will revoke the complete session:
    """
  
    from django.contrib.auth import logout

    def logout_view(request):
        
        logout(request)
        # Redirect to a success page.