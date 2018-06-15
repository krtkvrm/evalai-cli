import click
from click import echo
from datetime import datetime


class Date(click.ParamType):
    """
    Date object parsed using datetime.
    """
    name = 'date'

    def __init__(self, format):
        self.format = format

    def convert(self, value, param, ctx):
        try:
            date = datetime.strptime(value, self.format)
            return date
        except ValueError:
            raise self.fail("Incorrect date format, please use {} format".format(self.format))


def valid_token(response):
    """
    Checks if token is valid.
    """

    if ('detail' in response):
        if (response['detail'] == 'Invalid token'):
            echo("The authentication token you are using isn't valid."
                 " Please try again.")
            return False
        if (response['detail'] == 'Token has expired'):
            echo("Sorry, the token has expired.")
            return False
    return True
