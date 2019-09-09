import json
from flask import Blueprint, request
from matrix_client.errors import MatrixRequestError, MatrixError
from ..matrix.client import client
from ..services.logger import logger
from ..services.mapping import get_rooms_mapping, get_users_mapping

civ_pages = Blueprint('civ_pages', __name__)


@civ_pages.route('/', methods=['POST'])
def civ():
    try:
        if request.is_json:
            data = request.get_json();
        else:
            data = request.form

        if 'value1' not in data or 'value2' not in data or 'value3' not in data:
            logger.warning('Not expected values found in post data')
            return json.dumps({
                'success': False,
                'errorCode': 'POST_BODY_INVALID',
            });

        game_name = data.get('value1')
        user = data.get('value2')
        turn = data.get('value3')

        rooms_mapping = get_rooms_mapping()
        if game_name not in rooms_mapping:
            logger.info('Game "{:s}" has not defined room'.format(game_name))
            return json.dumps({
                'success': False,
                'errorCode': 'NOT_ASSOCIATED_TO_A_ROOM',
            })

        text = "Hey {:s}, it's your turn to play (turn {:s})".format(user, turn)

        users_mapping = get_users_mapping()
        if user in users_mapping:
            html = "Hey <a href =\"https://matrix.to/#/{:s}\">{:s}</a>, it's your turn to play (turn {:s})"\
                .format(users_mapping[user], user, turn)
            response = client.send_message_event(rooms_mapping.get(game_name), "m.room.message", {
                "body": text,
                "msgtype": 'm.text',
                "format": "org.matrix.custom.html",
                "formatted_body": html
            })
        else:
            response = client.send_message(rooms_mapping.get(game_name), text)

        return json.dumps({
            'success': True,
            'serverResponse': response,
        })
    except MatrixRequestError as err:
        logger.error(err)
        return json.dumps({
            'success': False,
            'errorCode': 'MATRIX_REQUEST_ERROR',
            'serverResponse': json.loads(err.content),
        }), err.code
    except MatrixError as err:
        logger.error(err)
        return json.dumps({
            'success': False,
            'errorCode': 'INTERNAL_ERROR'
        })


__all__ = ['civ_pages']
