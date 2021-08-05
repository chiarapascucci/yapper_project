function initAutoComplete() {
    var location = {
        lat: 40.000,
        lng: -79.000
    }
    var options = {
        center: location,
        zoom: 9
    }
    map = new google.maps.Map(document.getElementById("map"), options);
}