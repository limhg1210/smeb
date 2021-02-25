from django.contrib.auth.models import AbstractUser
from django.db import models

from layout.models import BasicModel


class User(AbstractUser, BasicModel):
    first_name = None
    last_name = None
    date_joined = None

    name = models.CharField(max_length=64, default='', verbose_name='이름')
    nickname = models.CharField(max_length=64, default='', blank=True, verbose_name='닉네임')
    duty = models.CharField(max_length=256, default='', blank=True, verbose_name='직책')
    phone = models.CharField(max_length=64, default='', blank=True, verbose_name='전화번호')
    email = models.EmailField(max_length=256, default='', blank=True, verbose_name='이메일')
    join_date = models.DateField(verbose_name='입사일', null=True, blank=True)
    leave_date = models.DateField(verbose_name='퇴사일', null=True, blank=True)
    photo = models.FileField(upload_to='profile_photo/',
                             default='default/profile_photo.png',
                             blank=True,
                             verbose_name='프로필사진')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='user_set', verbose_name='부서')
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='user_set', verbose_name='직위')

    class Meta:
        verbose_name = '회원'
        ordering = ['-status', 'pk']

    def save(self, *args, **kwargs):
        self.is_active = self.status
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Department(BasicModel):
    name = models.CharField(max_length=64, default='', verbose_name='부서명')
    level = models.IntegerField(default=0, verbose_name='레벨')
    manager = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='managing_department_set', verbose_name='부서장')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='child_department_set', verbose_name='상위부서')

    class Meta:
        verbose_name = '부서'
        ordering = ['-status', 'level', 'name']

    def __str__(self):
        return self.name


class Position(BasicModel):
    name = models.CharField(max_length=64, default='', verbose_name='직위명')
    level = models.IntegerField(default=0, verbose_name='레벨')
    wage = models.IntegerField(default=0, verbose_name='평균시급')

    class Meta:
        verbose_name = '직위'
        ordering = ['-status', 'level', 'name']
