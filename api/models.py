'''
from django.db import models


class Block(models.Model):
    title = models.CharField(max_length=200, unique=True,
                             verbose_name='раздел')
    tasks = models.CharField(max_length=248, unique=True,
                             blank=True, verbose_name='задача')
    is_active = models.BooleanField(verbose_name='активность', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Executor(models.Model):
    responsible_executor = models.CharField(max_length=100,
                                            verbose_name='ответственный')

    def __str__(self):
        return self.responsible_executor

    class Meta:
        verbose_name = 'Ответственный'
        verbose_name_plural = 'Ответственные'


class Task(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE,
                              verbose_name='задача')
    task_content = models.TextField(verbose_name='подзадача')
    deadline = models.DateField(verbose_name='срок выполнения')
    update = models.DateField(auto_now=True, verbose_name='дата обновления')
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE,
                                 verbose_name='ответственный исполнитель')
    task_price = models.PositiveSmallIntegerField(default=0)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_content

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

'''
