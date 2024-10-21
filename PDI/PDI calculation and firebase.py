import math
import pyrebase
class PDIAnalyzer:
    def __init__(self, k1, k2):
        self.k1 = k1
        self.k2 = k2

    def calculate_pdi(self, zacc, xgyro, ygyro):
        # Ensure the value inside sqrt is non-negative
        return math.sqrt(max(0, zacc**2 + self.k1 * xgyro**2 + self.k2 * ygyro**2))

# Constants
k1 = 0.35087277493985447
k2 = 0.59843378684492

# Create an instance of PDIAnalyzer
analyzer = PDIAnalyzer(k1, k2)

# Example usage
zacc = 0
xgyro = -1.496183206
ygyro = -3.633587786

# Calculate PDI for the given parameters
pdi = analyzer.calculate_pdi(zacc, xgyro, ygyro)
print(f"zacc: {zacc}, xgyro: {xgyro}, ygyro: {ygyro} -> PDI: {pdi}")

import pyrebase

def push_user_to_firebase(longitude, latitude, pdi, config):
    # Initialize the Firebase app with the given configuration
    firebase = pyrebase.initialize_app(config)

    # Get a reference to the database service
    database = firebase.database()

    # Check if the same name and age combination already exists
    users = database.child('users').get()
    if users.each():
        for user in users.each():
            user_data = user.val()
            if user_data['longitude'] == longitude and user_data['latitude'] == latitude:
                if user_data['pdi'] == pdi:
                    print("Data with the same name, age, and class already exists. Not pushing to the database.")
                    return
                else:
                    # Update the existing record with the new class
                    database.child('users').child(user.key()).update({'pdi': pdi})
                    print("Data updated in the database.")
                    return

    # If name and age combination does not exist, push the data to the 'users' node
    data = {
        'longitude': longitude,
        'latitude': latitude,
        'pdi': pdi
    }

    database.child('users').push(data)
    print("Data pushed to the database.")

# Firebase configuration
config = {
 "apiKey": "AIzaSyDv9aVCAK3QfpyZPsRzekJlc3MsBfZoxrg",
  "authDomain": "test-f6ef2.firebaseapp.com",
  "databaseURL": "https://test-f6ef2-default-rtdb.firebaseio.com",
 "projectId": "test-f6ef2",
  "storageBucket": "test-f6ef2.appspot.com",
  "messagingSenderId": "148456236172",
  "appId": "1:148456236172:web:8a09751c0fd0a1a76f47a9",
  "measurementId": "G-MX40KYM5YS"
}

# Example usage
push_user_to_firebase(longitude,latitude , pdi, config)