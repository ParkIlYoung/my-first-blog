from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

from pyrebase import pyrebase

config = {
	'apiKey' : "AIzaSyCVNoYOel5Peq4TRjkLdGECrKWMcA1lo0o",
    'authDomain': "kw-lg-test.firebaseapp.com",
    'databaseURL': "https://kw-lg-test.firebaseio.com",
    'projectId': "kw-lg-test",
    'storageBucket': "kw-lg-test.appspot.com",
    'messagingSenderId': "650240921135"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def signIn(request):
	return render(request,"signIn.html")

def postsign(request):
    email=request.POST.get("email")
    passw= request.POST.get("pass")

    user = auth.sign_in_with_email_and_password(email,passw)

    return render(request, "welcome.html", {"e":email})

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})