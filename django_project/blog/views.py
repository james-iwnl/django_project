from django.shortcuts import render

posts = [
    {
        'author':'JamesK',
        'title': 'Blog post 1',
        'content':'First post content',
        'date_posted': 'June 20, 2021'
    },
    {
        'author':'Jane Doe',
        'title': 'Blog post 2',
        'content':'Second post content',
        'date_posted': 'August, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')