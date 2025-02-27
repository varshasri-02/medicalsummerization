from django.db import models

class Chat(models.Model):
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.message[:50]}... | AI: {self.response[:50]}..."
