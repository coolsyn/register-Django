from django.db import models
from django.contrib import admin
class Participator(models.Model):

    Sname = models.CharField(max_length=10, blank=False)
    Sid = models.CharField(max_length=20, blank=False)
    Sex = models.CharField(max_length=4, blank=False)
    Department = models.CharField(max_length=100, blank=False)
    Major_class = models.CharField(max_length=100, blank=False)
    Phone_number = models.CharField(max_length=20, blank=False)
    Email = models.EmailField()
    Declaration = models.CharField(max_length=200, blank=False)
    Resume = models.CharField(max_length=100, blank=False)
    Comprehension = models.CharField(max_length=100, blank=False)

    def __str__(self):
       return self.Name
class ParticipatorAdmin(admin.ModelAdmin):
 list_display = ('Sname','Department','Sid','Sex','Major_class','Email','Phone_number','Declaration','Resume','Comprehension')

admin.site.register(Participator,ParticipatorAdmin)