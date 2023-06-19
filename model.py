import sqlite3

class Airport:
    def __init__(self, airport, city, country, latitude, longitude):
        """
        Access to attributes and methods
        """
        self.airport = airport
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

class AirportModel:

    def __init__(self, db_name):
        """
        Create database connection
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_airports_by_coordinates(self, min_lat, max_lat, min_lon, max_lon):
        """
        Function for picking airports from the database according to the given coordinates
        """
        self.cursor.execute('''
            SELECT airport, city, country, latitude, longitude
            FROM airports
            WHERE latitude >= ? AND latitude <= ? AND longitude >= ? AND longitude <= ?
        ''', (min_lat, max_lat, min_lon, max_lon))
        rows = self.cursor.fetchall()
        airports = []
        for row in rows:
            airport = Airport(*row)
            airports.append(airport)
        return airports
    
    def get_flights_by_city(self, city):
        """
        Function for creating a tuple of flights from and to the given city
        """
        self.cursor.execute('''SELECT al.name, a1.city, a2.city, r.airplane
                FROM routes r
                JOIN airports a1 ON r.src_airport = a1.iata
                JOIN airports a2 ON r.dst_airport = a2.iata
                JOIN airlines al ON r.airline_id = al.id
                WHERE a1.city = ? OR a2.city = ?''', (city, city))
        flights = self.cursor.fetchall()
        flights = [list(flight) for flight in flights]
        """
        Turn a tuple into a list
        """  
        return flights
   
    def close(self):
        """
        Close database connection 
        """
        self.conn.close()

    
    
