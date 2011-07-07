#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Google Site Copy Backup"

__email__ = 'nicolasp@microsigns.com'
__author__ = 'Nicolas Plessis <%s>' % __email__

import datetime
import atom.data
import gdata.sites.client
import gdata.sites.data
from sys import argv

script, site = argv
user = 'user@your_domain'
passwd = 'password'
domain = 'your_domain'
today = datetime.date.today()

client = gdata.sites.client.SitesClient()
client.ClientLogin(user, passwd, client.source);
client.domain = domain
feed = client.GetSiteFeed()

for entry in feed.entry:
    if entry.title.text == site:
        print "Site found : %r" % entry.title.text
        copied_site = client.CreateSite('%s-%s' % (today,site), 
            description='Backup', source_site=entry.FindSelfLink())
        print 'Site copied! View it at: ' + copied_site.GetAlternateLink().href

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
