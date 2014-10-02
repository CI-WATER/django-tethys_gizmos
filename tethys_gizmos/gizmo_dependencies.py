def global_dependencies(context):
    """
    Dependencies that are loaded for all tethys gizmos (after gizmo dependencies).
    """
    return('tethys_gizmos/css/tethys_gizmos.css',
           'tethys_gizmos/js/tethys_gizmos.js')


def date_picker(context):
    """
    Dependencies for date_picker gizmo.
    """
    return ('tethys_gizmos/vendor/bootstrap_datepicker/css/datepicker3.css',
            'tethys_gizmos/vendor/bootstrap_datepicker/js/bootstrap_datepicker.js')


def highcharts_plot_view(context):
    """
    Dependencies for highcharts_plot_view gizmo.
    """
    return ('tethys_gizmos/vendor/highcharts/js/highcharts.js',
            'tethys_gizmos/vendor/highcharts/js/highcharts-more.js',
            'tethys_gizmos/vendor/highcharts/js/modules/exporting.js',
    )


def toggle_switch(context):
    """
    Dependencies for toggle_switch gizmo.
    """
    return ('tethys_gizmos/vendor/bootstrap_switch/dist/css/bootstrap3/bootstrap-switch.min.css',
            'tethys_gizmos/vendor/bootstrap_switch/dist/js/bootstrap-switch.min.js')


def editable_google_map(context):
    """
    Dependencies for editable_google_map gizmo.
    """

    return ('tethys_gizmos/vendor/farbtastic/farbtastic.css',
            'tethys_gizmos/vendor/farbtastic/farbtastic.js',
            'tethys_gizmos/js/tethys_editable_map.js')


def google_map(context):
    """
    Dependencies for google_map gizmo.
    """
    return ('tethys_gizmos/js/tethys_map.js',)


def fetchclimate(context):
    """
    Dependencies for fetchclimate gizmo.
    """
    return ('tethys_gizmos/vendor/farbtastic/farbtastic.css',
            'tethys_gizmos/vendor/bootstrap_datepicker/css/datepicker3.css',
            'tethys_gizmos/css/fetchclimate/fetchclimate.css',
            'tethys_gizmos/css/fetchclimate/fetchclimate_map.css',
            'tethys_gizmos/css/fetchclimate/fetchclimate_plot.css',
            'tethys_gizmos/vendor/bootstrap_datepicker/js/bootstrap_datepicker.js',
            'tethys_gizmos/js/fetchclimate/fetchclimate_main.js',
            'tethys_gizmos/js/fetchclimate/fetchclimate_date.js',
            'tethys_gizmos/js/fetchclimate/fetchclimate_map.js',
            'tethys_gizmos/vendor/highcharts/js/highcharts.js',
            'tethys_gizmos/vendor/highcharts/js/highcharts-more.js',
            'tethys_gizmos/js/fetchclimate/fetchclimate_plot.js',
            'tethys_gizmos/js/fetchclimate/fetchclimate_data.js')

def range_slider(context):
    """
    Dependencies for range_slider gizmo.
    """

    return ('tethys_gizmos/css/range_slider.css',)
