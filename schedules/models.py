from django.db import models

from layout.models import BasicModel
from users.models import User


class Workspace(BasicModel):
    title = models.CharField(max_length=256, verbose_name='제목')
    detail = models.TextField(null=True, blank=True, verbose_name='본문')
    leader = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, blank=True, verbose_name='책임자',
                               related_name='workspace_leader')
    attendees = models.ManyToManyField(User, verbose_name='참여자', blank=True,
                                       related_name='workspace_attendees')

    class Meta:
        verbose_name = '업무'
        ordering = ['-status', 'title']

    def __str__(self):
        return self.title


class ScheduleCategory(BasicModel):
    name = models.CharField(max_length=128, verbose_name='카테고리')

    class Meta:
        verbose_name = '일정구분'
        ordering = ['-status', 'name']

    def __str__(self):
        return self.name


class Schedule(BasicModel):
    title = models.CharField(max_length=256, verbose_name='제목')
    detail = models.TextField(null=True, blank=True, verbose_name='본문')
    started = models.DateTimeField(verbose_name='시작일시')
    ended = models.DateTimeField(verbose_name='종료일시')
    category = models.ForeignKey(ScheduleCategory, on_delete=models.SET_NULL,
                                 null=True, blank=True, verbose_name='일정구분')
    workspace = models.ForeignKey(Workspace, on_delete=models.SET_NULL,
                                  null=True, blank=True, verbose_name='업무')
    attendees = models.ManyToManyField(User, verbose_name='참석자', blank=True)

    class Meta:
        verbose_name = '일정'
        ordering = ['-status', 'pk']

    def __str__(self):
        return self.title
