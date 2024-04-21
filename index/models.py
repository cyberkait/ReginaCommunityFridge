from django.db import models


class Topic(models.Model):
    """
    Topic of post on message board.
    """
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """
        Returns a string representation of data.
        """
        return self.text


class Post(models.Model): 
    """
    Posts relating to its topic.
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """
        Return a  string representing the post, shortened to 50 characters.
        """
        return f"{self.title[:50]}..."


