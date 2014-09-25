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
    Similar to the include tag, gizmo loads special templates called gizmos that come with the django-tethys_gizmo
    app. Gizmos provide tools for developing user interface elements with minimal code. Examples include date pickers,
    maps, and interactive plots.

    To insert a gizmo, use the "gizmo" tag and give it the name of a gizmo and a dictionary of configuration parameters.

    Example::
        {% load tethys_gizmos %}

        {% gizmo example_gizmo options %}
        {% gizmo "example_gizmo" options %}

    NOTE: the "options" dictionary must be a template context variable.
    """
    try:
        tag_name, gizmo_name, options_literal = token.split_contents()

    except ValueError:
        raise template.TemplateSyntaxError('"%s" tag requires exactly two arguments' % token.contents.split()[0])

    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError('"{0}" tag takes at least one argument: the name of the '
                                  'template to be included.'.format(bits[0]))

    return TethysGizmoIncludeNode(gizmo_name, options_literal)