from django.db import models
from django.conf import settings


class Setting(models.Model):
    name = models.CharField(max_length=200)
    logo_img = models.ImageField(blank=True, upload_to='layout')

    def __str__(self):
        return f'{self.name} 설정'


class BasicModel(models.Model):
    """
    대부분의 테이블에 필요한 컬럼이 포함된 abstract class.
    대부분 모델은 이 클래스를 상속받아 작성한다.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='this_%(class)s_author', verbose_name='작성자',
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    updated = models.DateTimeField(auto_now=True, verbose_name='수정일시')
    status = models.BooleanField(default=True, verbose_name='활성')

    class Meta:
        abstract = True
