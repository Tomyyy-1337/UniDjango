from django.db import models

# Create your models here.

class Student(models.Model):
 matnr = models.IntegerField(unique=True)
 name = models.CharField(max_length=64)
 hoert = models.ManyToManyField('Vorlesung', blank=True)
 def __str__(self):
  return "%s [%s]" % (self.name, self.matnr)
 class Meta:
  verbose_name = 'Student'
  verbose_name_plural = 'Studenten'
  ordering = ('name', 'matnr',)
class Professor(models.Model):
 persnr = models.IntegerField(unique=True)
 name = models.CharField(max_length=64)
 def __str__(self):
  return "%s [%s]" % (self.name, self.persnr)
 class Meta:
  verbose_name = 'Professor'
  verbose_name_plural = 'Professoren'
  ordering = ('name', 'persnr',)
class Vorlesung(models.Model):
 vorlnr = models.IntegerField(unique=True)
 titel = models.CharField(max_length=128)
 dozent = models.ForeignKey(Professor, null=True,
on_delete=models.SET_NULL)
 def __str__(self):
  return "%s [%s]" % (self.titel, self.vorlnr)
 class Meta:
  verbose_name = 'Vorlesung'
  verbose_name_plural = 'Vorlesungen'
  ordering = ('titel', 'vorlnr',)
class Pruefung(models.Model):
 student = models.ForeignKey(Student, on_delete=models.CASCADE)
 vorlesung = models.ForeignKey(Vorlesung, on_delete=models.RESTRICT)
 datum = models.DateField()
 note = models.IntegerField()
 def __str__(self):
  return "%s %s %s [%s]" % (self.student,self.vorlesung,self.note,self.datum)
 class Meta:
  verbose_name = 'Pruefung'
  verbose_name_plural = 'Pruefungen'
  ordering = ('student','vorlesung','note','datum',)
