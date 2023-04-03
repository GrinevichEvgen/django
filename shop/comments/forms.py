
from django import forms
from django.conf import settings

from comments import models


class AddCommentForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=1000, widget=forms.Textarea)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                               related_name="comments")
