from .base import TethysGizmoOptions

__all__ = ['MapView']


class MapView(TethysGizmoOptions):
    """
    Map View

    The Map View gizmo can be used to visualize maps of spatial data. Map View is powered by OpenLayers 3, an open source pure javascript mapping library.

    Attributes
    height(string): Height of the map element. Any valid css unit of length.
    width(string): Width of the map element. Any valid css unit of length.
    basemap(string or dict): The base map to show on the map which can be either OpenStreetMap, MapQuest, or a Bing map. Valid values for the string option are: 'OpenStreetMap' and 'MapQuest'. If you wish to configure the base map with options, you must use the dictionary form. The dictionary form is required to use a Bing map, because an API key must be passed as an option. See details below.
    view(dictionary): The initial view or extent for the map. This is set by specifying a center point and a zoom level where a zoom of 0 is zoomed out. Note that the default projection for OpenLayers is Spherical Mercator (`EPSG:3857 reference <http://spatialreference.org/ref/sr-org/6864/>`_). The dictionary can have keys: center, zoom, projection, minZoom, and maxZoom. If you want to specify the coordinates for the center in a different projection, such as WGS 84 (`EPSG:4326 reference <http://spatialreference.org/ref/epsg/4326/>`_), you must specify the projection. See details below.
    controls(list): A list of controls to add to the map. The list can be a list of strings or a list of dictionaries. Valid strings are 'ZoomSlider', 'Rotate', 'FullScreen', 'ScaleLine', 'ZoomToExtent', and 'MousePosition'.
    layers(list): A list of layer dictionaries where the singular key of each dictionary specifies the type of layer and the value is another dictionary with the options for that layer. Supported layer types are 'WMS', 'TiledWMS', 'GeoJSON', and 'KML'. See notes below details.
    """

    def __init__(self, height='520px', width='100%', basemap='OpenStreetMap', view={'center': [-100, 40], 'zoom': 2},
                 controls=[], layers='', draw=[], legend=False):
        """
        Constructor
        """
        # Initialize super class
        super(MapView, self).__init__()

        self.height = height
        self.width = width
        self.basemap = basemap
        self.view = view
        self.controls = controls
        self.layers = layers
        self.draw = draw
        self.legend = legend