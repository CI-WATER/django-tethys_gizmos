

class TethysGizmoOptions(dict):
    """
    Base class for Tethys Gizmo Options objects.
    """

    def __init__(self):
        """
        Constructor for Tethys Gizmo Options base.
        """
        # Initialize super class
        super(TethysGizmoOptions, self).__init__()

        # Dictionary magic
        self.__dict__ = self
