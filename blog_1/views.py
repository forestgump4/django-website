from django.shortcuts import render
from django.http import HttpResponse

# dummy data
posts_data = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog postal one',
        'content': 'First post on a this blog by me quoting Corey Schafer',
        'date': 'Marzo 28, 2022, earlier that day'
    },
    {
        'author': 'Israel',
        'title': 'blog post 2',
        'content': 'a blog post part 2',
        'date': 'Marzo 28, 2022, 15:20'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts_key': posts_data
    }
    return render(request, 'blog/Home_page.html', context)


def about(request):
    return render(request, 'blog/About_page.html', {'title': 'The about site'})
