from django.db import models

from django.db import models
from django_quill.fields import QuillField


class QuillPost(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()

    def __str__(self):
        return self.title
