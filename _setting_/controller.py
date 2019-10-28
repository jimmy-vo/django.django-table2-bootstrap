from django.http import JsonResponse
from log import controller as log_controller

def json_get_ok(data):
    return JsonResponse({
        'result': True,
        'data': data
    })


def json_get_error(error):
    error = str(error)
    log_controller.create(log_type_id=1, info=error)
    return JsonResponse({
        'result': error,
        'data': 'None'
    })
