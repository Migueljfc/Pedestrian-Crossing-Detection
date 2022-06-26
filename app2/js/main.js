const obuIcon = L.icon({
    iconUrl: 'img/blue-circle.png',
    iconSize: [10, 10],
    iconAnchor: [5, 5]
});
const rsuIcon = L.icon({
    iconUrl: 'img/yellow-circle.png',
    iconSize: [10, 10],
    iconAnchor: [5, 5]
});

var map = L.map('mapid').setView([ 40.630291, -8.654298 ], 90);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([  40.630366, -8.653955 ], {icon:obuIcon}).addTo(map)
    .bindPopup('obu1');

L.marker([ 40.630238, -8.653885 ], {icon:obuIcon}).addTo(map)
    .bindPopup('obu2');

L.marker([40.630093, -8.653802], {icon:obuIcon}).addTo(map)
    .bindPopup('obu3');

