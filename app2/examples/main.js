const obuIcon = L.icon({
    iconUrl: '../img/blue-circle.png',
    iconSize: [10, 10],
    iconAnchor: [5, 5]
});
const rsuIcon = L.icon({
    iconUrl: '../img/yellow-circle.png',
    iconSize: [10, 10],
    iconAnchor: [5, 5]
});

var map = L.map('map').setView([ 40.629036, -8.652790], 100);
layer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Maps © <a href=\"www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors',
}).addTo(map);


var obu1 = [[40.628816, -8.653032], [40.630366, -8.653955]];
var obu2 = [[40.628710, -8.652978], [40.630238, -8.653885]];
var obu3 = [[40.628641, -8.652930], [40.630198, -8.653849]];

var marker2 = L.Marker.movingMarker(obu1,
    [3000], {autostart: true}).addTo(map);

marker2.on('end', function() {
    marker2.bindPopup('<b>Stop !</b>', {closeOnClick: false})
    .openPopup();
    
});    

var marker3 = L.Marker.movingMarker(obu2,
    [4000], {autostart: true}).addTo(map);

marker3.on('end', function() {
    marker3.bindPopup('<b>Stop !</b>', {closeOnClick: false})
    .openPopup();
    
});

var marker4 = L.Marker.movingMarker(obu3,
    [4000], {autostart: true}).addTo(map);

marker4.on('end', function() {
    marker4.bindPopup('<b>Stop !</b>', {closeOnClick: false})
    .openPopup();
});

/* L.marker([  40.630366, -8.653955 ], {icon:obuIcon}).addTo(map)
    .bindPopup('obu1');

L.marker([ 40.630238, -8.653885 ], {icon:obuIcon}).addTo(map)
    .bindPopup('obu2');

L.marker([40.630093, -8.653802], {icon:obuIcon}).addTo(map)
    .bindPopup('obu3'); */

L.marker([40.630291, -8.654298], {icon:rsuIcon}).addTo(map)
    .bindPopup('rsu');