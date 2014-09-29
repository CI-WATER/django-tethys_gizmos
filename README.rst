=============
Tethys Gizmos
=============

Tethys gizmos provides a mechanism for inserting common UI elements into your templates with minimal markup,
JavaScript, and CSS. Examples include date pickers, plots, and maps.

Quick start
-----------

1. Add "tethys_apps" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'tethys_gizmos',
    )

2. Include the Tethys URLconf in your project urls.py like this::

    url(r'^gizmos/', include('tethys_gizmos.urls')),

3. Add context processor to settings::

    TEMPLATE_CONTEXT_PROCESSORS = ('django.contrib.auth.context_processors.auth',
                               'django.core.context_processors.debug',
                               'django.core.context_processors.i18n',
                               'django.core.context_processors.media',
                               'django.core.context_processors.static',
                               'django.core.context_processors.tz',
                               'django.contrib.messages.context_processors.messages',
                               'tethys_gizmos.context_processors.tethys_gizmos_context')
