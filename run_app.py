import tkinter as tk
from model import AirportModel
from view import AirportView, FlightsView
from controller import AirportController

if __name__ == '__main__':
    """
    Set Model and connection
    """
    db_name = 'airports.db'
    model = AirportModel(db_name)
    """
    Set View
    """
    root = tk.Tk()
    root.title('Airports Finder')
    airport_view = AirportView(root)
    flights_view = FlightsView(airport_view.flights_frame)
    """
    Set Controller and connection
    """
    controller = AirportController(model, airport_view, flights_view)
    flights_view.set_controller(controller)
    """
    Start the cycle
    """
    root.mainloop()
    """
    Close connection
    """
    controller.close()


# if __name__ == '__main__':
#     db_name = 'airports.db'
#     model = AirportModel(db_name)
#     root = tk.Tk()
#     root.title('Airports Finder')
#     airport_view = AirportView(root)
#     flights_view = FlightsView(airport_view.flights_frame)
#     controller = AirportController(model, airport_view, flights_view)
#     root.mainloop()
#     controller.close()

    