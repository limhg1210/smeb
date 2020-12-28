from django.db import models


class Setting(models.Model):
    name = models.CharField(max_length=200)
    logo_img = models.ImageField(blank=True, upload_to='layout')

    def __str__(self):
        return f'{self.name} 설정'
