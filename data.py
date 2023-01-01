import pandas as pd


#############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#############################

iot4=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="IOT4")
tiot4=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_IOT4")
teach_iot4={}
i=0
while i<=11:
    teach_iot4[tiot4["SUB"][i]]=tiot4["TEACHER"][i]
    i += 1
##############################################4

cs4=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="CS4")
tcs4=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_CS4")
teach_cs4={}
i=0
while i<=11:
    teach_cs4[tcs4["SUB"][i]]=tcs4["TEACHER"][i]
    i += 1

######################################
###############


ds4=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="DS4")
tds4=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_DS4")
teach_ds4={}
i=0
while i<=11:
    teach_ds4[tds4["SUB"][i]]=tds4["TEACHER"][i]
    i += 1
##################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################

iot3=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="IOT3")
tiot3=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_IOT3")
teach_iot3={}
i=0
while i<=11:
    teach_iot3[tiot3["SUB"][i]]=tiot3["TEACHER"][i]
    i += 1
##############################################


cs3=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="CS3")
tcs3=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_CS3")
teach_cs3={}
i=0
while i<=11:
    teach_cs3[tcs3["SUB"][i]]=tcs3["TEACHER"][i]
    i += 1

######################################
###############


ds3=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="DS3")
tds3=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_DS3")
teach_ds3={}
i=0
while i<=11:
    teach_ds3[tds3["SUB"][i]]=tds3["TEACHER"][i]
    i += 1
##################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################

iot2=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="IOT2")
tiot2=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_IOT2")
teach_iot2={}
i=0
while i<=11:
    teach_iot2[tiot2["SUB"][i]]=tiot2["TEACHER"][i]
    i += 1
##############################################


cs2=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="CS2")
tcs2=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_CS2")
teach_cs2={}
i=0
while i<=11:
    teach_cs2[tcs2["SUB"][i]]=tcs2["TEACHER"][i]
    i += 1

######################################
###############

ds2=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="DS2")
tds2=pd.read_excel("TIMETABLE_3.xlsx",sheet_name="TEACH_DS2")
teach_ds2={}
i=0
while i<=11:
    teach_ds2[tds2["SUB"][i]]=tds2["TEACHER"][i]
    i += 1
