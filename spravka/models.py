from django.contrib.auth.models import User
from django.db import models


class Block(models.Model):
    """
    the block tasks
    """
    name = models.CharField(max_length=256, unique=True, verbose_name='название блока задач')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'блок задач'
        verbose_name_plural = 'блоки задач'


class Executer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='ответственный исполнитель')
    # дописать поле как многие ко многим, так как испонителей у задачи может быть много, и задач у исполнителся тоже

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Task(models.Model):
    """
    the task from a block
    """
    block = models.ForeignKey(Block, on_delete=models.PROTECT, verbose_name='блок')
    task_content = models.CharField(max_length=250, verbose_name='задача', blank=False)
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.task_content}'

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'


class Subtask(models.Model):
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    executer = models.ForeignKey(Executer, on_delete=models.PROTECT, verbose_name='ответственный исполнитель')
    date_created = models.DateField(auto_now_add=True, verbose_name='дата подзадачи')
    update = models.DateField(auto_now=True)
    content = models.TextField(verbose_name='содержание подзадачи', blank=False)
    deadline = models.DateField(blank=True, verbose_name='контрольный срок')
    task_cost = models.PositiveSmallIntegerField(verbose_name='с')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'подзадача'
        verbose_name_plural = 'подзадачи'


class Progress(models.Model):
    subtask = models.ForeignKey(Subtask, on_delete=models.CASCADE, verbose_name='прогресс')
    content = models.TextField(verbose_name='что изменилось')
    update_progress = models.DateField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'прогресс'
        verbose_name_plural = 'прогресс'
