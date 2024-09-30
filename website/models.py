from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Model representing a blog post.

    Attributes:
        title (str): The title of the post, with a maximum length of 100 characters.
        content (str): The content of the post, stored as text.
        author (User): A foreign key to the User model, representing the post's author.
        created_at (datetime): The date and time when the post was created, 
                               automatically set on creation.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the Post, which is the title."""
        return self.title
