from django.contrib.auth.models import User
from django.views.generic.edit import View
from django.http import JsonResponse


class ValidateUsernameView(View):
    def get(self, request):
        username = request.GET.get('username', None)
        data = {
            'is_present': User.objects.filter(username__iexact=username).exists()
        }
        return JsonResponse(data)
