from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    description = models.TextField(max_length=250,  verbose_name='Описание')
    created_fild = models.DateTimeField(auto_now_add=True, verbose_name='Дата подключения датчика')
    update_fild = models.DateTimeField(auto_now=True, verbose_name='Дата обновления датчика')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_fild = models.DateTimeField(auto_now_add=True,  verbose_name='Дата внесения показаний')
    update_fild = models.DateTimeField(auto_now=True, verbose_name='Дата обновления датчика')

    def __str__(self):
        return str(self.sensor_id)