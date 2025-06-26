from django.shortcuts import render

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            return render(request, '404.html', status=404)
        return response
import base64
from django.http import HttpResponse

class BasicAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.username = "admin"  # ✅ Replace with your username
        self.password = "supersecret"  # ✅ Replace with your password

    def __call__(self, request):
        if request.path.startswith('/swagger') or request.path.startswith('/redoc'):
            auth_header = request.META.get('HTTP_AUTHORIZATION')
            if auth_header:
                try:
                    method, credentials = auth_header.split(' ', 1)
                    if method.lower() == 'basic':
                        decoded = base64.b64decode(credentials).decode('utf-8')
                        input_username, input_password = decoded.split(':', 1)
                        if input_username == self.username and input_password == self.password:
                            return self.get_response(request)
                except Exception as e:
                    pass

            response = HttpResponse("Unauthorized", status=401)
            response['WWW-Authenticate'] = 'Basic realm="Swagger Access"'
            return response
        else:
            return self.get_response(request)
