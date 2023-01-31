from django.core.management.base import BaseCommand
from measurement.models import Sensor, Measurement


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        csm23_oxy_one = Sensor.objects.create(name='CSM23_OXY_one', description= 'Датчик температуры на кухне')
        csm23_oxy_two = Sensor.objects.create(name='CSM23_OXY_two', description= 'Датчик температуры в спальне')
        csm23_oxy_three = Sensor.objects.create(name='CSM23_OXY_three', description= 'Датчик температуры в коридоре')

        csm23_oxy_three.measurements.create(temperature=26.3)
        csm23_oxy_three.measurements.create(temperature=16.9)
        csm23_oxy_three.measurements.create(temperature=27.9)
        csm23_oxy_one.measurements.create(temperature=21.7)
        csm23_oxy_one.measurements.create(temperature=22.9)
        csm23_oxy_one.measurements.create(temperature=24.6)
        csm23_oxy_two.measurements.create(temperature=21.1)
        csm23_oxy_two.measurements.create(temperature=19.9)
        csm23_oxy_two.measurements.create(temperature=17.3)



        # sensors = Sensor.objects.all()
        # for sensor in Sensor.objects.all():
        #     print(f'id сенсора {sensor.id}')
        #     for measure in sensor.measurements.all():
        #         print(measure.sensor_id)


        # students = Student.objects.all()
        # for student in students:
        #     print(student.name)