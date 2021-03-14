from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from django.utils.translation import get_language, gettext, gettext_lazy as _


class BannerHomerPluginModel(CMSPlugin):
    enunciado = models.CharField(max_length=100)

    subtitulo = models.CharField(max_length=200)
    
    main_image = FilerImageField(
        verbose_name=_("main image"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )