from pyexpat import model
from django.db import models
from base_lib.model import BaseModel
from django.contrib.auth import get_user_model
from account.models import Developer, Client

User = get_user_model()


class Gig(BaseModel):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="gigs")
    title = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    content = models.TextField()
    # search_keywords = models.ManyToManyField(Skills)

    def __str__(self):
        return f"Gig: {self.title}"

    class Meta:
        unique_together = ["developer", "title"]


class FamiliarGigQuestion(BaseModel):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, related_name="questions")
    question = models.CharField(max_length=100)
    answer = models.TextField()

    class Meta:   
        unique_together = ["gig", "question"]
