/*****************************************************************************
 * FILE:    Tethys Map View Library
 * DATE:    February 4, 2015
 * AUTHOR:  Nathan Swain
 * COPYRIGHT: (c) 2015 Brigham Young University
 * LICENSE: BSD 2-Clause
 *****************************************************************************/

/*****************************************************************************
 *                      LIBRARY WRAPPER
 *****************************************************************************/

var TETHYS_MAP_VIEW = (function() {
	// Wrap the library in a package function
	"use strict"; // And enable strict mode for this library

	/************************************************************************
 	*                      MODULE LEVEL / GLOBAL VARIABLES
 	*************************************************************************/
 	var public_interface,				// Object returned by the module
      m_map_target,           // Selector for the map container
      m_map;					        // The map

	/************************************************************************
 	*                    PRIVATE FUNCTION DECLARATIONS
 	*************************************************************************/
 	var open_layers_base_map_init, open_layers_controls_init, open_layers_map_init;


 	/************************************************************************
 	*                    PRIVATE FUNCTION IMPLEMENTATIONS
 	*************************************************************************/

  // Initialize the background map
  open_layers_base_map_init = function()
  {
    // Constants
    var OPEN_STEET_MAP = 'OpenStreetMap',
        BING = 'Bing',
        MAP_QUEST = 'MapQuest';


    // Declarations
    var base_map_json,
        base_map_layer,
        base_map_obj;

    // Default base map
    base_map_layer = new ol.layer.Tile({
      source: new ol.source.OSM()
    });

    // Get control settings from data attribute
    base_map_json = $('#' + m_map_target).attr('data-base-map');

    if (typeof base_map_json !== typeof undefined && base_map_json !== false) {
      base_map_obj = JSON.parse(base_map_json);

      if (typeof base_map_obj === 'string') {
        if (base_map_obj === OPEN_STEET_MAP) {
          // Initialize default open street map layer
          base_map_layer = new ol.layer.Tile({
            source: new ol.source.OSM()
          });

        } else if (base_map_obj === BING) {
          // Initialize default bing layer

        } else if (base_map_obj === MAP_QUEST) {
          // Initialize default map quest layer
          base_map_layer = new ol.layer.Tile({
            source: new ol.source.MapQuest({layer: 'sat'})
          });

        }

      } else if (typeof base_map_obj === 'object') {

        if (OPEN_STEET_MAP in base_map_obj) {
          // Initialize custom open street map layer
          base_map_layer = new ol.layer.Tile({
            source: new ol.source.OSM(base_map_obj[OPEN_STEET_MAP])
          });

        } else if (BING in base_map_obj) {
          // Initialize custom bing layer
          base_map_layer = new ol.layer.Tile({
            preload: Infinity,
            source: new ol.source.BingMaps(base_map_obj[BING])
          });

        } else if (MAP_QUEST in base_map_obj) {
          // Initialize custom map quest layer
          base_map_layer = new ol.layer.Tile({
            source: new ol.source.MapQuest(base_map_obj[MAP_QUEST])
          });
        }

      }



      console.log(base_map_json);
    }

    m_map.addLayer(base_map_layer);
  };

  // Initialize the controls
  open_layers_controls_init = function()
  {
    // Constants
    var ZOOM_SLIDER = 'zoomslider',
        ROTATE = 'rotate',
        ZOOM_EXTENT = 'zoomtoextent',
        FULL_SCREEN = 'fullscreen',
        MOUSE_POSITION = 'mouseposition',
        SCALE_LINE = 'scaleline';

    var controls_json,
        controls_list,
        controls;

    // Get control settings from data attribute
    controls_json = $('#' + m_map_target).attr('data-controls');

    // Start with defaults
    controls = ol.control.defaults();

    if (typeof controls_json !== typeof undefined && controls_json !== false) {
      controls_list = JSON.parse(controls_json);

      for (var i = 0; i < controls_list.length; i++) {
        if (controls_list[i].toLowerCase() === ZOOM_SLIDER) {
          m_map.addControl(new ol.control.ZoomSlider());
        }

        if (controls_list[i].toLowerCase() === ROTATE) {
          m_map.addControl(new ol.control.Rotate());
        }

        if (controls_list[i].toLowerCase() === ZOOM_EXTENT) {
          m_map.addControl(new ol.control.ZoomToExtent());
        }

        if (controls_list[i].toLowerCase() === FULL_SCREEN) {
          m_map.addControl(new ol.control.FullScreen());
        }

        if (controls_list[i].toLowerCase() === MOUSE_POSITION) {
          m_map.addControl(new ol.control.MousePosition());
        }

        if (controls_list[i].toLowerCase() === SCALE_LINE) {
          m_map.addControl(new ol.control.ScaleLine());
        }
      }
    }

    return controls;

  };

  // Initialize the map
 	open_layers_map_init = function()
  {
    // Init Map
    m_map = new ol.Map({
      target: m_map_target,
      view: new ol.View({
        center: ol.proj.transform([37.41, 8.82], 'EPSG:4326', 'EPSG:3857'),
        zoom: 4
      })
    });

    // Init controls
    open_layers_controls_init();

    // Init background map
    open_layers_base_map_init();

  };

	/************************************************************************
 	*                        DEFINE PUBLIC INTERFACE
 	*************************************************************************/
	/*
	 * Library object that contains public facing functions of the package.
	 * This is the object that is returned by the library wrapper function.
	 * See below.
	 * NOTE: The functions in the public interface have access to the private
	 * functions of the library because of JavaScript function scope.
	 */
  public_interface = {
    hello_goodbye: function() {
      hello_world();
      goodbye_world();
    },
    my_name_is: function(name) {
      console.log("My Name Is: " + name);
    }
  };

	/************************************************************************
 	*                  INITIALIZATION / CONSTRUCTOR
 	*************************************************************************/

	// Initialization: jQuery function that gets called when
	// the DOM tree finishes loading
	$(function() {
    // Map container selector
    m_map_target = 'map_view';

    // Initialize the map
    open_layers_map_init();

	});

	return public_interface;

}()); // End of package wrapper
// NOTE: that the call operator (open-closed parenthesis) is used to invoke the library wrapper
// function immediately after being parsed.