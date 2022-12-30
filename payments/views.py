import base64
# Create your views here.
import os

import requests
from django.shortcuts import render
from gerencianet import Gerencianet

credentials = {
    "client_id": os.environ.get('CLIENT_ID'),
    "client_secret": os.environ.get('CLIENT_SECRET'),
}

certificado = 'credentials/certificate/homologacao-429610-certficate.pem'


def home(request):
    auth = base64.b64encode(
        (f"{credentials['client_id']}:{credentials['client_secret']}"
         ).encode()).decode()

    # Para ambiente de Desenvolvimento
    url = "https://api-pix-h.gerencianet.com.br/oauth/token"

    payload = "{\r\n    \"grant_type\": \"client_credentials\"\r\n}"
    headers = {
        'Authorization': f"Basic {auth}",
        'Content-Type': 'application/json'
    }

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=payload,
                                cert=certificado)

    print(response.text)
    return render(request, 'payments/pages/home.html')
