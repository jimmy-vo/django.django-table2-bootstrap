from django.utils.dateparse import parse_date
from dateutil import parser

class Validator:
    @staticmethod
    def existing_primary_key(id, model, exception_message="The id is not found."):
        if id is None:
            raise Exception(exception_message)
        if not model.objects.filter(id=id).exists():
            raise Exception(exception_message)
        return int(id)

    @staticmethod
    def is_not_empty(data, exception_message="Cannot be empty."):
        if data is None:
            raise Exception(exception_message)
        if len(data) < 1:
            raise Exception(exception_message)
        return data

    @staticmethod
    def is_decimal(data, exception_message="Must be decimal number."):
        try:
            data = float(data)
            return data
        except:
            raise Exception(exception_message)

    @staticmethod
    def is_date(data, exception_message="Must be a date."):
        try:
            data = parse_date(data)
            return data
        except:
            raise Exception(exception_message)

    @staticmethod
    def is_datetime(data, exception_message="Must be a datetime."):
        try:
            data = parser.parse( data)
            return data
        except:
            raise Exception(exception_message)
