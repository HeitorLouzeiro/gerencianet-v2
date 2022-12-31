# Create your views here.
from django.shortcuts import redirect, render
from gerencianet import Gerencianet

from credentials.credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


def home(request):
    return render(request, 'payments/pages/home.html')


def bank_billet(request):
    if request.method == 'POST':
        data = {
            'items': [
                {
                    'name': 'Course Programming',
                    'value': 100000,
                    'amount': 1,
                }
            ],
        }
        body = {
            'payment': {
                'banking_billet': {
                    'expire_at': '2023-01-01',
                    'customer': {
                        'name': 'Gorbadoc Oldbuck',
                        'cpf': '04267484171',
                        'phone_number': '5144916523',
                        'email': 'exemple@gmail.com',
                    },
                }
            },
            'items': data['items'],
        }
        response = gn.create_charge_onestep(params=None, body=body)
        link = response['data']['link']
        return redirect(link)


def carnet(request):
    if request.method == 'POST':
        data = {
            'items': [
                {
                    'name': 'Course Programming',
                    'value': 25000,
                    'amount': 1,
                }
            ],
        }
        body = {
            'customer': {
                'name': 'Gorbadoc Oldbuck',
                        'cpf': '04267484171',
                        'phone_number': '5144916523',
                        'birth': '1977-01-15',
                        'email': 'exemple@gmail.com',
            },
            'repeats': 4,
            'expire_at': '2023-01-01',
            'items': data['items'],
        }
        response = gn.create_carnet(params=None, body=body)
        carnet_link = response['data']['carnet_link']
        return redirect(carnet_link)


def credit_card(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        data = {
            'items': [
                {
                    'name': 'Course Programming',
                    'value': 25000,
                    'amount': 1,
                }
            ],
        }
        body = {
            'payment': {
                'credit_card': {
                    'installments': 4,
                    'payment_token': token,
                    'billing_address': {
                        'street': "Av. JK",
                        'number': 909,
                        'neighborhood': "Bauxita",
                        'zipcode': "35400000",
                        'city': "Ouro Preto",
                        'state': "MG"
                    },
                    'customer': {
                        'name': 'Gorbadoc Oldbuck',
                        'cpf': '04267484171',
                        'phone_number': '5144916523',
                        'birth': "1977-01-15",
                        'email': 'exemple@gmail.com',
                    },
                }
            },
            'items': data['items'],
        }
        response = gn.create_charge_onestep(params=None, body=body)
        print(response)
        return redirect('home')
