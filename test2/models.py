from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()
from test1.models import Post

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} -> {self.post.title}[{self.created_at}]"