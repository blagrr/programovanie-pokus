def on_forever():
    if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        led.enable(True)
    else:
        led.enable(False)
basic.forever(on_forever)
