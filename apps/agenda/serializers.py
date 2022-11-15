from rest_framework import serializers

from apps.agenda.models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    lat_origen = serializers.IntegerField(min_value=0, max_value=100)
    lng_origen = serializers.IntegerField(min_value=0, max_value=100)

    class Meta:
        model = Agenda
        fields = [
            'id',
            'cliente',
            'conductor',
            'fecha',
            'hora',
            'lat_origen',
            'lng_origen',
            'destino'
        ]
        read_only_fields = ['id', 'cliente']

    def create(self, validated_data):
        validated_data['fecha_hora'] = f"{validated_data['fecha']} {validated_data['hora']}"
        request = self.context.get("request")
        validated_data['cliente'] = request.user.usuario_cliente
        return super().create(validated_data)
