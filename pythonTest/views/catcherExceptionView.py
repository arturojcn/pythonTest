from pyramid.view import (notfound_view_config, view_config, forbidden_view_config, exception_view_config)
from pyramid.response import Response
from ..exceptions.handlerExceptions import UserExistException


@notfound_view_config(renderer='json')
def notfound_view(request):
    request.response.status = 404
    return {'status': 404, 'message': 'Resource not found!'}

@exception_view_config(Exception, renderer='json')
def any_exception(exc, request):
    body={"status":500, "message":"this is so embarrass, but something was wrong. Please try again in a moment"}
    return Response(json_body=body, status=500 )

@view_config(context=UserExistException, renderer="json")
def exist_user_exception(exc, request):
    return Response(json_body=exc.data, status=exc.data['status'] )


@forbidden_view_config(renderer='json')
def forbiddenException(request, exec):
    return Response(json_body={"stats": 403, "message":"You don't permision to use this module"}, status=403)