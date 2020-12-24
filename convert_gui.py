import math
import PySimpleGUI as sg

# 参考になったURL
# https://qiita.com/dario_okazaki/items/656de21cab5c81cabe59
# https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Python

def window_init():
    sg.theme('Dark Blue 3')

    layout = [
        [sg.Text('lat_deg', size=(15,1)), sg.InputText('')],
        [sg.Text('lon_deg', size=(15,1)), sg.InputText('')],
        [sg.Text('zoomLevel', size=(15,1)), sg.InputText('')],
        [sg.Button(button_text='Convert')],
        [sg.Text('Tile Number',key='RESULT')] 
    ]

    window = sg.Window('Convert LatLng to Tile Number', layout)

    while True:
        event, values = window.read()

        if event is None:
            print('exit')
            break

        if event == "Convert":
            try:
                result = deg2num(float(values[0]),float(values[1]),float(values[2]))
                window['RESULT'].update(result)
            except ValueError:
                window['RESULT'].update('Vaule Error Occurred..')

            
    window.close()


def deg2num(lat_deg, lon_deg, zoom):
    print(type(lat_deg))
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (xtile, ytile)


if __name__ == "__main__":
    window_init()
