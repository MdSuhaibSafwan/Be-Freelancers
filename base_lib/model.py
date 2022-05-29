import uuid
from django.db import models


def create_uuid():
    return uuid.uuid4().hex

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=create_uuid, editable=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
