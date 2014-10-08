=============
Tethys Gizmos
=============

Gizmos are building blocks that can be used to create beautiful interactive controls for web apps. Using gizmos,
developers can add date-pickers, plots, and maps to their templates with minimal coding.

Django Configuration
--------------------

1. Add "tethys_gizmos" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'tethys_gizmos',
    )

2. Add the context processor to settings. For example::

    TEMPLATE_CONTEXT_PROCESSORS = ('django.contrib.auth.context_processors.auth',
                                   'django.core.context_processors.debug',
                                   'django.core.context_processors.i18n',
                                   'django.core.context_processors.media',
                                   'django.core.context_processors.static',
                                   'django.core.context_processors.tz',
                                   'tethys_gizmos.context_processors.tethys_gizmos_context')

3. Some of the gizmos provided make use of the Google Maps v3 API, which requires an API key to use
(see https://developers.google.com/maps/documentation/javascript/tutorial). This can API key can be configured globally
in the settings for your project. Otherwise, you will need to pass the API key as an option everytime you use a map
enabled gizmo. To set the API key, add the following line to your settings with your API key::

    TETHYS_GIZMOS_GOOGLE_MAPS_API_KEY = 'S0m3@pik3y'


4. Include the Tethys Gizmos URLconf to your project urls.py with the "gizmos" namespace::

    url(r'^gizmos/', include('tethys_gizmos.urls', namespace='gizmos')),

5. Tethys Gizmos makes extensive use of Twitter Bootstrap and Jquery. These libraries must be included in all templates
that use gizmos. Because of the prevalent use of these two libraries, we leave it to the developer to decide how to
provide these dependencies. It is suggested that you include them in your "page.html" (see below) or some other base
template that all pages in your website use.


6. Tethys Gizmos includes a showcase of all the available gizmos including live demos and code examples. To get this page
working you will need to create a template called "page.html" in your base "templates" directory that includes blocks
called "styles", "bodytag", "primary_content", and "scripts". Also include the Bootstrap and Jquery dependencies. Your
"page.html" should look something like this::


    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
            {% block styles %}
            {% endblock %}
        </head>
        <body {% block bodytag %}{% endblock %}>
            {% block primary_content %}
            {% endblock %}

            {% block scripts %}
            {% endblock %}
        </body>
    </html>


..note:: The gizmos work best if your Jquery and Bootstrap JavaScript scripts are included in the head of your document as is depicted above.
