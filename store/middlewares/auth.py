from django.shortcuts import redirect

def auth_middleware(get_response):
    
    def middleware(request):
        # User jis page par jana chahta hai, uska URL path nikalna
        returnUrl = request.META['PATH_INFO']
        
        # Check karna ki user logged in hai ya nahi (session mein customer id hai ya nahi)
        if not request.session.get('customer'):
            # Agar login nahi hai, toh login page par redirect kar dena
            return redirect(f'/login/?return_url={returnUrl}')
            
        # Agar login hai, toh usko aage badhne dena
        response = get_response(request)
        return response

    return middleware