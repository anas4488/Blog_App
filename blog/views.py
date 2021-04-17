from django.shortcuts import render

posts = [
    {
        'author':'user1',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'17 th April, 2021'
    },
    {   'author':'user2',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'17 th April, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})