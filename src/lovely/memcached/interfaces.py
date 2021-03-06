##############################################################################
#
# Copyright (c) 2007 Lovely Systems and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
$Id$
"""
__docformat__ = "reStructuredText"

from zope import interface
from zope import schema

class IMemcachedClient(interface.Interface):

    """A memcache client utility"""

    defaultNS = schema.TextLine(
        title=u'Default Namespace',
        description=u"The default namespace used by this client",
        required=False,
        default=None)

    servers = schema.List(
        title = u'Servers',
        description = u"Servers defined as <hostname>:<port>",
        value_type = schema.BytesLine(),
        required = True,
        default=['127.0.0.1:11211']
        )

    defaultLifetime = schema.Int(
        title = u'Default Lifetime',
        description = u'The default lifetime of entries',
        required = True,
        default = 3600,
        )

    trackKeys = schema.Bool(
        title = u'Track Keys',
        description = u'Enable the keys method',
        required = False,
        default = False,
        )

    def getStatistics():
        """returns the memcached stats"""

    def set(data, key, lifetime=None, ns=None,
            raw=False,
            dependencies=[]):
        """Sets data with the given key in namespace. Lifetime
        defaults to defautlLifetime and ns defaults to the
        default namespace.

        The dependencies argument can be used to invalidate on
        specific dependency markers.

        This method returns the key that is generated by the utility.

        If raw is True, the key is taken as is, and is not modified by
        the utility, the key and the namespace need to be strings in
        this case, otherwise a ValueError is raised.
        """

    def query(key, default=None, ns=None, raw=False):
        """query the cache for key in namespace, returns default if
        not found. ns defaults to default namespace."""

    def invalidate(key=None, ns=None, raw=False, dependencies=[]):
        """invalidates key in namespace which defaults to default
        namespace, currently we can not invalidate just a namespace.

        If dependencies are provided all, entries with such
        dependencies are invalidated.
        """

    def invalidateAll():
        """invalidates all data of the memcached servers, not that all
        namespaces are invalidated"""

    def keys(ns=None):
        """if trackKeys is True, returns the keys defined in the
        namespace"""


class IInvalidateCacheEvent(interface.Interface):
    """An event which invalidates cache entries."""

    cacheName = schema.TextLine(
            title = u'cacheName',
            description = u"""
                Invalidate in the cache with this name.
                If no name is given all caches are invalidated.
                """,
            required = False,
            )

    key = schema.TextLine(
            title = u'key',
            required = False,
            )

    ns = schema.TextLine(
            title = u'namespace',
            required = False,
            )

    raw = schema.Bool(
            title = u'raw',
            required = False,
            default = False,
            )

    dependencies = schema.List(
            title = u'Dependencies',
            required = False,
            )
