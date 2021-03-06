from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from optimized_image.fields import OptimizedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=64, blank=True, null=True)
    image = OptimizedImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folgt = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='folgt', default="", editable=False)

    class Meta:
        unique_together = (("user", "folgt"),)
