from django.shortcuts import render
from.models import Topic


def index(request):
    """
    Shows the homepage of the RCF website.
    """
    page_title = "Home"
    return render(request, 'index.html', {'page_title': page_title})


def volunteer(request):
    """
    Shows the page of the RCF website on volunteer resources. 
    """
    page_title = "Volunteer Resources"
    return render(request, 'volunteer.html', {'page_title': page_title})


def help(request):
    """
    Shows the webpage on how to get involved with the RCF.
    """
    page_title = "How to Help"
    return render(request, 'help.html', {'page_title': page_title})

def donate(request):
    """
    Shows a page on how to donate to the RCF.
    """
    page_title = "Donation Guide"
    return render(request, 'donate.html', {'page_title': page_title})


def messageboard(request):
    """
    Shows the RCF forum.
    """
    page_title = "Forum"
    topics = Topic.objects.order_by('-date_added')
    context = {'page_title': page_title,
        'topics': topics}
    return render(request, 'messageboard.html', context)


def topic(request, topic_id): 
    """
    Show posts within a topic.
    """ 
    topic = Topic.objects.get(id=topic_id) 
    posts = topic.post_set.order_by('-date_posted')
    page_title= Topic.title
    context = {'topic': topic, 'posts': posts, 'page_title': page_title} 
    return render(request, 'topic.html', context)


def contact(request):
    """
    Shows a page to contact RCF.
    """
    page_title = "Contact Us"
    return render(request, 'contact.html', {'page_title': page_title})