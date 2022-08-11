from django.shortcuts import render

posts = [
    {
        'author': 'Konstantin',
        'title': 'Blog post 1',
        'content': 'First post',
        'date_posted': '10 August, 2022'
    },
    {
        'author': 'Alina',
        'title': 'Blog post 2',
        'content': 'Second post',
        'date_posted': '11 August, 2022'
    }

]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
