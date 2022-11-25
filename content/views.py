from rest_framework.views import APIView, Response
# from django.forms.models import model_to_dict
from .serializers import CNABSerializer
#  autopep8

class fazerUpload(APIView):

    def post(self, request):
        arquivo = request.FILES["file"]

        linhas = arquivo.readlines()

        for i in linhas:

            tipo = i.decode("utf-8")[0:1]
            natureza = "Entrada"
            sinal = "+"

            if (tipo == "1"):
                tipo = "Débito"

            if (tipo == "2"):
                natureza = "Saída"
                sinal = "-"
                tipo = "Boleto"

            if (tipo == "3"):
                natureza = "Saída"
                sinal = "-"
                tipo = "Financiamento"

            if (tipo == "4"):
                tipo = "Crédito"

            if (tipo == "5"):
                tipo = "Recebimento Empréstimo"

            if (tipo == "6"):
                tipo = "Vendas"

            if (tipo == "7"):
                tipo = "Recebimento TED"

            if (tipo == "8"):
                tipo = "Recebimento DOC"

            if (tipo == "9"):
                natureza = "Saída"
                sinal = "-"
                tipo = "Aluguel"

            data = i.decode("utf-8")[1:9]
            ajustar_data = f"{data[6:8]}/{data[4:6]}/{data[0:4]}"

            valor = i.decode("utf-8")[9:19]
            ajustar_valor = int(valor)/100.00

            cpf = i.decode("utf-8")[19:30]

            cartao = i.decode("utf-8")[30:42]

            hora = i.decode("utf-8")[42:48]
            ajustar_hora = f"{hora[0:2]}:{hora[2:4]}:{hora[4:6]}"

            dono_nome = i.decode("utf-8")[48:62]

            nome_loja = i.decode("utf-8")[62:81]

            dados_da_transasao = {"tipo": tipo, "data": ajustar_data,
                                  "valor": ajustar_valor, "cpf": cpf,
                                  "cartao": cartao, "hora": ajustar_hora,
                                  "dono_nome": dono_nome, "nome_loja": nome_loja,
                                  "natureza": natureza, "sinal": sinal}

            Serializer = CNABSerializer(data= dados_da_transasao)
            Serializer.is_valid(raise_exception=True)
            Serializer.save()

        return Response({"mensagen":"sucesso dados foram colocados no banco"})
