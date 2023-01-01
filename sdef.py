from playsound import playsound
import pyttsx3
e = pyttsx3.init()
v=e.getProperty('voices')
e.setProperty('voice',v[0].id)
e.setProperty('rate',100)
def m_first(n_p1=[]):
    if n_p1:
        return
    # playsound('sample.mp3')
    e.say("First period")

    e.runAndWait()
    n_p1.append(1)
def m_second(n_p2=[]):
    if n_p2:
        return
    # playsound('sample.mp3')
    e.say("Second period")
    e.runAndWait()
    n_p2.append(1)
def m_third(n_p3=[]):
    if n_p3:
        return
    # playsound('sample.mp3')
    e.say("Third period")
    e.runAndWait()
    n_p3.append(1)
def m_fourth(n_p4=[]):
    if n_p4:
        return
    # playsound('sample.mp3')
    e.say("Fourth period")
    e.runAndWait()
    n_p4.append(1)
def m_lunch(n_pl=[]):
    if n_pl:
        return
    # playsound('sample.mp3')
    e.say("Lunch period")
    e.runAndWait()
    n_pl.append(1)
def m_fifth(n_p5=[]):
    if n_p5:
        return
    # playsound('sample.mp3')
    e.say("Fifth period")
    e.runAndWait()
    n_p5.append(1)
def m_sixth(n_p6=[]):
    if n_p6:
        return
    # playsound('sample.mp3')
    e.say("Sixth period")
    e.runAndWait()
    n_p6.append(1)
def m_seventh(n_p7=[]):
    if n_p7:
        return
    # playsound('sample.mp3')
    e.say("Seventh period")
    e.runAndWait()
    n_p7.append(1)
def m_end(n_pe=[]):
    if n_pe:
        return
    # playsound('sample.mp3')
    e.say("end")
    e.runAndWait()
    n_pe.append(1)

