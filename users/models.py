from django.db import models
from django.contrib.auth.models import User
from PIL import Image

PICTURE_SIZE = (300, 300)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > PICTURE_SIZE[0] or img.width > PICTURE_SIZE[1]:
            img.thumbnail(PICTURE_SIZE)
            img.save(self.image.path)
