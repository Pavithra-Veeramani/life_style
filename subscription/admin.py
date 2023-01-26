from django.contrib import admin
from .models import Subscription, Newsletter


def send_newsletter(modeladmin, request, queryset):
    print('send_newsletter called')
    for newsletter in queryset:
        newsletter.send(request)
        print('send_newsletter', request)


send_newsletter.short_description = "Send selected Newsletters to all subscribers"


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'created_on'
    )


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Newsletter, NewsletterAdmin)