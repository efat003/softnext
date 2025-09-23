from .models import SiteSetting

def site_settings(request):
    """
    Context processor to make site settings available in all templates
    """
    try:
        settings = SiteSetting.objects.first()
        return {
            'site_settings': settings,
        }
    except:
        return {
            'site_settings': None,
        }