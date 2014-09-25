import os
from django.conf import settings
from django import template
from django.template.loader import get_template
from django.template import TemplateSyntaxError


register = template.Library()


class TethysGizmoIncludeNode(template.Node):
    """
    Custom template include node that returns Tethys gizmos
    """
    def __init__(self, gizmo_name, options, *args, **kwargs):
        super(TethysGizmoIncludeNode, self).__init__(*args, **kwargs)
        self.gizmo_name = gizmo_name
        self.options = template.Variable(options)

    def render(self, context):
        try:
            gizmo_name = self.gizmo_name

            if self.gizmo_name[0] in ('"', "'"):
                gizmo_name = self.gizmo_name.replace("'", '')
                gizmo_name = gizmo_name.replace('"', '')

            gizmo_file_name = '{0}.html'.format(gizmo_name)
            template_name = os.path.join('tethys_gizmos', 'gizmos', gizmo_file_name)
            t = get_template(template_name)
            context = context.new(self.options.resolve(context))
            return t.render(context)

        except:
            if settings.TEMPLATE_DEBUG:
                raise
            return ''


@register.tag()
def gizmo(parser, token):
    """
    Similar to the include tag, gizmo loads a template and renders it. However, the gizmo tag will not render the
    template with the current context.

    Example::

        {% gizmo "foo/some_include" %}
        {% gizmo "foo/some_include" with bar="BAZZ!" baz="BING!" %}

    Use the ``only`` argument to exclude the current context when rendering
    the included template::

        {% gizmo "foo/some_include" only %}
        {% gizmo "foo/some_include" with bar="1" only %}
    """
    try:
        tag_name, gizmo_name, options_literal = token.split_contents()

    except ValueError:
        raise template.TemplateSyntaxError('"%s" tag requires exactly two arguments' % token.contents.split()[0])

    print(gizmo_name, options_literal)

    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError('"{0}" tag takes at least one argument: the name of the '
                                  'template to be included.'.format(bits[0]))

    return TethysGizmoIncludeNode(gizmo_name, options_literal)