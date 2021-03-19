from django.contrib import admin
from django.utils.html import format_html
from django.utils.formats import date_format
from django.utils.timezone import now
from django.urls import reverse
from django.urls import include, path
from django.conf import settings

from django.contrib import admin, messages
from django.contrib.sites.models import Site
from django.http import HttpResponse, HttpResponseRedirect, Http404
from newsletter.admin import SubmissionAdmin,NewsletterAdmin,NewsletterAdminLinkMixin
from newsletter.admin_utils import ExtendibleModelAdminMixin

from newsletter.admin_forms import (
    SubmissionAdminForm, SubscriptionAdminForm, ImportForm, ConfirmForm,
    ArticleFormSet
)

from django.utils.translation import gettext as _, ngettext

from newsletter.models import Submission


# Construct URL's for icons
ICON_URLS = {
    'yes': '%snewsletter/admin/img/icon-yes.gif' % settings.STATIC_URL,
    'wait': '%snewsletter/admin/img/waiting.gif' % settings.STATIC_URL,
    'submit': '%snewsletter/admin/img/submitting.gif' % settings.STATIC_URL,
    'no': '%snewsletter/admin/img/icon-no.gif' % settings.STATIC_URL
}

# Desinstalo el Submission que estaba en el panel de administracion y lo sobrescribo por el mio
admin.site.unregister(Submission)



class SubmissionAdmin(NewsletterAdminLinkMixin, ExtendibleModelAdminMixin,
                      admin.ModelAdmin):
    form = SubmissionAdminForm
    list_display = (
        'admin_message', 'admin_newsletter', 'admin_publish_date', 'publish',
        'admin_status_text', 'admin_status'
    )
    date_hierarchy = 'publish_date'
    list_filter = ('newsletter', 'publish', 'sent')
    save_as = True
    filter_horizontal = ('subscriptions',)

    """ List extensions """
    def admin_message(self, obj):
        return format_html('<a href="{}/">{}</a>', obj.id, obj.message.title)
    admin_message.short_description = _('submission')

    def admin_publish_date(self, obj):
        if obj.publish_date:
            return date_format(obj.publish_date, 'DATETIME_FORMAT')
        else:
            return ''
    admin_publish_date.short_description = _("publish date")

    def admin_status(self, obj):
        if obj.prepared:
            if obj.sent:
                return format_html(
                    '<img src="{}" width="10" height="10" alt="{}"/>',
                    ICON_URLS['yes'], self.admin_status_text(obj)
                )
            else:
                if obj.publish_date > now():
                    return format_html(
                        '<img src="{}" width="10" height="10" alt="{}"/>',
                        ICON_URLS['wait'], self.admin_status_text(obj)
                    )
                else:
                    return format_html(
                        '<img src="{}" width="12" height="12" alt="{}"/>',
                        ICON_URLS['wait'], self.admin_status_text(obj)
                    )
        else:
            return format_html(
                '<img src="{}" width="10" height="10" alt="{}"/>',
                ICON_URLS['no'], self.admin_status_text(obj)
            )
    admin_status.short_description = ''

    def admin_status_text(self, obj):
        if obj.prepared:
            if obj.sent:
                return _("Sent.")
            else:
                if obj.publish_date > now():
                    return _("Delayed submission.")
                else:
                    return _("Submitting.")
        else:
            return _("Not sent.")
    admin_status_text.short_description = _('Status')

    """ Views """
    def submit(self, request, object_id):
        submission = self._getobj(request, object_id)

        if submission.sent or submission.prepared:
            messages.info(request, _("Submission already sent."))
            change_url = reverse(
                'admin:newsletter_submission_change', args=[object_id]
            )
            return HttpResponseRedirect(change_url)

        
        submission.prepared = True
        submission.save()
        Submission.submit_queue()
        messages.info(request, _("Your submission is sent."))

        changelist_url = reverse('admin:newsletter_submission_changelist')
       
        return HttpResponseRedirect(changelist_url)

    """ URLs """
    def get_urls(self):
        urls = super().get_urls()

        my_urls = [
            path(
                '<object_id>/submit/',
                self._wrap(self.submit),
                name=self._view_name('submit')
            )
        ]

        return my_urls + urls


admin.site.register(Submission, SubmissionAdmin)