class AirportController:

    def __init__(self, model, airport_view, flights_view):
        self.model = model
        self.airport_view = airport_view
        self.flights_view = flights_view
        self.airport_view.set_controller(self)
        self.flights_view.set_controller(self)

    def get_airports_by_coordinates(self, min_lat, max_lat, min_lon, max_lon):
        """
        Function for getting the airports from Model and showing them in View
        """
        airports = self.model.get_airports_by_coordinates(min_lat, max_lat, min_lon, max_lon)
        return airports
       
    
    def get_flights_by_city(self, city):
        """
        Function for getting the flights from Model and showing them in View
        """
        flights = self.model.get_flights_by_city(city)
        return flights
     
    def close(self):
        self.model.close()