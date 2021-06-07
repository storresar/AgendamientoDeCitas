from  .models import parametrizacion
from rest_framework import serializers
from django.utils import timezone

class parametrizacion_serializer(serializers.ModelSerializer):
    class Meta():
        model = parametrizacion
        fields = ('id','nombre', 'fecha_inicio', 'fecha_fin', 'valor', 'estado')
        read_only_fields = ('estado',)
        
    def create(self, validated_data):
        nombre = validated_data['nombre']
        f_inicio = validated_data['fecha_inicio']
        f_fin = validated_data['fecha_fin']

        activo = False

        if timezone.now().date() >= f_inicio:
            activo = True

        mismos_parametros = parametrizacion.objects.filter(nombre=nombre)

        entra = True

        for i in mismos_parametros:
            print(f_inicio, i.fecha_fin)
            if f_inicio < i.fecha_fin:
                print("1")
                entra = False

        if f_inicio > f_fin:
            print("3")
            entra = False
        
        if entra == True:
            
            obj = parametrizacion(nombre=nombre,
                fecha_inicio=f_inicio,
                fecha_fin=f_fin,
                valor = validated_data['valor'],
                estado=activo)
            obj.save()
            return obj
        else:
            raise serializers.ValidationError('No se pueden ingresar el mismo parametro con una fecha existente',code = 400)



