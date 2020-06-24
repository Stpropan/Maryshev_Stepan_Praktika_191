import datetime
from django.db import models

from django.utils import timezone

class Medicine(models.Model):
    medicine_name = models.CharField('Название препарата', max_length = 300)
    quanity = models.PositiveSmallIntegerField('Количетво', default = 0)
    checklist = models.CharField('список', max_length = 4)
    medicine_description = models.TextField('описание')

    def __str__(self):
        return self.medicine_name
        
    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'
        
class Doctor(models.Model):
    doctor_name = models.CharField('ФИО врача', max_length = 100)
    doctor_schedule = models.CharField('График работы', max_length = 200)
    doctor_description = models.TextField('Дополнительная информация')
    doctor_image = models.ImageField('Изображение врача', upload_to='doctors/')
    
    def __str__(self):
        return self.doctor_name
        
    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        
class Patient(models.Model):
    patient_name = models.CharField('Имя пациента', max_length = 100)
    patient_information = models.TextField('Данные пациента')
    medical_Card = models.TextField('Медицинская карта')

    def __str__(self):
        return self.patient_name
        
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        
class Comment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 500)
    
    def __str__(self):
        return self.author_name
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'