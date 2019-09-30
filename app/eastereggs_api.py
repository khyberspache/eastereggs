from aiohttp_jinja2 import template


class EggsApi:

    def __init__(self, auth_svc, plugins):
        self.auth_svc = auth_svc
        self.plugins = plugins

    @template('eggshome.html')
    async def home(self, request):
        await self.auth_svc.check_permissions(request)
        p = [dict(name=getattr(p, 'name'), description=getattr(p, 'description'), address=getattr(p, 'address'))
             for p in self.plugins]
        return dict(plugins=p)

