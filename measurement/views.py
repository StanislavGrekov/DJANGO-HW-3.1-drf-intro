# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer

# CreateAPIView – создание данных по POST-запросу; *
# ListCreateAPIView – для чтения (по GET-запросу) и создания списка данных (по POST-запросу); *
# RetrieveUpdateAPIView – чтение и изменение отдельной записи (GET-, PUT- и PATCH-запросы); *

class SensorListCreateAPIView(ListCreateAPIView):
    """Получение всех датчиков"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        """Метод добавляет датчик"""
        new_element = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description'],
        )
        return Response({'info': model_to_dict(new_element)})


class SensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """Получение отдельного датчика и изменение датчика"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementListCreateAPIView(CreateAPIView):
    # queryset = Measurement.objects.all()
    # serializer_class = MeasurementSerializer
    """Добавление измерения"""
    def post(self, request):
        new_element = Measurement(sensor_id_id=request.data['sensor'], temperature=request.data['temperature']).save()
        return Response({'info': model_to_dict(new_element)})




















# class SensorsAPIView(APIView):
#     def get(self, request):
#         """Метод возвращает все датчики"""
#         queryset = Sensor.objects.all()
#         serializer = SensorDetailSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         """Метод добавляет датчик"""
#         new_element = Sensor.objects.create(
#             name=request.data['name'],
#             description=request.data['description'],
#         )
#         return Response({'info': model_to_dict(new_element)})
#
#
# class SensorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     """Метод возращает 1 датчик, обновляет информацию по датчику, удаляет датчик"""
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#
#
# class MeasurementAPIView(APIView):
#
#     # добавление измерения
#     def post(self, request):
#         new_element = Measurement(sensor_id_id=request.data['sensor'], temperature=request.data['temperature']).save()
#         return Response({'info': model_to_dict(new_element)})




# class SensorsAPIView(APIView):
#     def get(self, request):
#         queryset = Sensor.objects.all()
#         serializer = SensorDetailSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         new_element = Sensor.objects.create(
#             name=request.data['name'],
#             description=request.data['description'],
#         )
#         return Response({'post': model_to_dict(new_element)})
#
#


# class SensorsView(ListCreateAPIView):
#         queryset = Sensor.objects.all()
#         serializer_class = SensorDetailSerializer
#
#
#         def post(self, request):
#             serializer = SensorDetailSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({'post': serializer.data})
#
#
#         def delete(self, request, pk, format=None):
#             delete_sensor = self.get_object(pk)
#             delete_sensor.delete()
#             return Response(status=delete_sensor.HTTP_204_NO_CONTENT)
#
# class SensorView(RetrieveUpdateDestroyAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#
#
# class Measurements(ListCreateAPIView):
#         queryset = Measurement.objects.all()
#         serializer_class = MeasurementSerializer
#
#         def post(self, request):
#             serializer = MeasurementSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({'post': serializer.data})