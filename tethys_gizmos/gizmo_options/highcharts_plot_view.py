from .base import TethysGizmoOptions

__all__ = ['PlotView', 'HighChartsObject']


class PlotView(TethysGizmoOptions):
    """
    Highcharts Plot View

    Plot views can be used to generate interactive plots of tabular data. All of the plots available through this gizmo are powered by the Highcharts JavaScript library.

    Attributes
    highcharts_object(PySON, required): The highcharts_object contains the definition of the chart. The full `Highcharts API reference <http://api.highcharts.com/highcharts>`_ is supported via this object. The object can either be a JavaScript string or a JavaScript-equivalent Python data structure. The latter is recommended.
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


class HighChartsObject(TethysGizmoOptions):
    """
    HighCharts Object

    Attributes
    """

    def __init__(self, chart={}, title='', subtitle='', legend={}, xAxis={}, yAxis={}, tooltip={},
                 series=[], **kwargs):
        """
        Constructor
        """
        # Initialize super class
        super(TethysGizmoOptions, self).__init__()

        self.chart = chart
        self.title = title
        self.subtitle = subtitle
        self.legend = legend
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.tooltip = tooltip
        self.series = series
        #add any other attributes the user wants
        for key, value in kwargs.iteritems():
            setattr(self, key, value)


class HighChartsLinePlot(TethysGizmoOptions):
    """
    Line Plot

    Displays as a line graph.

    Attributes
    """

    def __init__(self,chart={'type': 'line'}, title='', subtitle='', legend={}, xAxis={}, yAxis={}, tooltip={},
                 series=[]):
        """
        Constructor
        """
        # Initialize super class
        super(HighChartsObject, self).__init__(chart=chart, title=title, subtitle=subtitle, legend=legend,
                                               xAxis=xAxis, yAxis=yAxis, tooltip=tooltip, series=series)