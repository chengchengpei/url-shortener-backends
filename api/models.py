from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import random

class Link(models.Model):
    
    alphabet = 'abcdefghigklmnopqrstuvwxyz0123456789'

    long_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    visit_count = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Short url: %s, Long url: %s' % (self.short_url, self.long_url)

    def save(self, *args, **kwargs):
        if not self.short_url:
            url = None
            while True:
                code = ''.join(random.choice(Link.alphabet) for _ in range(6))
                url = settings.SITE_BASE_URL + code
                if not Link.objects.filter(short_url=url).exists():
                    break

            self.short_url = url
 
        super(Link, self).save(*args, **kwargs)



