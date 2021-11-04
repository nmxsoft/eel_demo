import eel

eel.init('web')


@eel.expose
def todo(n):
    return int(n) * int(n)


eel.start('index.html', size=(450, 200), mode="chrome")
