from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        # TODO: Delete the original file before saving the new file
        super().save()

        img = Image.open(self.image.path)

        MAX_THUMBNAIL_SIZE = (300, 300)
        if img.height > MAX_THUMBNAIL_SIZE[0] or img.width > MAX_THUMBNAIL_SIZE[1]:
            img.thumbnail(MAX_THUMBNAIL_SIZE)
            img.save(self.image.path)
