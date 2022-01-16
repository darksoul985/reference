from django.contrib import admin
from .models import Block, Task, Executer, Subtask, Progress


admin.site.register(Block)
admin.site.register(Task)
admin.site.register(Executer)
admin.site.register(Subtask)
admin.site.register(Progress)
