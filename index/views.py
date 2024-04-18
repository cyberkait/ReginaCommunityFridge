from django.shortcuts import render
from.models import Topic


def index(request):
    return render(request, 'index.html')


def volunteer(request):
    return render(request, 'volunteer.html')


def help(request):
    return render(request, 'help.html')

def donate(request):
    return render(request, 'donate.html')


def messageboard(request):
    topics = Topic.objects.order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'messageboard.html', context)


def topic(request, topic_id): 
    """
    Show posts within a topic.
    """ 
    topic = Topic.objects.get(id=topic_id) 
    posts = topic.post_set.order_by('-date_posted')
    context = {'topic': topic, 'posts': posts} 
    return render(request, 'topic.html', context)


def contact(request):
    return render(request, 'contact.html')