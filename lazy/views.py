from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from lazy.models import lazy_links
from django.contrib.auth.models import User
from django.conf import settings
import uuid
import base64
# Create your views here.

host= settings.LAZY_LOGIN.get('HOST','localhost')
port= settings.LAZY_LOGIN.get('PORT', 8000)

class lazy_login(View):

    def get_key(self,*args,**kwargs):
        key = base64.urlsafe_b64encode(uuid.uuid4().bytes).replace('=', '')
        return key

    def get_user(self,email):
        try:
            user=User.objects.get(email=email)
            return user
        except:
            return None

    def check_lazy(self,*args,**kwargs):
        pass

    def get(self, request):
        key= request.GET.get('key')
        pass

    def post(self,request):
        email= request.POST.get('email')
        user= self.get_user(email)
        key= self.get_key()
        new_link= "{}:{}/?key={}&user={}".format(host, port, key, user.id)
        return HttpResponse(new_link)
