from datetime import datetime

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

from tagging.fields import TagField
from clan.models import Clan

try:
    from notification import models as notification
except:
    notification = None

class Topic(models.Model):
    """
    a discussion topic for a clan.
    """
 
    clan = models.ForeignKey(Clan, related_name="topics", verbose_name=_('clan'))

    title = models.CharField(_('title'), max_length=50)
    creator = models.ForeignKey(User, related_name="created_topics", verbose_name=_('creator'))
    created = models.DateTimeField(_('created'), default=datetime.now)
    modified = models.DateTimeField(_('modified'), default=datetime.now) # topic modified when commented on
    body = models.TextField(_('body'), blank=True)

    tags = TagField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ("tribe_topic", [self.pk])
    get_absolute_url = models.permalink(get_absolute_url)

    class Meta:
        ordering = ('-modified', )

from threadedcomments.models import ThreadedComment
def new_comment(sender, instance, **kwargs):
    if isinstance(instance.content_object, Topic):
        topic = instance.content_object
        topic.modified = datetime.now()
        topic.save()
        if notification:
            notification.send([topic.creator], "tribes_topic_response", {"user": instance.user, "topic": topic})
models.signals.post_save.connect(new_comment, sender=ThreadedComment)
