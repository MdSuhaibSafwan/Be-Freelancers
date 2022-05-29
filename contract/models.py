from django.db import models
from base_lib.model import BaseModel
from django.contrib.auth import get_user_model
from job.models import Job, Proposal
from gig.models import Gig
from account.models import Client, Developer

User = get_user_model()


class Contract(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    gig = models.ForeignKey(Gig, on_delete=models.SET_NULL, related_name="gig_contracts", null=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, related_name="job_contracts", null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Contract: {self.id}"