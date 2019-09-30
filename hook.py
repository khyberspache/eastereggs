from plugins.eastereggs.app.eastereggs_api import EggsApi

name = 'EasterEggs'
description = 'Adds closed source abilities, adversaries, planners, parsers and more'
address = None


async def initialize(app, services):
    eggs_api = EggsApi(auth_svc=services.get('auth_svc'), plugins=services.get('plugin_svc').get_plugins())
    app.router.add_static('/eggs', 'plugins/eastereggs/static/', append_version=True)
    route = [r for r in app.router._resources if r.canonical == '/']
    if route:
        app.router._resources.remove(route[0])
    app.router.add_route('*', '/', eggs_api.home)
