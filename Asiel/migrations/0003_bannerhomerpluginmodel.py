# Generated by Django 3.1.7 on 2021-03-19 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0022_auto_20180620_1551'),
        ('Asiel', '0002_delete_bannerhomerpluginmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerHomerPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='asiel_bannerhomerpluginmodel', serialize=False, to='cms.cmsplugin')),
                ('titulo1', models.CharField(max_length=100)),
                ('titulo2', models.CharField(max_length=200)),
                ('imagen1', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Imagen 1')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
