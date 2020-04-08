from app.utility.base_world import BaseWorld
from plugins.eastereggs.app.eastereggs_api import EggsApi

name = 'EasterEggs'
description = 'Heh heh heh'
address = None
access = BaseWorld.Access.APP


async def enable(services):
    app = services.get('app_svc').application
    eggs_api = EggsApi(services)
    app.router.add_static('/eggs', 'plugins/eastereggs/static/', append_version=True)
    route = [r for r in app.router._resources if r.canonical == '/']
    if route:
        app.router._resources.remove(route[0])
    app.router.add_route('*', '/', eggs_api.landing)
    app.router.add_route('*', '/red', eggs_api.red_landing)
    app.router.add_route('*', '/blue', eggs_api.blue_landing)
