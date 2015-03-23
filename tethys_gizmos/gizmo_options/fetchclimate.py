from .base import TethysGizmoOptions

__all__ = ['URLParameter', 'MapParameters', 'MapData', 'PlotParameters', 'VariableParameters', 'GridParameters', 'PointParameters']


class URLParameter(TethysGizmoOptions):
    """
    URL Parameter

    This gizmo can be used to get climate data based off of a bounding box over an area or a point. It is based off of Microsoft Research. See the `FetchClimate page reference <http://research.microsoft.com/en-us/projects/fetchclimate/>`_ for more info.

    Attributes
    serverUrl(string): The URL to the FetchClimate server (e.g 'serverUrl':'http://fetchclimate2.cloudapp.net')
    """

    def __init__(self, serverUrl='http://fetchclimate2.cloudapp.net', ):
        """
        Constructor
        """
        # Initialize super class
        super(URLParameter, self).__init__()

        self.serverUrl = serverUrl


class MapParameters(TethysGizmoOptions):
    """
    Map Parameters
    Optional if grid or point included. Otherwise, required!

    Attributes
    css(dictionary):Custom css elements. FORMAT:{'css-element-name': 'css-value'}. If no width or height included, 500px X 500px assumed.
    map_data(dictionary): Data needed to create the map.
    """

    def __init__(self, css={}, map_data={}):
        """
        Constructor
        """
        # Initialize super class
        super(MapParameters, self).__init__()

        self.css = css
        self.map_data = map_data


class MapData(TethysGizmoOptions):
    """
    Map Parameters - map_data

    Attributes
    api_key(string): API key for Google maps.
    drawing_types_enabled(string array): A list of the types of geometries the user will be allowed to draw. Valid types are: RECTANGLE, and POINTS. (e.g.: drawing_types_enabled=['RECTANGLE','POINTS'])
    initial_drawing_mode(string array): A string representing the drawing mode that will be enabled by default. Valid modes are: 'RECTANGLE', 'POINTS'. The mode used must be one of the drawing_types_enabled that the user is allowed to draw.
    max_num_grids(integer): The maximum number of grids allowed for the user. Default is unlimited. (e.g. 'max_num_grids':0).
    max_num_points(integer): The maximum number of points allowed for the user. Default is unlimited. (e.g 'max_num_points':0).
    """

    def __init__(self, api_key='', drawing_types_enabled=['RECTANGLE'], initial_drawing_mode='RECTANGLE', max_num_grids=0, max_num_points=0):
        """
        Constructor
        """
        # Initialize super class
        super(MapData, self).__init__()

        self.api_key = api_key
        self.drawing_types_enabled = drawing_types_enabled
        self.initial_drawing_mode = initial_drawing_mode
        self.max_num_grids = max_num_grids
        self.max_num_points = max_num_points


class PlotParameters(TethysGizmoOptions):
    """
    Plot Parameters

    Attributes
    dimensions(string dictionary): The integer is in pixels for width (`Highcharts width reference <http://api.highcharts.com/highcharts#chart.width>`_) or height (`Highcharts height reference <http://api.highcharts.com/highcharts#chart.height>`_). Not required to be defined.
    """

    def __init__(self, dimensions={'width':'100%', 'height':'500px'}):
        """
        Constructor
        """
        # Initialize super class
        super(PlotParameters, self).__init__()

        self.dimensions = dimensions


class VariableParameters(TethysGizmoOptions):
    """
    Variable Parameters

    To find out which variables you can use and their parameters, go to your service url with '/api/coniguration' at the end. (e.g. `http://fetchclimate2.cloudapp.net/api/configuration <http://fetchclimate2.cloudapp.net/api/configuration>`_). Look in "EnvironmentalVariables" for the variable names. Then, to find the data source ID's of sources available, go to "DataSources".

    Attributes
    variables(dictionary): Must have variable defined. It is in the format {'variable_name':[variable_id,variable_id,variable_id]}.
    """

    def __init__(self, variables={'precip':[]}):
        """
        Constructor
        """
        # Initialize super class
        super(VariableParameters, self).__init__()

        self.variables = variables


class GridParameters(TethysGizmoOptions):
    """
    Grid Parameters

    Optional if there is a map or point included. Otherwise, it is required! No map needed. If map included, it will initialize with input grid.

    Attributes
    title(string): The name of the grid area.
    boundingBox(array): An array of length 4 with bounding lat and long. e.g.[min lat, max lat, min lon, max long].
    gridResolution(array): An array of length 2. Number of grid cells in lat and lon directions. e.g.[lat resolution,lon resolution].
    """

    def __init__(self, title='', boundingBox=[], gridResolution=[]):
        """
        Constructor
        """
        # Initialize super class
        super(GridParameters, self).__init__()

        self.title = title
        self.boundingBox = boundingBox
        self.gridResolution = gridResolution


class PointParameters(TethysGizmoOptions):
    """
    Point Parameters

    Optional if there is a map or grid included. Otherwise, it is required! No map needed. If map included, it will initialize with input point.

    Attributes
    title(string): The name of the point location.
    location(array): An array of length 2 with lat and lon of point. e.g.[lat,lon].
    """

    def __init__(self, title='', location=[]):
        """
        Constructor
        """
        # Initialize super class
        super(PointParameters, self).__init__()

        self.title = title
        self.location = location