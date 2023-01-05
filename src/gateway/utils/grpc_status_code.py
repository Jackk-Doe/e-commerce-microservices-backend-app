import http
from grpc import StatusCode


# Convert grpc status code class into http status code class
# NOTE : match-case only work with python3.10+
async def convert_to_http_status_code(grpc_code: StatusCode) -> http.HTTPStatus:    
    if grpc_code == StatusCode.NOT_FOUND:
        return http.HTTPStatus.NOT_FOUND
    elif grpc_code == StatusCode.UNAUTHENTICATED:
        return http.HTTPStatus.UNAUTHORIZED
    elif grpc_code == StatusCode.PERMISSION_DENIED:
        return http.HTTPStatus.FORBIDDEN
    elif grpc_code == StatusCode.INTERNAL:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        return http.HTTPStatus.BAD_REQUEST