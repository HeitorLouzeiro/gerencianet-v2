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
