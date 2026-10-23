from rest_framework import exceptions, status
from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return None

    if isinstance(exc, exceptions.NotAuthenticated):
        response.data["detail"] = "Для выполнения этого действия необходимо войти"
    elif isinstance(exc, exceptions.PermissionDenied):
        response.data["detail"] = "У вас недостаточно прав для этого действия"
    elif isinstance(exc, exceptions.NotFound):
        response.data["detail"] = "Запрошенный объект не найден"

    if response.status_code == status.HTTP_400_BAD_REQUEST:
        response.data.setdefault("detail", "Проверьте правильность переданных данных")

    return response
