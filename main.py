import requests

f = open('nerdwords', 'r')
words = f.read().split()

available = []

def plateChecker(plate):
    base_url = 'https://services.dps.ohio.gov/BMVOnlineServices/VR/Availability/Passenger/GetAvailability?vehicleClass=&newPlate={0}&organizationCode=0'.format(plate)

    r = requests.get(base_url)

    if 'currently available' in r.text:
        print('License Plate [AVAILABLE]: {0} available'.format(plate))
    elif 'unavailable' in r.text:
        print('License Plate [NOT AVAILABLE]: {0} unavailable'.format(plate))

for word in words:
    plateChecker(word)

print(available)