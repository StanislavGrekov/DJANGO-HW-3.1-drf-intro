from rest_framework import serializers
from .models import Sensor, Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_fild']

    # def create(self, validated_data):
    #     return Measurement.objects.create(**validated_data)


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

    # def create(self, validated_data):
    #     return Sensor.objects.create(**validated_data)







# class SensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ['id','name', 'description']
#
# class MeasureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Measurement
#         fields = ['sensor_id', 'temperaturer', 'created_fild']

