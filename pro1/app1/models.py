from django.db import models
from django.core import validators

def check(n):
    if n.istitle()!=True:
        validators.ValidationError('eeeeee')
# Create your models here.
class Content(models.Model):
    cid = models.IntegerField(primary_key=True,
                              validators=[validators.MinValueValidator(1),
                                          validators.MaxValueValidator(200)])
    title = models.CharField(max_length=200,
                             validators=[check])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)