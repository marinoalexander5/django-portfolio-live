from django.shortcuts import render
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address
import folium

def calculate_distance_view(request):
    form = MeasurementModelForm(request.POST or None)
    destination = None
    distance = None

    geolocator = Nominatim(user_agent='geodjango')
    
    ip = get_ip_address(request)
    country, city, l_lat, l_lon = get_geo(ip)

    # location coordinates
    location = geolocator.reverse(f'{l_lat}, {l_lon}')
    pointA = (l_lat, l_lon)
    d_lat = l_lat
    d_lon = l_lon

    m = folium.Map(width='100%', height='100%', location=get_center_coordinates(l_lat, l_lon), min_zoom=1)

    # Current IP location
    folium.Marker([l_lat, l_lon], tooltip='Click for details', popup=city,
        icon=folium.Icon(color='red', icon='fa map-marker-alt')).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)
        input_destination = form.cleaned_data.get('destination')
        destination = geolocator.geocode(input_destination)


        # destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude

        pointB = (d_lat, d_lon)

        distance = round(geodesic(pointA, pointB).km, 2)

        # Redraw Map
        m = folium.Map(width='100%', height='100%', location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon), zoom_start=get_zoom(distance), min_zoom=1.5) 

        # Current IP location
        folium.Marker([l_lat, l_lon], tooltip='Click for details', popup=city,
            icon=folium.Icon(color='red', icon='fa map-marker-alt')).add_to(m)

        # Destination location
        folium.Marker([d_lat, d_lon], tooltip='Click for details', popup=destination,
            icon=folium.Icon(color='red', icon='fa map-pin')).add_to(m)

        # Connect location and destination with a line
        line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='blue')
        m.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()

    m.fit_bounds([[min(l_lat, d_lat), min(l_lon, d_lon)] , [max(l_lat, d_lat), max(l_lon, d_lon)]], padding=(9,9))

    # Convert object to HTML
    m = m._repr_html_()

    context = {
        'distance': distance,
        'form': form,
        'map': m,
        'destination': destination,
    }

    return render(request, 'geodjango/main.html', context)