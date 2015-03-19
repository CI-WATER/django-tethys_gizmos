from .base import TethysGizmoOptions

__all__ = ['PlotView']


class PlotView(TethysGizmoOptions):
    """
    Highcharts Plot View

    Plot views can be used to generate interactive plots of tabular data. All of the plots available through this gizmo are powered by the Highcharts JavaScript library.

    Attributes
    highcharts_object(PySON, required): The highcharts_object ocontains the definition of the chart. The full `Highcharts API reference <http://api.highcharts.com/highcharts>`_ is supported via this object. The object can either be a JavaScript string or a JavaScript-equivalent Python data structure. The latter is recommended.
    height(string): Height of the plot element. Any valid css unit of length.
    width(string): Width of the plot element. Any valid css unit of length.
    attributes(string): Any HTML attributes to add to the plot element (e.g.: "id=foo name=bar value=hello-world")
    """

    def __init__(self, highcharts_object, height='520px', width='100%', attributes=""):
        """
        Constructor
        """
        # Initialize super class
        super(PlotView, self).__init__()

        self.highcharts_object = highcharts_object
        self.height = height
        self.width = width
        self.attributes = attributes