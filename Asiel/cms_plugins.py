from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext as _
from .models import *
from django.conf import settings

@plugin_pool.register_plugin
class NavBarPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "Plugins/barnav.html"

    def render(self, context, instance, placeholder):
        cadena = settings.NOMBRE_DEL_BLOG[1:]
        letra_inicial = settings.NOMBRE_DEL_BLOG[0]
        context = super().render(context, instance, placeholder)
        context['sitio']=cadena
        context['letra_inicial']=letra_inicial
        return context


@plugin_pool.register_plugin
class HomeSeccionPlugin(CMSPluginBase):
    model = HomeSeccionPluginModel
    allow_children = True
    render_template = "Plugins/Home_Seccion.html"

@plugin_pool.register_plugin
class HomeNewsletterPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "Plugins/newsletter.html"

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
class BannerBlog(CMSPluginBase):
    model = BannerBlogPluginModel
    render_template = "Plugins/bannerblog.html"
    name = _("Plugin Banner Blog")
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class FooterPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "Plugins/footer.html"

    def render(self, context, instance, placeholder):
        cadena = settings.NOMBRE_DEL_BLOG[1:]
        letra_inicial = settings.NOMBRE_DEL_BLOG[0]
        context = super().render(context, instance, placeholder)
        context['sitio']=cadena
        context['letra_inicial']=letra_inicial
        return context


@plugin_pool.register_plugin
class AboutMePlugin(CMSPluginBase):
    model = AboutMePluginModel
    render_template = "Plugins/about_me.html"
    name = _("About Me Plugin")
    cache = False
    allow_children = True
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context



@plugin_pool.register_plugin
class NewsLetterNavBarBlogPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "Plugins/newsletter_barra_nav_blog.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context