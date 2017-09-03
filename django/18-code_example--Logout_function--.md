# Logout function
-------

## Example:

    """
    This way, the logout functionality will revoke the complete session:
    """
  
    from django.contrib.auth import logout

    def logout_view(request):
        
        # Logging logout
        log.info('Logout Successful : {user} via ip: {ip}'.format(
            user=user,
            ip=ip
        ))

        logout(request)
        # Redirect to a success page.