from django.db import models
import uuid
from uuid import uuid4
import os


class Folder(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    create = models.DateField(auto_now=True)


def upload_path(instance, filename):
    return os.path.join(f'uploaded_files/{instance.folder.uid}', filename)


class uploaded_files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_path)
    create = models.DateField(auto_now=True)
