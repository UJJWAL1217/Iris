import phonenumbers
import folium
import pywhatkit as pwk
from datetime import datetime

from myNumber import number


def sos():
    from phonenumbers import geocoder
    sanNumber = phonenumbers.parse(number)
    yourLocation = geocoder.description_for_number(sanNumber, "en")
    print(yourLocation)

    # get service provider
    from phonenumbers import carrier

    service_provider = phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider, "en"))

    from opencage.geocoder import OpenCageGeocode

    key = "6c88f3edf15448a582a99183d722b39c"

    geocoder = OpenCageGeocode(key)

    query = str(yourLocation)

    result = geocoder.geocode(query)
    print(result)

    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']

    print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start=9)

    folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

    # save map in html file

    myMap.save("myLocation.html")

    now = datetime.now()
    Hr = now.strftime("%H")
    Min = now.strftime("%M")

    #
    try:
        # sending message in Whatsapp in India so using Indian dial code (+91)
        pwk.sendwhatmsg("+917974848773", "help! help! help!", int(Hr), int(Min) + 1)

        print("Message Sent!")  # Prints success message in console

        # error message
    except:
        print("Error in sending the message")

    try:
        # sending message in Whatsapp in India so using Indian dial code (+91)
        pwk.sendwhatmsg("+917974848773", str(result), int(Hr), int(Min) + 2)

        print("Message Sent!")  # Prints success message in console

        # error message
    except:
        print("Error in sending the message")
    ###########################################################
    try:
        # sending message in Whatsapp in India so using Indian dial code (+91)
        pwk.sendwhatmsg("+917974848773", "longitude" + str(lat), int(Hr), int(Min) + 3)

        print("Message Sent!")  # Prints success message in console

        # error message
    except:
        print("Error in sending the message")

    try:
        # sending message in Whatsapp in India so using Indian dial code (+91)
        pwk.sendwhatmsg("+917974848773", "latitude" + str(lat), int(Hr), int(Min) + 4)

        print("Message Sent!")  # Prints success message in console

        # error message
    except:
        print("Error in sending the message")
# sos()