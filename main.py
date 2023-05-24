def on_button_pressed_a():
    global counter
    counter += 1
    basic.show_number(counter)
input.on_button_pressed(Button.A, on_button_pressed_a)

counter = 0
counter = 0