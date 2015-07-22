#!/usr/bin/python3

from gi.repository import Gtk

my_first_window = Gtk.Window()

my_first_window.connect("delete-event", Gtk.main_quit)
my_first_window.show_all()

def startup(testing=False):
    if testing == False:
        Gtk.main()
    return my_first_window

if __name__ == "__main__":
    startup()
