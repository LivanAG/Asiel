from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from django.utils.translation import get_language, gettext, gettext_lazy as _


class BannerHomerPluginModel(CMSPlugin):
    titulo1 = models.CharField(max_length=100)

    titulo2 = models.CharField(max_length=200)

    imagen1 = FilerImageField(
        verbose_name=_("Imagen"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )


    imagen2 = FilerImageField(related_name="Imagen_2", blank=True,null=True,on_delete=models.SET_NULL)
    imagen3 = FilerImageField(related_name="Imagen_3", blank=True,null=True,on_delete=models.SET_NULL)




class BannerBlogPluginModel(CMSPlugin):
    titulo = models.CharField(max_length=100)

    subtitulo = models.CharField(max_length=200)

    imagen1 = FilerImageField(
        verbose_name=_("Imagen"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
