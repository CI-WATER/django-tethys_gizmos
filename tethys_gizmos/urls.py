from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'tethys_gizmos.views.gizmo_showcase.index', name='showcase'),
    url(r'^editable-map/$', 'tethys_gizmos.views.gizmo_showcase.', name='editable_map'),
    url(r'^google-map/$', 'tethys_gizmos.views.gizmo_showcase.', name='google_map'),
    url(r'^map-view', 'tethys_gizmos.views.gizmo_showcase.', name='map_view'),
    url(r'^fetch-climate-map/$', 'tethys_gizmos.views.gizmo_showcase.', name='fetch_climate_map'),
)