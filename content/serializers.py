from rest_framework import serializers

from .models import Formulario_CNAB


class CNABSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tipo = serializers.CharField()
    data = serializers.CharField()

    natureza = serializers.CharField()
    sinal = serializers.CharField()
    
    valor = serializers.CharField()
    cpf = serializers.CharField()
    cartao = serializers.CharField()
    hora = serializers.CharField()
    dono_nome = serializers.CharField()
    nome_loja = serializers.CharField()

    def create(self, validated_data):

        criar_formulario = Formulario_CNAB.objects.get_or_create(**validated_data)

        return {"mensagen":"foi um sucesso"}
