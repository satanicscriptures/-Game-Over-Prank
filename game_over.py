import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GLib

def on_window_destroy(window):
    Gtk.main_quit()

def on_button_clicked(button):
    # Create a new window
    window = Gtk.Window()
    window.set_title("Game Over")
    window.set_position(Gtk.WindowPosition.CENTER)
    window.fullscreen()  # Set window to full-screen

    # Create a black overlay to cover the entire screen
    overlay = Gtk.Overlay()
    window.add(overlay)

    # Create a drawing area for the black overlay
    black_overlay = Gtk.DrawingArea()
    black_overlay.connect("draw", draw_black_overlay)  # Connect draw event to draw_black_overlay function
    overlay.add_overlay(black_overlay)

    # Create a label for "GAME OVER" text
    label = Gtk.Label(label="GAME OVER")
    label.override_color_rgba(Gdk.RGBA(1, 0, 0, 1))  # Set text color to red
    label.override_font_description(Pango.FontDescription("Courier Bold 100"))  # Set font and size
    overlay.add_overlay(label)

    # Display the window
    window.show_all()

    # Close the window after 2 minutes (120,000 milliseconds)
    GLib.timeout_add(120000, close_window, window)

    # Beep every 10 seconds during the 2-minute duration
    for i in range(12):
        GLib.timeout_add(i * 10000, beep)

def draw_black_overlay(widget, context):
    # Draw a semi-transparent black rectangle covering the entire drawing area
    context.set_source_rgba(0, 0, 0, 0.7)  # Set color to black with 70% opacity
    context.rectangle(0, 0, widget.get_allocated_width(), widget.get_allocated_height())
    context.fill()

def close_window(window):
    window.destroy()
    return False  # Stop the timeout

def beep():
    os.system("sudo modprobe pcspkr && beep -f 1000 -l 50")  # Beep with frequency 1000 Hz and duration 50 milliseconds
    return False  # Stop the timeout

def main():
    # Create a new window
    window = Gtk.Window()
    window.connect("destroy", on_window_destroy)

    # Create a button
    button = Gtk.Button(label="Click Me")
    button.connect("clicked", on_button_clicked)

    # Add the button to the window
    window.add(button)

    # Display the window
    window.show_all()

    # Start the GTK main loop
    Gtk.main()

if __name__ == "__main__":
    main()
