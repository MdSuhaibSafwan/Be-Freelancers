from django.db import models
from django.contrib.auth import get_user_model
from base_lib.model import BaseModel
from account.models import Developer, Client

User = get_user_model()


class Job(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="jobs")
    open = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"Job: {self.title}"


class JobQuestion(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="questions")
    question = models.CharField(max_length=300)

    def __str__(self):
        return f"Question: {self.question}"


class Proposal(BaseModel): 
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    job_question = models.ForeignKey(JobQuestion, on_delete=models.CASCADE, null=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    content = models.TextField()
    files = models.FileField(null=True, upload_to="proposal/docs")

    class Meta:
        unique_together = [["job", "developer"], ["job_question", "developer"]]


class JobInvite(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="invites")
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="got_invited")
    text = models.TextField(null=True)

    class Meta:
        unique_together = ["job", "developer"]

    def __str__(self):
        return f"Invites: {self.job} --> {self.developer}"


class JobRating(BaseModel):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="rating")
    client_rating = models.PositiveSmallIntegerField(null=True)
    client_message = models.TextField(null=True)
    client_rating_posted = models.DateTimeField(null=True)
    developer_rating = models.PositiveSmallIntegerField(null=True)
    developer_message = models.TextField(null=True)
    developer_rating_posted = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.job)
