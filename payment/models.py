from django.db import models
from base_lib.model import BaseModel, create_uuid
from django.contrib.auth import get_user_model
from account.models import Client, Developer
from job.models import Job
from django.utils import timezone

User = get_user_model()


class BkashClientPayment(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    job = models.OneToOneField(Job, on_delete=models.SET_NULL, null=True, related_name="payment")
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    transaction_number = models.CharField(editable=False, unique=True, max_length=500)
    bkash_transaction_number = models.CharField(max_length=500, unique=True)
    image1 = models.ImageField(upload_to="bkash/transaction/images/client")
    image2 = models.ImageField(upload_to="bkash/transaction/images", null=True)
    pending = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        tn = self.transaction_number
        if tn is None:
            self.transaction_number = f"{create_uuid()}-{timezone.now()}-{create_uuid()}"

        return super().save(*args, **kwargs)


class BkashToDeveloperPayment(BaseModel):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="bkash_history")
    price = models.PositiveSmallIntegerField()
    phone = models.CharField(max_length=15)
    pending = models.BooleanField(default=True)
    image = models.ImageField(upload_to="bkash/transaction/images/developer")

    bkash_transaction_number = models.CharField(unique=True, max_length=500, null=True)

