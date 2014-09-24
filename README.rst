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
