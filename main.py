counter = 0

def on_forever():
    global counter
    counter += 1
basic.forever(on_forever)
