import django.utils.timezone as tz

from _setting_ import controller
from _setting_.validator import Validator
from .models import Log, LogType


def validate_info_not_empty(request):
    return Validator.is_not_empty(
        data=request.GET.get('info', None),
        exception_message='Info cannot be empty.'
    )


def validate_id_exists(request):
    return Validator.existing_primary_key(
        id=request.GET.get('id', None),
        model=Log,
        exception_message='The id is not found.'
    )


def validate_fk_exists(request):
    return Validator.existing_primary_key(
        id=request.GET.get('log_type_id', None),
        model=LogType,
        exception_message='The fk is not found.'
    )

def validate_all(request):
    id = validate_id_exists(request)
    info = validate_info_not_empty(request)
    log_type_id = validate_fk_exists(request)
    return id, info, log_type_id


def update_with_id(id, info, log_type_id):
    target = Log.objects.get(id=id)
    target.log_type_id = log_type_id
    target.info = info
    target.save()
    return target


def delete_with_id(id):
    target = Log.objects.get(id=id)
    target.delete()


def get_json_error(error):
    return controller.json_get_error(error=error)


def get_json_ok(target):
    return controller.json_get_ok({
        'id': target.id,
        'time': target.time,
        'info': target.info,
    })


def create(log_type_id, info):
    target = Log(time=tz.localtime(), info=info, log_type_id=log_type_id)
    target.save()
    return target
