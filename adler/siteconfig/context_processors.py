from .models import SiteSettings


def settings(request):
    return {'settings': SiteSettings.get_solo()}
