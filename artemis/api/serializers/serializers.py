from enum import Enum

from rest_framework import serializers
from rest_framework.response import Response


class TypeResult(Enum):
    ERROR = 'ERR'
    EXCEPTION = 'EXC'
    SUCCESS = 'OK'


class ErrorSerializer(serializers.Serializer):
    type_err = serializers.CharField()
    message_err = serializers.CharField()


class APIResponseSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=[(tag.value, tag.name) for tag in TypeResult])
    message = serializers.CharField()
    data = serializers.DictField(required=False, allow_null=True)
    err_info = ErrorSerializer(many=True, required=False)


class APIResponse(Response):

    def __init__(self, type_result: TypeResult, message_result, status=200, data=None, error_info=None):
        response_data = {
            'type': type_result.value,
            'message': message_result,
            'data': data,
            'err_info': error_info
        }
        super().__init__(data=response_data, status=status)
