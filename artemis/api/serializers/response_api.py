from artemis.api.serializers.serializers import APIResponse, TypeResult


class SuccessResponse(APIResponse):
    def __init__(self, message, data=None):
        super().__init__(TypeResult.SUCCESS, message, data=data)


class RequiredDataException(APIResponse):

    def __init__(self, missing_fields):
        fields_str = ', '.join(missing_fields)
        error_info = {
            'type_err': 'RequiredData',
            'message_err': f'Required data: ({fields_str})'
        }
        super().__init__(TypeResult.ERROR, 'Required data missing', error_info=error_info)


class InvalidCredentialsException(APIResponse):

    def __init__(self, fields):
        fields_str = ', '.join(fields)
        error_info = {
            'type_err': 'InvalidCredentials',
            'message_err': f'Check the data in the fields: ({fields_str})'
        }
        super().__init__(TypeResult.ERROR, 'Invalid credentials', error_info=error_info)
