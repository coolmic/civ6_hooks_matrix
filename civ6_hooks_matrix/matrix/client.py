from matrix_client.api import MatrixHttpApi as _MatrixHttpApi
from .. import env as _env

client = _MatrixHttpApi(_env.MATRIX_URL, token=_env.MATRIX_USER_ACCESS_TOKEN)

__all__ = ['client']
