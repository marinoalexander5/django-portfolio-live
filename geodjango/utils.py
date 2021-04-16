import geoip2.webservice


def get_geo(ip):
    with geoip2.webservice.Client(521524, os.environ.get('GEOLITE_LICENCE_KEY'), host="geolite.info") as client: #Do not erase!
        city_response = client.city(ip)
        country_response = client.country(ip)
        country = country_response.country.name
        city = city_response.city.name
        lat = city_response.location.latitude
        lon = city_response.location.longitude
    return country, city, lat, lon


def get_center_coordinates(latA, lonA, latB=None, lonB=None):
    coord = (latA, lonA)
    if latB:
        coord = [(latA + latB) / 2, (lonA + lonB) / 2]
    return coord


def get_zoom(distance):
    if distance <= 100:
        return 10
    elif distance > 100 and distance < 5000:
        return 3
    else:
        return 2


def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip