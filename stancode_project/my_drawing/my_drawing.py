"""
File: Let's go the infinity and beyond
Name: Abbie Chen
----------------------
TODO: this is buzz
he will lead us to the infinity and beyond
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    this program will use oval, rect, arc, triangle and label to create my buzz
    """
    window = GWindow(600, 600, title='my_buzz')
    wing1 = GRect(450, 80, x=60, y=300)
    wing1.filled = True
    wing1.fill_color = 'purple'
    wing1.color = 'purple'
    window.add(wing1)
    wing4 = GRect(450, 40, x=60, y=300)
    wing4.filled = True
    wing4.fill_color = 'white'
    wing4.color = 'white'
    window.add(wing4)
    wing5 = GPolygon()
    wing5.add_vertex((60, 300))
    wing5.add_vertex((90, 300))
    wing5.add_vertex((90, 340))
    wing5.filled = True
    wing5.fill_color = 'red'
    wing5.color = 'red'
    window.add(wing5)
    wing6 = GPolygon()
    wing6.add_vertex((90, 300))
    wing6.add_vertex((120, 300))
    wing6.add_vertex((120, 340))
    wing6.filled = True
    wing6.fill_color = 'red'
    wing6.color = 'red'
    window.add(wing6)
    wing7 = GPolygon()
    wing7.add_vertex((120, 300))
    wing7.add_vertex((150, 300))
    wing7.add_vertex((150, 340))
    wing7.filled = True
    wing7.fill_color = 'red'
    wing7.color = 'red'
    window.add(wing7)
    wing8 = GPolygon()
    wing8.add_vertex((400, 340))
    wing8.add_vertex((400, 300))
    wing8.add_vertex((430, 300))
    wing8.filled = True
    wing8.fill_color = 'red'
    wing8.color = 'red'
    window.add(wing8)
    wing9 = GPolygon()
    wing9.add_vertex((430, 340))
    wing9.add_vertex((430, 300))
    wing9.add_vertex((460, 300))
    wing9.filled = True
    wing9.fill_color = 'red'
    wing9.color = 'red'
    window.add(wing9)
    wing10 = GPolygon()
    wing10.add_vertex((460, 340))
    wing10.add_vertex((460, 300))
    wing10.add_vertex((490, 300))
    wing10.filled = True
    wing10.fill_color = 'red'
    wing10.color = 'red'
    window.add(wing10)
    wing11 = GPolygon()
    wing11.add_vertex((490, 340))
    wing11.add_vertex((490, 300))
    wing11.add_vertex((520, 300))
    wing11.filled = True
    wing11.fill_color = 'red'
    wing11.color = 'red'
    window.add(wing11)
    wing2 = GRect(30, 100, x=30, y=290)
    wing2.filled = True
    wing2.fill_color = 'green'
    wing2.color = 'green'
    window.add(wing2)
    wing3 = GRect(30, 100, x=510, y=290)
    wing3.filled = True
    wing3.fill_color = 'green'
    wing3.color = 'green'
    window.add(wing3)
    body = GOval(250, 400, x=150, y=100)
    body.filled = True
    body.fill_color = 'skyblue'
    body.color ='skyblue'
    window.add(body)
    head = GOval(200, 300, x=175, y=150)
    head.filled = True
    head.fill_color = 'purple'
    head.color = 'purple'
    window.add(head)
    l_ear = GOval(70, 70, x=170, y=200)
    l_ear.filled = True
    l_ear.fill_color = 'purple'
    l_ear.color = 'purple'
    window.add(l_ear)
    r_ear = GOval(70, 70, x=310, y=200)
    r_ear.filled = True
    r_ear.fill_color = 'purple'
    r_ear.color = 'purple'
    window.add(r_ear)
    face = GOval(180, 250, x=185, y=180)
    face.filled = True
    face.fill_color = 'bisque'
    face.color = 'bisque'
    window.add(face)
    cloth_7 = GOval(175, 140, x=190, y=360)
    cloth_7.filled = True
    cloth_7.fill_color = 'mediumseagreen'
    cloth_7.color = 'mediumseagreen'
    window.add(cloth_7)
    cloth_2 = GRect(210, 80, x=170, y=360)
    cloth_2.filled = True
    cloth_2.fill_color = 'white'
    cloth_2.color = 'white'
    window.add(cloth_2)
    l_cloth2 = GPolygon()
    l_cloth2.add_vertex((155, 360))
    l_cloth2.add_vertex((170, 360))
    l_cloth2.add_vertex((170, 410))
    l_cloth2.filled = True
    l_cloth2.fill_color = "white"
    l_cloth2.color = "white"
    window.add(l_cloth2)
    r_cloth2 = GPolygon()
    r_cloth2.add_vertex((395, 360))
    r_cloth2.add_vertex((380, 360))
    r_cloth2.add_vertex((380, 410))
    r_cloth2.filled = True
    r_cloth2.fill_color = "white"
    r_cloth2.color = "white"
    window.add(r_cloth2)
    cloth_1 = GRect(250, 50, x=150, y=310)
    cloth_1.filled = True
    cloth_1.fill_color = 'mediumseagreen'
    cloth_1.color = 'mediumseagreen'
    window.add(cloth_1)
    bottom_1 = GOval(15, 30, x=180, y=320)
    bottom_1.filled = True
    bottom_1.fill_color = 'dodgerblue'
    bottom_1.color = 'dodgerblue'
    window.add(bottom_1)
    bottom_2 = GOval(15, 30, x=200, y=320)
    bottom_2.filled = True
    bottom_2.fill_color = 'green'
    bottom_2.color = 'green'
    window.add(bottom_2)
    bottom_3 = GOval(15, 30, x=220, y=320)
    bottom_3.filled = True
    bottom_3.fill_color = 'red'
    bottom_3.color = 'red'
    window.add(bottom_3)
    bottom_4 = GOval(30, 30, x=340, y=320)
    bottom_4.filled = True
    bottom_4.fill_color = 'red'
    bottom_4.color = 'red'
    window.add(bottom_4)
    cloth_3 = GPolygon()
    cloth_3.add_vertex((160, 360))
    cloth_3.add_vertex((240, 360))
    cloth_3.add_vertex((185, 440))
    cloth_3.filled = True
    cloth_3.fill_color = 'purple'
    cloth_3.color = 'purple'
    window.add(cloth_3)
    cloth_4 = GPolygon()
    cloth_4.add_vertex((160, 360))
    cloth_4.add_vertex((220, 360))
    cloth_4.add_vertex((175, 420))
    cloth_4.filled = True
    cloth_4.fill_color = 'white'
    cloth_4.color = 'white'
    window.add(cloth_4)
    cloth_5 = GPolygon()
    cloth_5.add_vertex((320, 360))
    cloth_5.add_vertex((400, 360))
    cloth_5.add_vertex((370, 440))
    cloth_5.filled = True
    cloth_5.fill_color = 'purple'
    cloth_5.color = 'purple'
    window.add(cloth_5)
    cloth_6 = GPolygon()
    cloth_6.add_vertex((340, 360))
    cloth_6.add_vertex((400, 360))
    cloth_6.add_vertex((400, 440))
    cloth_6.filled = True
    cloth_6.fill_color = 'white'
    cloth_6.color = 'white'
    window.add(cloth_6)
    mouth = GOval(50, 50, x=250, y=260)
    mouth.filled = True
    mouth.fill_color = 'red'
    mouth.color = 'red'
    window.add(mouth)
    mouth_1 = GOval(45, 45, x=250, y=250)
    mouth_1.filled = True
    mouth_1.fill_color = 'bisque'
    mouth_1.color = 'bisque'
    window.add(mouth_1)
    l_eye = GOval(35, 35, x=225, y=230)
    l_eye.filled = True
    window.add(l_eye)
    r_eye = GOval(35, 35, x=300, y=230)
    r_eye.filled = True
    window.add(r_eye)
    dialog = GRect(160, 90, x=50, y=50)
    dialog.filled = True
    dialog.fill_color = 'grey'
    dialog.color = 'grey'
    window.add(dialog)
    dialog1 = GPolygon()
    dialog1.add_vertex((120, 140))
    dialog1.add_vertex((160, 170))
    dialog1.add_vertex((160, 140))
    dialog1.filled = True
    dialog1.fill_color = 'grey'
    dialog1.color = 'grey'
    window.add(dialog1)
    label = GLabel(' To infinity and  ', x=60, y=100)
    window.add(label)
    label1 = GLabel(' beyond SC101!', x=60, y=130)
    label1.font = '-20'
    window.add(label1)


if __name__ == '__main__':
    main()
