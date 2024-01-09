from django.shortcuts import redirect
from django.contrib import messages


def user_is_superuser(function=None, redirect_url="users:login"):

    def decorator(view_func):
        
        def _wrapper_view(request, *args, **kwargs):
            if not request.user.is_superuser:
                messages.error(request, "Kamu tidak dizikan akses kesini bro!") 
                return redirect(redirect_url)
            
            return view_func(request, *args, **kwargs)
        
        return _wrapper_view
    
    if function:
        return decorator(function)
    
    return decorator