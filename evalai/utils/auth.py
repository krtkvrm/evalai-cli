import os
import json
import sys

from click import echo, style
from evalai.utils.config import (AUTH_TOKEN_PATH,
                                 API_HOST_URL,
                                 HOST_URL_FILE_PATH,)


def get_user_auth_token():
    """
    Description
    ----------
    Loads token to be used for sending requests

    Args
    ----------
    None

    Returns
    -------
    token: str
       Token of the user

    Raises
    -------
    OSError, IOError: Error while operating on file system
    """
    if os.path.exists(AUTH_TOKEN_PATH):
        with open(str(AUTH_TOKEN_PATH), 'r') as TokenObj:
            try:
                data = TokenObj.read()
            except (OSError, IOError) as e:
                echo(e)
        data = json.loads(data)
        token = data["token"]
        return token
    else:
        echo(style("\nThe authentication token json file doesn't exists at the required path. "
                   "Please download the file from the Profile section of the EvalAI webapp and "
                   "place it at ~/.evalai/token.json\n", bold=True, bg="red"))
        sys.exit(1)


def get_request_header():
    """
    Description
    ----------
    Returns user auth token formatted in header for sending requests

    Args
    ----------
    None

    Returns
    -------
    header: dict
       Token of the user as a header

    Raises
    ----------
    None
    """
    header = {
            "Authorization": "Token {}".format(get_user_auth_token()),
    }

    return header


def get_host_url():
    """
    Description
    ----------
    Returns the host url

    Args
    ----------
    None

    Returns
    -------
    API_HOST_URL: str
       Host URL the user has configured

    Raises
    -------
    OSError, IOError: Error while operating on file system
    """
    if not os.path.exists(HOST_URL_FILE_PATH):
        return API_HOST_URL
    else:
        with open(HOST_URL_FILE_PATH, 'r') as fr:
            try:
                data = fr.read()
                return str(data)
            except (OSError, IOError) as e:
                echo(e)
