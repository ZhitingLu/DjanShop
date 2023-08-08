from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from decouple import config
import braintree

environment = config('BRAINTREE_ENVIRONMENT', default=braintree.Environment.Sandbox)
merchant_id = config('BRAINTREE_MERCHANT_ID')
public_key = config('BRAINTREE_PUBLIC_KEY')
private_key = config('BRAINTREE_PRIVATE_KEY')

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
      environment,
      merchant_id=merchant_id,
      public_key=public_key,
      private_key=private_key
  )
)

def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({
            'error': 'Invalid session, please login again'
        })
    return JsonResponse({
        'clientToken': gateway.client_token.generate(),
        'success': True
    })

