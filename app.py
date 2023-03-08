#pyinstaller --onefile -w ntg.py
import sdef as s
import data as do
import PySimpleGUI as sg
import re
import pyautogui
import time as t
import datetime as dt
my_window=pyautogui.size()
width=my_window[0]
height=my_window[1]
d = dt.date.today()
lo=t.localtime()
weekDays = ("Monday", "Tuesday",
                   "Wednesday", "Thursday",
                   "Friday", "Saturday",
                   "Sunday")
def t_to_m(hour, minute):
    return hour*60+minute
color="cyan"
t1=''
i=0
table_content=[["","2nd Year"],["IOT","-----","-----"],["CS","-----","-----"],["DS","-----","-----"]]
table_content2=[["","3rd Year"],["IOT","-----","-----"],["CS","-----","-----"],["DS","-----","-----"],
                ["","4th Year"],["IOT","-----","-----"],["CS","-----","-----"],["DS","-----","-----"]]
def create_window(theme):
    sg.theme(theme)
    layout=[[sg.Text(" ",font= "Franklin 12")],
        [sg.Image(filename="mrcet.png"),
         sg.Text("    "),
         sg.Text("MRCET   ",font= "Franklin 42",
                 justification="center",right_click_menu=theme_menu)],
        [sg.Image(filename="et .png"),
         sg.Text("Welcome to Department of Emerging Technologies",
                 font= "Franklin 28",justification="center")],
        [sg.Text(t1,key='time',pad=(0,10), font="Franklin 36", justification="center"),
         sg.Text("                "),
         sg.Text("",key='date',font= "Franklin 36",justification="center"),
         sg.Text("            "),
         sg.Text("",key='day',font= "Franklin 36")],
        [sg.Text("CURRENT SESSION",border_width=5,
                 relief="sunken",font= "Franklin 35",justification="center")],
        [sg.Text("    "),
         sg.Text("",key='period',background_color=color,
                                 font= "Franklin 35"),
         sg.Text(" "),
         sg.Text("[--:-- - --:--]",key="timestamp",font="Franklin 30")],
        [sg.Table(headings=["Section","Subject","Teacher"],values=table_content,
                  expand_x=True,auto_size_columns=False,hide_vertical_scroll=True,
                  key="-table-",num_rows=4,
                  row_colors=((0,color),(4,color),(8,color)),
                  row_height=48,justification="center",sbar_width=20)],
        [sg.Text("    "),
         sg.Text("", key='period2', background_color=color,
                     font="Franklin 35"),
         sg.Text(" "),
         sg.Text("[--:-- - --:--]", key="timestamp2", font="Franklin 30")],
        [sg.Table(headings=["Section", "Subject", "Teacher"], values=table_content2,
                      expand_x=True, auto_size_columns=False, hide_vertical_scroll=True,
                      key="-table2-", num_rows=8,
                      row_colors=((0, color), (4, color), (8, color)),
                      row_height=48, justification="center", sbar_width=20)],
        [sg.Text("Designed by S.Praveen (IoT 3rd Year)",font="Helvetica 20")],
        [sg.VPush()]
    ]

    return sg.Window('Period Details', layout,finalize=True,
                     element_justification='center',
                     no_titlebar=False, location=(0, 0),
                     size=(1920,1080),font='Helvetica 30', keep_on_top=True)
theme_menu=['menu',['random','Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']]
window = create_window('Gray Gray Gray')

