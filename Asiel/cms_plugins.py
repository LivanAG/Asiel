from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext as _
from .models import BannerHomerPluginModel

'''
@plugin_pool.register_plugin
class BannerHomePlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "Plugins/bannerhome.html"
'''

@plugin_pool.register_plugin
class BannerHomePlugin2(CMSPluginBase):
    model = BannerHomerPluginModel
    render_template = "Plugins/bannerhome.html"
    name = _("Plugin Banner Home")
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class FooterPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "Plugins/footer.html"


