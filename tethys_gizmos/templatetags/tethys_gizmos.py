import os
import json
import time
from datetime import datetime
from django.conf import settings
from django import template
from django.template.loader import get_template
from django.template import TemplateSyntaxError


register = template.Library()

@register.filter(is_safe=True)
def isstring(value):
    """
    Filter that returns a type
    """
    if value is str:
        return True
    else:
        return False


def json_date_handler(obj):
    if isinstance(obj, datetime):
        return time.mktime(obj.timetuple()) * 1000
    else:
        return obj


@register.filter
def jsonify(data):
    """
    Convert python data structures into a JSON string
    """
    return json.dumps(data, default=json_date_handler)

@register.filter
def divide(value, divisor):
    """
    Divide value by divisor
    """
    v = float(value)
    d = float(divisor)

    return v/d


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
            # Get the name of the gizmo to load
            gizmo_name = self.gizmo_name
            gizmo_templates_root = os.path.join('tethys_gizmos', 'gizmos')

            # Handle case where gizmo_name is a string literal
            if self.gizmo_name[0] in ('"', "'"):
                gizmo_name = self.gizmo_name.replace("'", '')
                gizmo_name = gizmo_name.replace('"', '')

            # Add gizmo name to context variable
            # if 'gizmos_rendered' not in context:
            #     context.update({'gizmos_rendered': []})
            #
            # print(context)
            #
            # if gizmo_name not in context['gizmos_rendered']:
            #     context['gizmos_rendered'].append(gizmo_name)
            #
            # print(context)

            # Determine path to gizmo template
            gizmo_file_name = '{0}.html'.format(gizmo_name)
            template_name = os.path.join(gizmo_templates_root, gizmo_file_name)

            # Retrieve the gizmo template and render
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


# class TethysGizmoRegisterStaticNode(template.Node):
#     """
#     Custom template node that registers/appends the static library to the template context object.
#     """
#
#     def __init__(self, static_path, *args, **kwargs):
#         super(TethysGizmoRegisterStaticNode, self).__init__(*args, **kwargs)
#         self.static_path = static_path
#
#     def render(self, context):
#         if 'tethys_gizmo_static' not in context:
#             append_context = {'tethys_gizmo_static': []}
#             context.update(append_context)
#             print(context)
#         try:
#             pass
#             # gizmo_name = self.gizmo_name
#             #
#             # if self.gizmo_name[0] in ('"', "'"):
#             #     gizmo_name = self.gizmo_name.replace("'", '')
#             #     gizmo_name = gizmo_name.replace('"', '')
#             #
#             # gizmo_file_name = '{0}.html'.format(gizmo_name)
#             # template_name = os.path.join('tethys_gizmos', 'gizmos', gizmo_file_name)
#             # t = get_template(template_name)
#             # context = context.new(self.options.resolve(context))
#             # return t.render(context)
#
#         except:
#             if settings.TEMPLATE_DEBUG:
#                 raise
#             return ''
#
#
# @register.tag()
# def gizmo_static(parser, token):
#     """
#     Append a gizmo static library to the context object to avoid repetitive library imports.
#
#     Note: This tag will not import the static library, but it will register it for being imported by the gizmo_libraries
#     tag. Use the gizmo_libraries tag to import the libraries that have been collected.
#     """
#
#     try:
#         tag_name, static_path = token.split_contents()
#
#     except ValueError:
#         raise template.TemplateSyntaxError('"%s" tag requires exactly one argument' % token.contents.split()[0])
#
#     bits = token.split_contents()
#     if len(bits) < 2:
#         raise TemplateSyntaxError('"{0}" tag takes at least one argument: the name of the '
#                                   'static library to be included.'.format(bits[0]))
#
#     return TethysGizmoRegisterStaticNode(static_path)