p="end"
np_11=[]
np_22=[]
np_33=[]
np_44=[]
np_ll=[]
np_55=[]
np_66=[]
np_77=[]
np_e=[]
p2="end"
while True:
    event,values=window.read(timeout=1000)
    t1="".join([str(t.localtime().tm_hour),' : ',str(t.localtime().tm_min)," : ",str(t.localtime().tm_sec)])
    d1="".join([str(d.day)," - ",str(d.month)," - ",str(d.year)])
    w1=weekDays[t.localtime().tm_wday]
    # w1="Tuesday"
    window['time'].update(t1)
    window['date'].update(d1)
    window['day'].update(w1)
    if event=="" or event==sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window=create_window(event)
    if t.localtime().tm_wday!=6:
      cur_t=[(t.localtime().tm_hour),(t.localtime().tm_min)]

      if cur_t[0]>=16:
        p="END"
        p2="END"
      else:
        #second year timing end period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(15,50):
            window["timestamp"].update("[15:50-00:00]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", "-----", "-----"],
                             ["CS", "-----", "-----"],
                             ["DS", "-----", "-----"]]
            window["-table-"].update(values=table_content, row_colors=((0, color), (4, color),(8,color)))
        #third year timings
        if t_to_m(cur_t[0], cur_t[1]) >= t_to_m(15, 30):
            window["timestamp2"].update("[15:30-00:00]")
            table_content2 = [["", "3rd YEAR"],
                              ["IOT", "-----", "-----"],
                              ["CS", "-----", "-----"],
                              ["DS", "-----", "-----"],
                              ["", "4th YEAR"],
                              ["IOT", "-----", "-----"],
                              ["CS", "-----", "-----"],
                              ["DS", "-----", "-----"]]
            window["-table2-"].update(values=table_content2, row_colors=((0, color), (4, color), (8, color)))
        # second year timing 7TH period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(15,10) and t_to_m(cur_t[0],cur_t[1])<t_to_m(15,50):
            p = "7TH"
            i=7
            window["timestamp"].update("[15:10-15:50]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", do.iot2[w1][i], do.teach_iot2[do.iot2[w1][i]]],
                             ["CS", do.cs2[w1][i], do.teach_cs2[do.cs2[w1][i]]],
                             ["DS", do.ds2[w1][i], do.teach_ds2[do.ds2[w1][i]]]
                             ]
            window["-table-"].update(values=table_content,row_colors=((0,color),(4,color),(8,color)))
        # second year timing 7TH period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(14,20) and t_to_m(cur_t[0],cur_t[1])<t_to_m(15,10):
            p = "6TH"
            i=6
            window["timestamp"].update("[14:20-15:10]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", do.iot2[w1][i], do.teach_iot2[do.iot2[w1][i]]],
                             ["CS", do.cs2[w1][i], do.teach_cs2[do.cs2[w1][i]]],
                             ["DS", do.ds2[w1][i], do.teach_ds2[do.ds2[w1][i]]]
                             ]
            window["-table-"].update(values=table_content, row_colors=((0, color), (4, color),(8,color)))

        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(14,30) and t_to_m(cur_t[0],cur_t[1])<t_to_m(15,30):
            p2 = "6 TH"
            i=6
            window["timestamp2"].update("[14:30-15:30]")
            table_content2 = [
                             ["", "3rd YEAR"],
                             ["IOT", do.iot3[w1][i], do.teach_iot3[do.iot3[w1][i]]],
                             ["CS", do.cs3[w1][i], do.teach_cs3[do.cs3[w1][i]]],
                             ["DS", do.ds3[w1][i], do.teach_ds3[do.ds3[w1][i]]],
                             ["", "4th YEAR"],
                             ["IOT", do.iot4[w1][i], do.teach_iot4[do.iot4[w1][i]]],
                             ["CS", do.cs4[w1][i], do.teach_cs4[do.cs4[w1][i]]],
                             ["DS", do.ds4[w1][i], do.teach_ds4[do.ds4[w1][i]]]
                             ]
            window["-table2-"].update(values=table_content2, row_colors=((0, color), (4, color),(8,color)))

        # second year timing 7TH period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(13,30) and t_to_m(cur_t[0],cur_t[1])<t_to_m(14,20):
            p = "5TH"
            i=5
            window["timestamp"].update("[13:30-14:20]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", do.iot2[w1][i], do.teach_iot2[do.iot2[w1][i]]],
                             ["CS", do.cs2[w1][i], do.teach_cs2[do.cs2[w1][i]]],
                             ["DS", do.ds2[w1][i], do.teach_ds2[do.ds2[w1][i]]],
                             ["", "3rd YEAR"],
                             ["IOT", do.iot3[w1][i], do.teach_iot3[do.iot3[w1][i]]],
                             ["CS", do.cs3[w1][i], do.teach_cs3[do.cs3[w1][i]]],
                             ["DS", do.ds3[w1][i], do.teach_ds3[do.ds3[w1][i]]],
                             ["", "4th YEAR"],
                             ["IOT", do.iot4[w1][i], do.teach_iot4[do.iot4[w1][i]]],
                             ["CS", do.cs4[w1][i], do.teach_cs4[do.cs4[w1][i]]],
                             ["DS", do.ds4[w1][i], do.teach_ds4[do.ds4[w1][i]]]]
            window["-table-"].update(values=table_content, row_colors=((0, color), (4, color),(8,color)))

        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(13,30) and t_to_m(cur_t[0],cur_t[1])<t_to_m(14,30):
            p2 = "5 TH"
            i=5
            window["timestamp2"].update("[13:30-14:30]")
            table_content2 = [
                             ["", "3rd YEAR"],
                             ["IOT", do.iot3[w1][i], do.teach_iot3[do.iot3[w1][i]]],
                             ["CS", do.cs3[w1][i], do.teach_cs3[do.cs3[w1][i]]],
                             ["DS", do.ds3[w1][i], do.teach_ds3[do.ds3[w1][i]]],
                             ["", "4th YEAR"],
                             ["IOT", do.iot4[w1][i], do.teach_iot4[do.iot4[w1][i]]],
                             ["CS", do.cs4[w1][i], do.teach_cs4[do.cs4[w1][i]]],
                             ["DS", do.ds4[w1][i], do.teach_ds4[do.ds4[w1][i]]]
                             ]
            window["-table2-"].update(values=table_content2, row_colors=((0, color), (4, color),(8,color)))
        # second year timing 7TH period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(12,50) and t_to_m(cur_t[0],cur_t[1])<t_to_m(13,30):
            p = "LUNCH"
            p2= "LUNCH"
            window["timestamp"].update("[12:50-13:30]")
            window["timestamp2"].update("[12:50-13:30]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", "-----", "-----"],
                             ["CS", "-----", "-----"],
                             ["DS", "-----", "-----"]]
            table_content2=[["", "3rd YEAR"],
                             ["IOT", "-----", "-----"],
                             ["CS", "-----", "-----"],
                             ["DS", "-----","-----"],
                             ["", "4th YEAR"],
                             ["IOT", "-----", "-----"],
                             ["CS", "-----", "-----"],
                             ["DS", "-----", "-----"]
                             ]
            window["-table-"].update(values=table_content, row_colors=((0, color), (4, color),(8,color)))
            window["-table2-"].update(values=table_content2, row_colors=((0, color), (4, color), (8, color)))
        # second year timing 7TH period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(12,00) and t_to_m(cur_t[0],cur_t[1])<t_to_m(12,50):
            p="4 TH"
            p2="4 TH"
            i = 3
            window["timestamp"].update("[12:00-12:50]")
            window["timestamp2"].update("[12:00-12:50]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", do.iot2[w1][i], do.teach_iot2[do.iot2[w1][i]]],
                             ["CS", do.cs2[w1][i], do.teach_cs2[do.cs2[w1][i]]],
                             ["DS", do.ds2[w1][i], do.teach_ds2[do.ds2[w1][i]]]]
            table_content2 = [["", "3rd YEAR"],
                              ["IOT", do.iot3[w1][i], do.teach_iot3[do.iot3[w1][i]]],
                                ["CS", do.cs3[w1][i], do.teach_cs3[do.cs3[w1][i]]],
                                ["DS", do.ds3[w1][i], do.teach_ds3[do.ds3[w1][i]]],
                                ["", "4th YEAR"],
                                ["IOT", do.iot4[w1][i], do.teach_iot4[do.iot4[w1][i]]],
                                ["CS", do.cs4[w1][i], do.teach_cs4[do.cs4[w1][i]]],
                                ["DS", do.ds4[w1][i], do.teach_ds4[do.ds4[w1][i]]]
                            ]
            window["-table2-"].update(values=table_content2, row_colors=((0, color), (4, color), (8, color)))
            window["-table-"].update(values=table_content, row_colors=((0, color), (4, color),(8,color)))
        # second year timing 7TH period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(11,10) and t_to_m(cur_t[0],cur_t[1])<t_to_m(12,00):
            p="3 RD"
            p2="3 RD"
            i = 2
            window["timestamp"].update("[11:10-12:00]")
            window["timestamp2"].update("[11:10-12:00]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", do.iot2[w1][i], do.teach_iot2[do.iot2[w1][i]]],
                             ["CS", do.cs2[w1][i], do.teach_cs2[do.cs2[w1][i]]],
                             ["DS", do.ds2[w1][i], do.teach_ds2[do.ds2[w1][i]]]]
            table_content2 = [
                ["", "3rd YEAR"],
                ["IOT", do.iot3[w1][i], do.teach_iot3[do.iot3[w1][i]]],
                ["CS", do.cs3[w1][i], do.teach_cs3[do.cs3[w1][i]]],
                ["DS", do.ds3[w1][i], do.teach_ds3[do.ds3[w1][i]]],
                ["", "4th YEAR"],
                ["IOT", do.iot4[w1][i], do.teach_iot4[do.iot4[w1][i]]],
                ["CS", do.cs4[w1][i], do.teach_cs4[do.cs4[w1][i]]],
                ["DS", do.ds4[w1][i], do.teach_ds4[do.ds4[w1][i]]]
            ]
            window["-table2-"].update(values=table_content2, row_colors=((0, color), (4, color), (8, color)))
            window["-table-"].update(values=table_content, row_colors=((0, color), (4, color),(8,color)))
        # second year timing 7TH period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(10,20) and t_to_m(cur_t[0],cur_t[1])<t_to_m(11,10):
            p="2 ND"
            p2="2 ND"
            i = 1
            window["timestamp"].update("[10:20-11:10]")
            window["timestamp2"].update("[10:20-11:10]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", do.iot2[w1][i], do.teach_iot2[do.iot2[w1][i]]],
                             ["CS", do.cs2[w1][i], do.teach_cs2[do.cs2[w1][i]]],
                             ["DS", do.ds2[w1][i], do.teach_ds2[do.ds2[w1][i]]]]
            table_content2 = [
                ["", "3rd YEAR"],
                ["IOT", do.iot3[w1][i], do.teach_iot3[do.iot3[w1][i]]],
                ["CS", do.cs3[w1][i], do.teach_cs3[do.cs3[w1][i]]],
                ["DS", do.ds3[w1][i], do.teach_ds3[do.ds3[w1][i]]],
                ["", "4th YEAR"],
                ["IOT", do.iot4[w1][i], do.teach_iot4[do.iot4[w1][i]]],
                ["CS", do.cs4[w1][i], do.teach_cs4[do.cs4[w1][i]]],
                ["DS", do.ds4[w1][i], do.teach_ds4[do.ds4[w1][i]]]
            ]
            window["-table2-"].update(values=table_content2, row_colors=((0, color), (4, color), (8, color)))
            window["-table-"].update(values=table_content, row_colors=((0, color), (4, color),(8,color)))
        # second year timing 7TH period
        if t_to_m(cur_t[0],cur_t[1])>=t_to_m(9,30) and t_to_m(cur_t[0],cur_t[1])<t_to_m(10,20):
            p="1 ST"
            p2="1 ST"
            i=0
            window["timestamp"].update("[9:30-10:20]")
            window["timestamp2"].update("[9:30-10:20]")
            table_content = [["", "2nd YEAR"],
                             ["IOT", do.iot2[w1][i], do.teach_iot2[do.iot2[w1][i]]],
                             ["CS", do.cs2[w1][i], do.teach_cs2[do.cs2[w1][i]]],
                             ["DS", do.ds2[w1][i], do.teach_ds2[do.ds2[w1][i]]]]
            table_content2 = [
                ["", "3rd YEAR"],
                ["IOT", do.iot3[w1][i], do.teach_iot3[do.iot3[w1][i]]],
                ["CS", do.cs3[w1][i], do.teach_cs3[do.cs3[w1][i]]],
                ["DS", do.ds3[w1][i], do.teach_ds3[do.ds3[w1][i]]],
                ["", "4th YEAR"],
                ["IOT", do.iot4[w1][i], do.teach_iot4[do.iot4[w1][i]]],
                ["CS", do.cs4[w1][i], do.teach_cs4[do.cs4[w1][i]]],
                ["DS", do.ds4[w1][i], do.teach_ds4[do.ds4[w1][i]]]
            ]
            window["-table2-"].update(values=table_content2, row_colors=((0, color), (4, color), (8, color)))
            window["-table-"].update(values=table_content, row_colors=((0, color), (4, color),(8,color)))

        window['period'].update(p)
        window['period2'].update(p2)

      window['period'].update(p)
      window['period2'].update(p2)

    window['period'].update(p)
    window['period2'].update(p2)

window.close()