from django.db import models
from django.contrib.auth.models import User


class objectTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created_at',)


class Tag(objectTracking):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = []


# Create your models here.
class Question(objectTracking):
    title = models.TextField(null=True, blank=True)
    status = models.CharField(default='inactive', max_length=20)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # it means that one User(hr) can post multiple questions
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey('polls.Question', on_delete=models.CASCADE)
    # this query means question object is coming from the Question model
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    # we are using this proprty to count the no of votes for qustion
    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text
