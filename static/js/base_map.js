
function Initialize_map(lat,lng,zoom, target_map = 'map') {

    var apiKey = 'SdgHyawn0Rkg1lm8IrOIMaDe7Y7Gjp4k';

    var serviceUrl = 'https://api.os.uk/maps/vector/v1/vts';

    // Initialize the map.
    var mapOptions = {
        minZoom: 7,
        maxZoom: 19,
        center: [ lat, lng ],
        zoom: zoom,
        maxBounds: [
            [ 49.528423, -10.76418 ],
            [ 61.331151, 1.9134116 ]
        ],
        attributionControl: false
    };

    map = L.map(target_map, mapOptions);

    // Load and display vector tile layer on the map.
    var gl = L.mapboxGL({
        style: serviceUrl + '/resources/styles?key=' + apiKey,
        transformRequest: url => {
            return {
                url: url += '&srs=3857'
            }
        }
    }).addTo(map);
    return map
}
