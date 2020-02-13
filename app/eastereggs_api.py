import logging
import inspect

from aiohttp import web
from aiohttp_jinja2 import template

from app.api import blue, red
from app.service.auth_svc import red_authorization, blue_authorization
from app.utility.base_world import BaseWorld

search_red = dict(access=(BaseWorld.Access.RED, BaseWorld.Access.APP))
search_blue = dict(access=(BaseWorld.Access.BLUE, BaseWorld.Access.APP))


class EggsApi:

    def __init__(self, services):
        self.data_svc = services.get('data_svc')
        self.auth_svc = services.get('auth_svc')
        self.modules = {
            'red': {f[0]: f[1] for f in inspect.getmembers(red, inspect.isfunction)},
            'blue': {f[0]: f[1] for f in inspect.getmembers(blue, inspect.isfunction)}
        }
        self.log = logging.getLogger('rest_api')

    @red_authorization
    @template('eggsred.html')
    async def red_landing(self, request):
        try:
            s = {**search_red, **dict(enabled=True)}
            plugins = await self.data_svc.locate('plugins', s)
            return dict(plugins=[p.display for p in plugins])
        except web.HTTPFound as e:
            raise e
        except Exception as e:
            logging.error('[!] landing: %s' % e)

    @blue_authorization
    @template('eggsblue.html')
    async def blue_landing(self, request):
        try:
            s = {**search_blue, **dict(enabled=True)}
            plugins = await self.data_svc.locate('plugins', s)
            return dict(plugins=[p.display for p in plugins])
        except web.HTTPFound as e:
            raise e
        except Exception as e:
            logging.error('[!] landing: %s' % e)

    async def landing(self, request):
        try:
            await self.red_landing(request)
            return web.HTTPFound(location='/red')
        except web.HTTPFound:
            try:
                await self.blue_landing(request)
                return web.HTTPFound(location='/blue')
            except web.HTTPFound as e:
                raise e
