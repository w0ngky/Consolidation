from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.http import HttpResponse

def home(request):
    """Render the home page."""
    return render(request, 'home.html')

def about(request):
    """Render the about page."""
    return render(request, 'about.html')

def contact(request):
    """Render the contact page."""
    return render(request, 'contact.html')

def blog(request):
    """Render the blog page with a list of all posts.

    Retrieves all blog posts and passes them to the 'blog.html' template.
    """
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, post_id):
    """Render a specific blog post's detail page.

    Args:
        post_id (int): The ID of the post to retrieve.

    Returns:
        HttpResponse: Renders the 'post_detail.html' template with the post data.
    """
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def register(request):
    """Handle user registration.

    If the request is POST, validate and save the user form.
    If the request is GET, display an empty registration form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    """Handle user login.

    If the request is POST, authenticate the user with the provided credentials.
    If authentication is successful, log the user in and redirect to the home page.
    If not, return to the login page with an error message.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    """Log the user out and redirect to the home page with a logout message."""
    logout(request)
    messages.info(request, 'You have logged out.')
    return redirect('home')

def subscribe(request):
    """Handle email subscription.

    If the request is POST, retrieve the email and process the subscription logic.
    Return a thank-you message.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        # Handle email subscription logic here
        return HttpResponse('Thank you for subscribing!')
    return render(request, 'subscribe.html')
