from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from misago.threads.threadtypes.thread import Thread


class RootCategory(Thread):
    type_name = 'root_category'

    def get_category_name(self, category):
        return _('None (will become top level category)')

    def get_category_absolute_url(self, category):
        return reverse('misago:threads')

    def get_category_last_thread_url(self, category):
        return '/threads/%s-%s/' % (
            category.last_thread_slug,
            category.last_thread_id,
        )

    def get_category_last_post_url(self, category):
        return '/threads/%s-%s/last/' % (
            category.last_thread_slug,
            category.last_thread_id,
        )

    def get_category_api_read_url(self, category):
        return reverse('misago:api:thread-read')


class Category(RootCategory):
    type_name = 'category'

    def get_category_name(self, category):
        return category.name

    def get_category_absolute_url(self, category):
        return reverse('misago:category', kwargs={
            'pk': category.pk,
            'slug': category.slug,
        })

    def get_category_api_read_url(self, category):
        return '%s?category=%s' % (
            reverse('misago:api:thread-read'), category.pk)