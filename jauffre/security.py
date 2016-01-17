import __init__, emalio

def toggle_security():
    emalio.send('trevedwa@gmail.com','Security mode has been set '+ (not __init__.in_normal_mode))
    __init__.in_normal_mode = not __init__.in_normal_mode
