import tkinter as tk
from tkinter import ttk

class AirportView:

    def __init__(self, main):
        self.main = main
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill='both', expand=True)

        """
        Create Tabs
        """
        self.airports_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.airports_frame, text='Airports')
        self.flights_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.flights_frame, text='Flights')

        """
        Create Labels and Entries for AirportView
        """
        self.create_airports_widgets()

    def create_airports_widgets(self):
        self.min_lat_label = tk.Label(self.airports_frame, text='Min Latitude:')
        self.min_lat_label.grid(row=0, column=0)
        self.min_lat_entry = tk.Entry(self.airports_frame)
        self.min_lat_entry.grid(row=0, column=1)
        self.max_lat_label = tk.Label(self.airports_frame, text='Max Latitude:')
        self.max_lat_label.grid(row=1, column=0)
        self.max_lat_entry = tk.Entry(self.airports_frame)
        self.max_lat_entry.grid(row=1, column=1)
        self.min_lon_label = tk.Label(self.airports_frame, text='Min Longitude:')
        self.min_lon_label.grid(row=2, column=0)
        self.min_lon_entry = tk.Entry(self.airports_frame)
        self.min_lon_entry.grid(row=2, column=1)
        self.max_lon_label = tk.Label(self.airports_frame, text='Max Longitude:')
        self.max_lon_label.grid(row=3, column=0)
        self.max_lon_entry = tk.Entry(self.airports_frame)
        self.max_lon_entry.grid(row=3, column=1)
        
        """
        Create a Button for AirportView
        """
        self.filter_button = tk.Button(self.airports_frame, text='Filter', command=self.filter_airports)
        self.filter_button.grid(row=4, column=0, columnspan=2)
        
        """
        Create a Table for AirportView
        """
        self.airports_table = ttk.Treeview(self.airports_frame, columns=('Airport', 'City', 'Country', 'Latitude', 'Longitude'), show='headings')
        self.airports_table.heading('Airport', text='Airport')
        self.airports_table.heading('City', text='City')
        self.airports_table.heading('Country', text='Country')
        self.airports_table.heading('Latitude', text='Latitude')
        self.airports_table.heading('Longitude', text='Longitude')
        self.airports_table.grid(row=5, column=0, columnspan=2)

    def filter_airports(self):
        """
        Function for showing the picked airports according to the given coordinates
        """
        min_lat = self.min_lat_entry.get()
        max_lat = self.max_lat_entry.get()
        min_lon = self.min_lon_entry.get()
        max_lon = self.max_lon_entry.get()
        airports = self.controller.get_airports_by_coordinates(min_lat, max_lat, min_lon, max_lon)
        """
        Fill in the table
        """
        self.airports_table.delete(*self.airports_table.get_children())
        for airport in airports:
            self.airports_table.insert('', 'end', values=(airport.airport, airport.city, airport.country, airport.latitude, airport.longitude))
    
    def set_controller(self, controller):
        """
        Set the controller
        """
        self.controller = controller

class FlightsView:

    def __init__(self, main):
        self.main = main
        self.create_flights_widgets()

    def create_flights_widgets(self):
        """
        Create Labels and Entries for FlightsView
        """
        self.city_label = tk.Label(self.main, text='City:')
        self.city_label.grid(row=0, column=0)
        self.city_entry = tk.Entry(self.main)
        self.city_entry.grid(row=0, column=1)
        """
        Create a Button for FlightsView
        """
        self.search_button = tk.Button(self.main, text='Search', command=self.search_flights)
        self.search_button.grid(row=1, column=0, columnspan=2)
        """
        Create a Table for FlightsView
        """
        self.flights_table = ttk.Treeview(self.main, columns=('From', 'To', 'Airline', 'Airplane'), show='headings')
        self.flights_table.heading('From', text='From')
        self.flights_table.heading('To', text='To')
        self.flights_table.heading('Airline', text='Airline')
        self.flights_table.heading('Airplane', text='Airplane')
        self.flights_table.grid(row=5, column=0, columnspan=2)

    def search_flights(self):
        """
        Function for showing a list of flights from and to the given city
        """
        city = self.city_entry.get()
        flights = self.controller.get_flights_by_city(city)
        flight_list = []
        for flight in flights:
            airline = flight[0]
            from_city = flight[1]
            to_city = flight[2]
            airplane = flight[3]
            if from_city == city:
                flight_list.append({'airline': airline, 'from': from_city, 'to': to_city, 'airplane': airplane})
            elif to_city == city:
                flight_list.append({'airline': airline, 'from': to_city, 'to': from_city, 'airplane': airplane})
        self.show_flights(flight_list)

    def show_flights(self, flights):
        """
        Fill in the table
        """
        self.flights_table.delete(*self.flights_table.get_children())
        for flight in flights:
            self.flights_table.insert('', 'end', values=(flight['from'], flight['to'], flight['airline'], flight['airplane']))
    
    def set_controller(self, controller):
        """
        Set the controller
        """
        self.controller = controller