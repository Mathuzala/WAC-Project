from tkinter import *
import pandas as pd
from PIL import ImageTk, Image

root = Tk()
root.title("Capital Markets - Finance Grid WAC Calculator") 
root.geometry("800x800")

global df

# Bringing in the Data Through a Pandas Dataframe
df = pd.read_excel("C:\\Users\\mhorv656\\Documents\\Financing Grid v4.xlsx", "Data",
engine = 'openpyxl', usecols = ['ORIG_AMT', 'LOAN_RATE', 'SPECIAL_PROJ_CD', 'GROSS_POINT', 'Down Pmt %'])


###############################################################################################################################################################################


# Setting some of the columns variable types and creating the Rate Weight column for the WAC calculation
df['ORIG_AMT'] = df['ORIG_AMT'].fillna(0).astype(int)
df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
df['SPECIAL_PROJ_CD'] = df['SPECIAL_PROJ_CD'].fillna(0).astype(int)

# Creating a Points Category Column
def Points_Cat(df): 
    if (df['GROSS_POINT']) >= 1000 and (df['GROSS_POINT']) <= 1750:
        return "1000 - 1750"
    elif (df['GROSS_POINT']) >= 2000 and (df['GROSS_POINT']) <= 2750:
        return "2000 - 2750"
    elif (df['GROSS_POINT']) >= 3000 and (df['GROSS_POINT']) <= 3750:
        return "3000 - 3750"
    elif (df['GROSS_POINT']) >= 4000:
        return "4000 +"
    else:
        return ''

# Creating Concated Column for the Points Category
df['Points_Category'] = df.apply(Points_Cat, axis = 1)
df["Concat"] = df['Points_Category'].astype(str) + df["SPECIAL_PROJ_CD"].astype(str)

# Creating a Purchase Category Column
def Purchase_Cat(df): 
    if (df['ORIG_AMT']) >= 7000 and (df['ORIG_AMT']) <= 25359:
        return "7000 - 25359"
    elif (df['ORIG_AMT']) >= 25360 and (df['ORIG_AMT']) <= 35939:
        return "25360 - 35939"
    elif (df['ORIG_AMT']) >= 35940 and (df['ORIG_AMT']) <= 45039:
        return "35940 - 45039"
    elif (df['ORIG_AMT']) >= 45040:
        return "45040 +"
    else:
        return ''

# Creating a Concated Column for the Purchase Category
df['Purchase_Category'] = df.apply(Purchase_Cat, axis = 1)
df["Concat2"] = df['Purchase_Category'].astype(str) + df["SPECIAL_PROJ_CD"].astype(str)

# Creating This Function for 'MVC International Rates' Which Has Different Purchase Categories Than the Other Financing Programs
def Purchase_Cat2(df): 
    if (df['ORIG_AMT']) >= 7000 and (df['ORIG_AMT']) <= 21499:
        return "7000 - 21499"
    elif (df['ORIG_AMT']) >= 21500:
        return "21500 +"
    else:
        return ''

df['Purchase_Category2'] = df.apply(Purchase_Cat2, axis = 1)
df["Concat4"] = df['Purchase_Category2'].astype(str) + df["SPECIAL_PROJ_CD"].astype(str)

def Down_Payment_Cat(df):
    if (df['Down Pmt %']) < 10:
        return "0"
    if (df['Down Pmt %']) > 10 and (df['Down Pmt %']) <= 15:
        return "10 - 15"
    elif (df['Down Pmt %']) >= 16 and (df['Down Pmt %']) <= 20:
        return "15 - 20"
    elif (df['Down Pmt %']) >= 21 and (df['Down Pmt %']) <= 25:
        return "20 - 25"
    elif (df['Down Pmt %']) >= 26 and (df['Down Pmt %']) <= 30:
        return "25 - 30"
    elif (df['Down Pmt %']) >= 31 and (df['Down Pmt %']) <= 35:
        return "30 - 35"
    elif (df['Down Pmt %']) >= 36:
        return "35 +"
    else:
        return ''

df['Down_Payment_Category'] = df.apply(Down_Payment_Cat, axis = 1)
df["Concat3"] = df['Down_Payment_Category'].astype(str) + df["SPECIAL_PROJ_CD"].astype(str)

# Defining a Main Menu
my_menu = Menu(root)
root.config(menu = my_menu)

def Reset_WAC():
    global df

    df = pd.read_excel("C:\\Users\\mhorv656\\Documents\\Financing Grid v4.xlsx", "Data",
    engine = 'openpyxl', usecols = ['ORIG_AMT', 'LOAN_RATE', 'SPECIAL_PROJ_CD', 'GROSS_POINT', 'Down Pmt %'])

    df['ORIG_AMT'] = df['ORIG_AMT'].fillna(0).astype(int)
    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    df['SPECIAL_PROJ_CD'] = df['SPECIAL_PROJ_CD'].fillna(0).astype(int)

    def Points_Cat(df): 
        if (df['GROSS_POINT']) >= 1000 and (df['GROSS_POINT']) <= 1750:
            return "1000 - 1750"
        elif (df['GROSS_POINT']) >= 2000 and (df['GROSS_POINT']) <= 2750:
            return "2000 - 2750"
        elif (df['GROSS_POINT']) >= 3000 and (df['GROSS_POINT']) <= 3750:
            return "3000 - 3750"
        elif (df['GROSS_POINT']) >= 4000:
            return "4000 +"
        else:
            return ''

    df['Points_Category'] = df.apply(Points_Cat, axis = 1)
    df["Concat"] = df['Points_Category'].astype(str) + df["SPECIAL_PROJ_CD"].astype(str)

    def Purchase_Cat(df): 
        if (df['ORIG_AMT']) >= 7000 and (df['ORIG_AMT']) <= 25359:
            return "7000 - 25359"
        elif (df['ORIG_AMT']) >= 25360 and (df['ORIG_AMT']) <= 35939:
            return "25360 - 35939"
        elif (df['ORIG_AMT']) >= 35940 and (df['ORIG_AMT']) <= 45039:
            return "35940 - 45039"
        elif (df['ORIG_AMT']) >= 45040:
            return "45040 +"
        else:
            return ''

    df['Purchase_Category'] = df.apply(Purchase_Cat, axis = 1)
    df["Concat2"] = df['Purchase_Category'].astype(str) + df["SPECIAL_PROJ_CD"].astype(str)

    def Down_Payment_Cat(df):
        if (df['Down Pmt %']) < 10:
            return "0"
        if (df['Down Pmt %']) > 10 and (df['Down Pmt %']) <= 15:
            return "10 - 15"
        elif (df['Down Pmt %']) >= 16 and (df['Down Pmt %']) <= 20:
            return "15 - 20"
        elif (df['Down Pmt %']) >= 21 and (df['Down Pmt %']) <= 25:
            return "20 - 25"
        elif (df['Down Pmt %']) >= 26 and (df['Down Pmt %']) <= 30:
            return "25 - 30"
        elif (df['Down Pmt %']) >= 31 and (df['Down Pmt %']) <= 35:
            return "30 - 35"
        elif (df['Down Pmt %']) >= 36:
            return "35 +"
        else:
            return ''

    df['Down_Payment_Category'] = df.apply(Down_Payment_Cat, axis = 1)
    df["Concat3"] = df['Down_Payment_Category'].astype(str) + df["SPECIAL_PROJ_CD"].astype(str)


###############################################################################################################################################################################


# Codes 
def c3231_code():
    hide_menu_frames()
    c3231_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3231_button2 = Button(c3231_frame, text = "Previous Page", command = second_home)
    c3231_button2.pack(pady = 10)

    # Creating Input Box
    global c3231_input
    c3231_input = Entry(c3231_frame)
    c3231_input.pack(pady = 5)

    # Creating Label
    global c3231_label
    c3231_label = Label(c3231_frame, text = "Enter Rate Above for 3231")
    c3231_label.pack(pady = 5)

    # Creating Second Input Box
    global c3231_input2
    c3231_input2 = Entry(c3231_frame)
    c3231_input2.pack(pady = 5)

    # Creating Second Label
    global c3231_label2
    c3231_label2 = Label(c3231_frame, text = "Choose from Product Code List Below")
    c3231_label3 = Label(c3231_frame, text = "1,000 - 1,750") 
    c3231_label4 =Label(c3231_frame, text = "2,000 - 2,750") 
    c3231_label5 =Label(c3231_frame, text = "3,000 - 3,750") 
    c3231_label6 =Label(c3231_frame, text = "4,000 +")
    c3231_label2.pack(pady = 5)
    c3231_label3.pack(pady = 5)
    c3231_label4.pack(pady = 5)
    c3231_label5.pack(pady = 5)
    c3231_label6.pack(pady = 5)

    # Creating Answer Button
    c3231_button = Button(c3231_frame, text = "Calculate WAC", command = c3231_wac)
    c3231_button.pack(pady = 5)

def c3231_wac():
    concat_var = c3231_input2.get() + "3231"
    df.loc[df['Concat'] == concat_var, 'LOAN_RATE'] = float(c3231_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3231_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3231_input.delete(0, 'end')
    c3231_input2.delete(0, 'end')

def c3239_code():
    hide_menu_frames()
    c3239_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3239_button2 = Button(c3239_frame, text = "Previous Page", command = second_home)
    c3239_button2.pack(pady = 10)

    # Creating Input Box
    global c3239_input
    c3239_input = Entry(c3239_frame)
    c3239_input.pack(pady = 5)

    # Creating Label
    global c3239_label
    c3239_label = Label(c3239_frame, text = "Enter Rate Above for 3239")
    c3239_label.pack(pady = 5)

    # Creating Second Input Box
    global c3239_input2
    c3239_input2 = Entry(c3239_frame)
    c3239_input2.pack(pady = 5)

    # Creating Second Label
    global c3239_label2
    c3239_label2 = Label(c3239_frame, text = "Choose from Product Code List Below")
    c3239_label3 = Label(c3239_frame, text = "1,000 - 1,750") 
    c3239_label4 =Label(c3239_frame, text = "2,000 - 2,750") 
    c3239_label5 =Label(c3239_frame, text = "3,000 - 3,750") 
    c3239_label6 =Label(c3239_frame, text = "4,000 +")
    c3239_label2.pack(pady = 5)
    c3239_label3.pack(pady = 5)
    c3239_label4.pack(pady = 5)
    c3239_label5.pack(pady = 5)
    c3239_label6.pack(pady = 5)

    # Creating Answer Button
    c3239_button = Button(c3239_frame, text = "Calculate WAC", command = c3239_wac)
    c3239_button.pack(pady = 5)

def c3239_wac():
    concat_var = c3239_input2.get() + "3239"
    df.loc[df['Concat'] == concat_var, 'LOAN_RATE'] = float(c3239_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3239_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3239_input.delete(0, 'end')
    c3239_input2.delete(0, 'end')

def c3232_code():
    hide_menu_frames()
    c3232_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3232_button2 = Button(c3232_frame, text = "Previous Page", command = second_home)
    c3232_button2.pack(pady = 10)

    # Creating Input Box
    global c3232_input
    c3232_input = Entry(c3232_frame)
    c3232_input.pack(pady = 5)

    # Creating Label
    global c3232_label
    c3232_label = Label(c3232_frame, text = "Enter Rate Above for 3232")
    c3232_label.pack(pady = 5)

    # Creating Second Input Box
    global c3232_input2
    c3232_input2 = Entry(c3232_frame)
    c3232_input2.pack(pady = 5)

    # Creating Second Label
    global c3232_label2
    c3232_label2 = Label(c3232_frame, text = "Choose from Product Code List Below")
    c3232_label3 = Label(c3232_frame, text = "1,000 - 1,750") 
    c3232_label4 =Label(c3232_frame, text = "2,000 - 2,750") 
    c3232_label5 =Label(c3232_frame, text = "3,000 - 3,750") 
    c3232_label6 =Label(c3232_frame, text = "4,000 +")
    c3232_label2.pack(pady = 5)
    c3232_label3.pack(pady = 5)
    c3232_label4.pack(pady = 5)
    c3232_label5.pack(pady = 5)
    c3232_label6.pack(pady = 5)

    # Creating Answer Button
    c3232_button = Button(c3232_frame, text = "Calculate WAC", command = c3232_wac)
    c3232_button.pack(pady = 5)

def c3232_wac():
    concat_var = c3232_input2.get() + "3232"
    df.loc[df['Concat'] == concat_var, 'LOAN_RATE'] = float(c3232_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3232_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3232_input.delete(0, 'end')
    c3232_input2.delete(0, 'end')

def c3247_code():
    hide_menu_frames()
    c3247_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3247_button2 = Button(c3247_frame, text = "Previous Page", command = second_home)
    c3247_button2.pack(pady = 10)

    # Creating Input Box
    global c3247_input
    c3247_input = Entry(c3247_frame)
    c3247_input.pack(pady = 5)

    # Creating Label
    global c3247_label
    c3247_label = Label(c3247_frame, text = "Enter Rate Above for 3247")
    c3247_label.pack(pady = 5)

    # Creating Second Input Box
    global c3247_input2
    c3247_input2 = Entry(c3247_frame)
    c3247_input2.pack(pady = 5)

    # Creating Second Label
    global c3247_label2
    c3247_label2 = Label(c3247_frame, text = "Choose from Product Code List Below")
    c3247_label3 = Label(c3247_frame, text = "1,000 - 1,750") 
    c3247_label4 =Label(c3247_frame, text = "2,000 - 2,750") 
    c3247_label5 =Label(c3247_frame, text = "3,000 - 3,750") 
    c3247_label6 =Label(c3247_frame, text = "4,000 +")
    c3247_label2.pack(pady = 5)
    c3247_label3.pack(pady = 5)
    c3247_label4.pack(pady = 5)
    c3247_label5.pack(pady = 5)
    c3247_label6.pack(pady = 5)

    # Creating Answer Button
    c3247_button = Button(c3247_frame, text = "Calculate WAC", command = c3247_wac)
    c3247_button.pack(pady = 5)

def c3247_wac():
    concat_var = c3247_input2.get() + "3247"
    df.loc[df['Concat'] == concat_var, 'LOAN_RATE'] = float(c3247_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3247_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3247_input.delete(0, 'end')
    c3247_input2.delete(0, 'end')

def c3233_code():
    hide_menu_frames()
    c3233_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3233_button2 = Button(c3233_frame, text = "Previous Page", command = third_home)
    c3233_button2.pack(pady = 10)

    # Creating Input Box
    global c3233_input
    c3233_input = Entry(c3233_frame)
    c3233_input.pack(pady = 5)

    # Creating Label
    global c3233_label
    c3233_label = Label(c3233_frame, text = "Enter Rate Above for 3233")
    c3233_label.pack(pady = 5)

    # Creating Second Input Box
    global c3233_input2
    c3233_input2 = Entry(c3233_frame)
    c3233_input2.pack(pady = 5)

    # Creating Second Label
    global c3233_label2
    c3233_label2 = Label(c3233_frame, text = "Choose from Purchase Amount List Below")
    c3233_label3 = Label(c3233_frame, text = "7,000 - 25,359") 
    c3233_label4 =Label(c3233_frame, text = "25,360 - 35,939") 
    c3233_label5 =Label(c3233_frame, text = "35,940 - 45,039") 
    c3233_label6 =Label(c3233_frame, text = "45,040 +")
    c3233_label2.pack(pady = 5)
    c3233_label3.pack(pady = 5)
    c3233_label4.pack(pady = 5)
    c3233_label5.pack(pady = 5)
    c3233_label6.pack(pady = 5)

    # Creating Answer Button
    c3233_button = Button(c3233_frame, text = "Calculate WAC", command = c3233_wac)
    c3233_button.pack(pady = 5)

def c3233_wac():
    concat_var = c3233_input2.get() + "3233"
    df.loc[df['Concat2'] == concat_var, 'LOAN_RATE'] = float(c3233_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3233_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3233_input.delete(0, 'end')
    c3233_input2.delete(0, 'end')

def c3240_code():
    hide_menu_frames()
    c3240_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3240_button2 = Button(c3240_frame, text = "Previous Page", command = third_home)
    c3240_button2.pack(pady = 10)

    # Creating Input Box
    global c3240_input
    c3240_input = Entry(c3240_frame)
    c3240_input.pack(pady = 5)

    # Creating Label
    global c3240_label
    c3240_label = Label(c3240_frame, text = "Enter Rate Above for 3240")
    c3240_label.pack(pady = 5)

    # Creating Second Input Box
    global c3240_input2
    c3240_input2 = Entry(c3240_frame)
    c3240_input2.pack(pady = 5)

    # Creating Second Label
    global c3240_label2
    c3240_label2 = Label(c3240_frame, text = "Choose from Purchase Amount List Below")
    c3240_label3 = Label(c3240_frame, text = "7,000 - 25,359") 
    c3240_label4 =Label(c3240_frame, text = "25,360 - 35,939") 
    c3240_label5 =Label(c3240_frame, text = "35,940 - 45,039") 
    c3240_label6 =Label(c3240_frame, text = "45,040 +")
    c3240_label2.pack(pady = 5)
    c3240_label3.pack(pady = 5)
    c3240_label4.pack(pady = 5)
    c3240_label5.pack(pady = 5)
    c3240_label6.pack(pady = 5)

    # Creating Answer Button
    c3240_button = Button(c3240_frame, text = "Calculate WAC", command = c3240_wac)
    c3240_button.pack(pady = 5)

def c3240_wac():
    concat_var2 = c3240_input2.get() + "3240"
    df.loc[df['Concat2'] == concat_var2, 'LOAN_RATE'] = float(c3240_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3240_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    #c3240_label = Label(c3240_frame, text = concat_var, font = ("Helvetica", 14))
    #c3240_label.pack(pady = 5)

    # Clearing the answer box
    c3240_input.delete(0, 'end')
    c3240_input2.delete(0, 'end')

def c3214_code():
    hide_menu_frames()
    c3214_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3214_button2 = Button(c3214_frame, text = "Previous Page", command = fourth_home)
    c3214_button2.pack(pady = 10)

    # Creating Input Box
    global c3214_input
    c3214_input = Entry(c3214_frame)
    c3214_input.pack(pady = 5)

    # Creating Label
    global c3214_label
    c3214_label = Label(c3214_frame, text = "Enter Rate Above for 3214")
    c3214_label.pack(pady = 5)

    # Creating Second Input Box
    global c3214_input2
    c3214_input2 = Entry(c3214_frame)
    c3214_input2.pack(pady = 5)

    # Creating Second Label
    global c3214_label2
    c3214_label2 = Label(c3214_frame, text = "Choose from Product Code List Below")
    c3214_label3 = Label(c3214_frame, text = "1,000 - 1,750") 
    c3214_label4 =Label(c3214_frame, text = "2,000 - 2,750") 
    c3214_label5 =Label(c3214_frame, text = "3,000 +") 
    c3214_label2.pack(pady = 5)
    c3214_label3.pack(pady = 5)
    c3214_label4.pack(pady = 5)
    c3214_label5.pack(pady = 5)

    # Creating Answer Button
    c3214_button = Button(c3214_frame, text = "Calculate WAC", command = c3214_wac)
    c3214_button.pack(pady = 5)

def c3214_wac():
    concat_var = c3214_input2.get() + "3214"
    df.loc[df['Concat'] == concat_var, 'LOAN_RATE'] = float(c3214_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3214_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3214_input.delete(0, 'end')
    c3214_input2.delete(0, 'end')

def c3241_code():
    hide_menu_frames()
    c3241_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3241_button2 = Button(c3241_frame, text = "Previous Page", command = fourth_home)
    c3241_button2.pack(pady = 10)

    # Creating Input Box
    global c3241_input
    c3241_input = Entry(c3241_frame)
    c3241_input.pack(pady = 5)

    # Creating Label
    global c3241_label
    c3241_label = Label(c3241_frame, text = "Enter Rate Above for 3241")
    c3241_label.pack(pady = 5)

    # Creating Second Input Box
    global c3241_input2
    c3241_input2 = Entry(c3241_frame)
    c3241_input2.pack(pady = 5)

    # Creating Second Label
    global c3241_label2
    c3241_label2 = Label(c3241_frame, text = "Choose from Product Code List Below")
    c3241_label3 = Label(c3241_frame, text = "1,000 - 1,750") 
    c3241_label4 =Label(c3241_frame, text = "2,000 - 2,750") 
    c3241_label5 =Label(c3241_frame, text = "3,000 +") 
    c3241_label2.pack(pady = 5)
    c3241_label3.pack(pady = 5)
    c3241_label4.pack(pady = 5)
    c3241_label5.pack(pady = 5)

    # Creating Answer Button
    c3241_button = Button(c3241_frame, text = "Calculate WAC", command = c3241_wac)
    c3241_button.pack(pady = 5)

def c3241_wac():
    concat_var = c3241_input2.get() + "3241"
    df.loc[df['Concat'] == concat_var, 'LOAN_RATE'] = float(c3241_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3241_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3241_input.delete(0, 'end')
    c3241_input2.delete(0, 'end')

def c3216_code():
    hide_menu_frames()
    c3216_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3216_button2 = Button(c3216_frame, text = "Previous Page", command = fourth_home)
    c3216_button2.pack(pady = 10)

    # Creating Input Box
    global c3216_input
    c3216_input = Entry(c3216_frame)
    c3216_input.pack(pady = 5)

    # Creating Label
    global c3216_label
    c3216_label = Label(c3216_frame, text = "Enter Rate Above for 3216")
    c3216_label.pack(pady = 5)

    # Creating Second Input Box
    global c3216_input2
    c3216_input2 = Entry(c3216_frame)
    c3216_input2.pack(pady = 5)

    # Creating Second Label
    global c3216_label2
    c3216_label2 = Label(c3216_frame, text = "Choose from Product Code List Below")
    c3216_label3 = Label(c3216_frame, text = "1,000 - 1,750") 
    c3216_label4 =Label(c3216_frame, text = "2,000 - 2,750") 
    c3216_label5 =Label(c3216_frame, text = "3,000 +") 
    c3216_label2.pack(pady = 5)
    c3216_label3.pack(pady = 5)
    c3216_label4.pack(pady = 5)
    c3216_label5.pack(pady = 5)

    # Creating Answer Button
    c3216_button = Button(c3216_frame, text = "Calculate WAC", command = c3216_wac)
    c3216_button.pack(pady = 5)

def c3216_wac():
    concat_var = c3216_input2.get() + "3216"
    df.loc[df['Concat'] == concat_var, 'LOAN_RATE'] = float(c3216_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3216_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3216_input.delete(0, 'end')
    c3216_input2.delete(0, 'end')

def c3248_code():
    hide_menu_frames()
    c3248_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3248_button2 = Button(c3248_frame, text = "Previous Page", command = fourth_home)
    c3248_button2.pack(pady = 10)

    # Creating Input Box
    global c3248_input
    c3248_input = Entry(c3248_frame)
    c3248_input.pack(pady = 5)

    # Creating Label
    global c3248_label
    c3248_label = Label(c3248_frame, text = "Enter Rate Above for 3248")
    c3248_label.pack(pady = 5)

    # Creating Second Input Box
    global c3248_input2
    c3248_input2 = Entry(c3248_frame)
    c3248_input2.pack(pady = 5)

    # Creating Second Label
    global c3248_label2
    c3248_label2 = Label(c3248_frame, text = "Choose from Product Code List Below")
    c3248_label3 = Label(c3248_frame, text = "1,000 - 1,750") 
    c3248_label4 =Label(c3248_frame, text = "2,000 - 2,750") 
    c3248_label5 =Label(c3248_frame, text = "3,000 - 3,750") 
    c3248_label6 =Label(c3248_frame, text = "4,000 +")
    c3248_label2.pack(pady = 5)
    c3248_label3.pack(pady = 5)
    c3248_label4.pack(pady = 5)
    c3248_label5.pack(pady = 5)
    c3248_label6.pack(pady = 5)

    # Creating Answer Button
    c3248_button = Button(c3248_frame, text = "Calculate WAC", command = c3248_wac)
    c3248_button.pack(pady = 5)

def c3248_wac():
    concat_var = c3248_input2.get() + "3248"
    df.loc[df['Concat'] == concat_var, 'LOAN_RATE'] = float(c3248_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3248_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3248_input.delete(0, 'end')
    c3248_input2.delete(0, 'end')

def c3237_code():
    hide_menu_frames()
    c3237_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3237_button2 = Button(c3237_frame, text = "Previous Page", command = fifth_home)
    c3237_button2.pack(pady = 10)

    # Creating Input Box
    global c3237_input
    c3237_input = Entry(c3237_frame)
    c3237_input.pack(pady = 5)

    # Creating Label
    global c3237_label
    c3237_label = Label(c3237_frame, text = "Enter Rate Above for 3237")
    c3237_label.pack(pady = 5)

    # Creating Second Input Box
    global c3237_input2
    c3237_input2 = Entry(c3237_frame)
    c3237_input2.pack(pady = 5)

    # Creating Second Label
    global c3237_label2
    c3237_label2 = Label(c3237_frame, text = "Choose from Purchase Amount List Below")
    c3237_label3 = Label(c3237_frame, text = "7,000 - 25,359") 
    c3237_label4 =Label(c3237_frame, text = "25,360 - 35,939") 
    c3237_label6 =Label(c3237_frame, text = "35,940 +")
    c3237_label2.pack(pady = 5)
    c3237_label3.pack(pady = 5)
    c3237_label4.pack(pady = 5)
    c3237_label6.pack(pady = 5)

    # Creating Answer Button
    c3237_button = Button(c3237_frame, text = "Calculate WAC", command = c3237_wac)
    c3237_button.pack(pady = 5)

def c3237_wac():
    concat_var2 = c3237_input2.get() + "3237"
    df.loc[df['Concat2'] == concat_var2, 'LOAN_RATE'] = float(c3237_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3237_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3237_input.delete(0, 'end')
    c3237_input2.delete(0, 'end')

def c3242_code():
    hide_menu_frames()
    c3242_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3242_button2 = Button(c3242_frame, text = "Previous Page", command = fifth_home)
    c3242_button2.pack(pady = 10)

    # Creating Input Box
    global c3242_input
    c3242_input = Entry(c3242_frame)
    c3242_input.pack(pady = 5)

    # Creating Label
    global c3242_label
    c3242_label = Label(c3242_frame, text = "Enter Rate Above for 3242")
    c3242_label.pack(pady = 5)

    # Creating Second Input Box
    global c3242_input2
    c3242_input2 = Entry(c3242_frame)
    c3242_input2.pack(pady = 5)

    # Creating Second Label
    global c3242_label2
    c3242_label2 = Label(c3242_frame, text = "Choose from Purchase Amount List Below")
    c3242_label3 = Label(c3242_frame, text = "7,000 - 25,359") 
    c3242_label4 = Label(c3242_frame, text = "25,360 - 35,939") 
    c3242_label6 = Label(c3242_frame, text = "35,940 +")
    c3242_label2.pack(pady = 5)
    c3242_label3.pack(pady = 5)
    c3242_label4.pack(pady = 5)
    c3242_label6.pack(pady = 5)

    # Creating Answer Button
    c3242_button = Button(c3242_frame, text = "Calculate WAC", command = c3242_wac)
    c3242_button.pack(pady = 5)

def c3242_wac():
    concat_var2 = c3242_input2.get() + "3242"
    df.loc[df['Concat2'] == concat_var2, 'LOAN_RATE'] = float(c3242_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3242_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3242_input.delete(0, 'end')
    c3242_input2.delete(0, 'end')

def c3191_code():
    hide_menu_frames()
    c3191_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3191_button2 = Button(c3191_frame, text = "Previous Page", command = sixth_home)
    c3191_button2.pack(pady = 10)

    # Creating Input Box
    global c3191_input
    c3191_input = Entry(c3191_frame)
    c3191_input.pack(pady = 5)

    # Creating Label
    global c3191_label
    c3191_label = Label(c3191_frame, text = "Enter Rate Above for 3191")
    c3191_label.pack(pady = 5)

    # Creating Second Input Box
    global c3191_input2
    c3191_input2 = Entry(c3191_frame)
    c3191_input2.pack(pady = 5)

    # Creating Second Label
    global c3191_label2
    c3191_label2 = Label(c3191_frame, text = "Choose from Down Payment Amount List Below")
    c3191_label3 = Label(c3191_frame, text = "10 - 14") 
    c3191_label4 = Label(c3191_frame, text = "15 - 19")
    c3191_label5 = Label(c3191_frame, text = "20 - 24") 
    c3191_label6 = Label(c3191_frame, text = "25 - 29")   
    c3191_label7 = Label(c3191_frame, text = "30 - 34")  
    c3191_label8 = Label(c3191_frame, text = "35 +")
    c3191_label2.pack(pady = 5)
    c3191_label3.pack(pady = 5)
    c3191_label4.pack(pady = 5)
    c3191_label5.pack(pady = 5)
    c3191_label6.pack(pady = 5)
    c3191_label7.pack(pady = 5)
    c3191_label8.pack(pady = 5)

    # Creating Answer Button
    c3191_button = Button(c3191_frame, text = "Calculate WAC", command = c3191_wac)
    c3191_button.pack(pady = 5)

def c3191_wac():
    concat_var3 = c3191_input2.get() + "3191"
    df.loc[df['Concat3'] == concat_var3, 'LOAN_RATE'] = float(c3191_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3191_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3191_input.delete(0, 'end')
    c3191_input2.delete(0, 'end')

def c3186_code():
    hide_menu_frames()
    c3186_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3186_button2 = Button(c3186_frame, text = "Previous Page", command = sixth_home)
    c3186_button2.pack(pady = 10)

    # Creating Input Box
    global c3186_input
    c3186_input = Entry(c3186_frame)
    c3186_input.pack(pady = 5)

    # Creating Label
    global c3186_label
    c3186_label = Label(c3186_frame, text = "Enter Rate Above for 3186")
    c3186_label.pack(pady = 5)

    # Creating Second Input Box
    global c3186_input2
    c3186_input2 = Entry(c3186_frame)
    c3186_input2.pack(pady = 5)

    # Creating Second Label
    global c3186_label2
    c3186_label2 = Label(c3186_frame, text = "Choose from Down Payment Amount List Below")
    c3186_label3 = Label(c3186_frame, text = "10 - 14") 
    c3186_label4 = Label(c3186_frame, text = "15 - 19")
    c3186_label5 = Label(c3186_frame, text = "20 - 24") 
    c3186_label6 = Label(c3186_frame, text = "25 - 29")   
    c3186_label7 = Label(c3186_frame, text = "30 - 34")  
    c3186_label8 = Label(c3186_frame, text = "35 +")
    c3186_label2.pack(pady = 5)
    c3186_label3.pack(pady = 5)
    c3186_label4.pack(pady = 5)
    c3186_label5.pack(pady = 5)
    c3186_label6.pack(pady = 5)
    c3186_label7.pack(pady = 5)
    c3186_label8.pack(pady = 5)

    # Creating Answer Button
    c3186_button = Button(c3186_frame, text = "Calculate WAC", command = c3186_wac)
    c3186_button.pack(pady = 5)

def c3186_wac():
    concat_var3 = c3186_input2.get() + "3186"
    df.loc[df['Concat2'] == concat_var3, 'LOAN_RATE'] = float(c3186_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].s3m() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3186_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3186_input.delete(0, 'end')
    c3186_input2.delete(0, 'end')

def c3210_code():
    hide_menu_frames()
    c3210_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3210_button2 = Button(c3210_frame, text = "Previous Page", command = sixth_home)
    c3210_button2.pack(pady = 10)

    # Creating Input Box
    global c3210_input
    c3210_input = Entry(c3210_frame)
    c3210_input.pack(pady = 5)

    # Creating Label
    global c3210_label
    c3210_label = Label(c3210_frame, text = "Enter Rate Above for 3210")
    c3210_label.pack(pady = 5)

    # Creating Second Input Box
    global c3210_input2
    c3210_input2 = Entry(c3210_frame)
    c3210_input2.pack(pady = 5)

    # Creating Second Label
    global c3210_label2
    c3210_label2 = Label(c3210_frame, text = "Choose from Down Payment Amount List Below")
    c3210_label3 = Label(c3210_frame, text = "10 - 14") 
    c3210_label4 = Label(c3210_frame, text = "15 - 19")
    c3210_label5 = Label(c3210_frame, text = "20 - 24") 
    c3210_label6 = Label(c3210_frame, text = "25 - 29")   
    c3210_label7 = Label(c3210_frame, text = "30 - 34")  
    c3210_label8 = Label(c3210_frame, text = "35 +")
    c3210_label2.pack(pady = 5)
    c3210_label3.pack(pady = 5)
    c3210_label4.pack(pady = 5)
    c3210_label5.pack(pady = 5)
    c3210_label6.pack(pady = 5)
    c3210_label7.pack(pady = 5)
    c3210_label8.pack(pady = 5)

    # Creating Answer Button
    c3210_button = Button(c3210_frame, text = "Calculate WAC", command = c3210_wac)
    c3210_button.pack(pady = 5)

def c3210_wac():
    concat_var3 = c3210_input2.get() + "3210"
    df.loc[df['Concat3'] == concat_var3, 'LOAN_RATE'] = float(c3210_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3210_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3210_input.delete(0, 'end')
    c3210_input2.delete(0, 'end')

def c3211_code():
    hide_menu_frames()
    c3211_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3211_button2 = Button(c3211_frame, text = "Previous Page", command = sixth_home)
    c3211_button2.pack(pady = 10)

    # Creating Input Box
    global c3211_input
    c3211_input = Entry(c3211_frame)
    c3211_input.pack(pady = 5)

    # Creating Label
    global c3211_label
    c3211_label = Label(c3211_frame, text = "Enter Rate Above for 3211")
    c3211_label.pack(pady = 5)

    # Creating Second Input Box
    global c3211_input2
    c3211_input2 = Entry(c3211_frame)
    c3211_input2.pack(pady = 5)

    # Creating Second Label
    global c3211_label2
    c3211_label2 = Label(c3211_frame, text = "Choose from Down Payment Amount List Below")
    c3211_label3 = Label(c3211_frame, text = "10 - 14") 
    c3211_label4 = Label(c3211_frame, text = "15 - 19")
    c3211_label5 = Label(c3211_frame, text = "20 - 24") 
    c3211_label6 = Label(c3211_frame, text = "25 - 29")   
    c3211_label7 = Label(c3211_frame, text = "30 - 34")  
    c3211_label8 = Label(c3211_frame, text = "35 +")
    c3211_label2.pack(pady = 5)
    c3211_label3.pack(pady = 5)
    c3211_label4.pack(pady = 5)
    c3211_label5.pack(pady = 5)
    c3211_label6.pack(pady = 5)
    c3211_label7.pack(pady = 5)
    c3211_label8.pack(pady = 5)

    # Creating Answer Button
    c3211_button = Button(c3211_frame, text = "Calculate WAC", command = c3211_wac)
    c3211_button.pack(pady = 5)

def c3211_wac():
    concat_var3 = c3211_input2.get() + "3211"
    df.loc[df['Concat3'] == concat_var3, 'LOAN_RATE'] = float(c3211_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3211_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3211_input.delete(0, 'end')
    c3211_input2.delete(0, 'end')

def c3198_code():
    hide_menu_frames()
    c3198_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3198_button2 = Button(c3198_frame, text = "Previous Page", command = seventh_home)
    c3198_button2.pack(pady = 10)

    # Creating Input Box
    global c3198_input
    c3198_input = Entry(c3198_frame)
    c3198_input.pack(pady = 5)

    # Creating Label
    global c3198_label
    c3198_label = Label(c3198_frame, text = "Enter Rate Above for 3198")
    c3198_label.pack(pady = 5)

    # Creating Second Input Box
    global c3198_input2
    c3198_input2 = Entry(c3198_frame)
    c3198_input2.pack(pady = 5)

    # Creating Second Label
    global c3198_label2
    c3198_label2 = Label(c3198_frame, text = "Choose from Purchase Amount List Below")
    c3198_label3 = Label(c3198_frame, text = "7,000 – 21,499") 
    c3198_label2.pack(pady = 5)
    c3198_label3.pack(pady = 5)

    # Creating Answer Button
    c3198_button = Button(c3198_frame, text = "Calculate WAC", command = c3198_wac)
    c3198_button.pack(pady = 5)

def c3198_wac():
    concat_var4 = c3198_input2.get() + "3198"
    df.loc[df['Concat4'] == concat_var4, 'LOAN_RATE'] = float(c3198_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3198_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3198_input.delete(0, 'end')
    c3198_input2.delete(0, 'end')

def c3199_code():
    hide_menu_frames()
    c3199_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3199_button2 = Button(c3199_frame, text = "Previous Page", command = seventh_home)
    c3199_button2.pack(pady = 10)

    # Creating Input Box
    global c3199_input
    c3199_input = Entry(c3199_frame)
    c3199_input.pack(pady = 5)

    # Creating Label
    global c3199_label
    c3199_label = Label(c3199_frame, text = "Enter Rate Above for 3199")
    c3199_label.pack(pady = 5)

    # Creating Second Input Box
    global c3199_input2
    c3199_input2 = Entry(c3199_frame)
    c3199_input2.pack(pady = 5)

    # Creating Second Label
    global c3199_label2
    c3199_label2 = Label(c3199_frame, text = "Choose from Purchase Amount List Below")
    c3199_label3 = Label(c3199_frame, text = "21,500 +")
    c3199_label2.pack(pady = 5)
    c3199_label3.pack(pady = 5)

    # Creating Answer Button
    c3199_button = Button(c3199_frame, text = "Calculate WAC", command = c3199_wac)
    c3199_button.pack(pady = 5)

def c3199_wac():
    concat_var4 = c3199_input2.get() + "3199"
    df.loc[df['Concat4'] == concat_var4, 'LOAN_RATE'] = float(c3199_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3199_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3199_input.delete(0, 'end')
    c3199_input2.delete(0, 'end')

def c3230_code():
    hide_menu_frames()
    c3230_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c3230_button2 = Button(c3230_frame, text = "Previous Page", command = seventh_home)
    c3230_button2.pack(pady = 10)

    # Creating Input Box
    global c3230_input
    c3230_input = Entry(c3230_frame)
    c3230_input.pack(pady = 5)

    # Creating Label
    global c3230_label
    c3230_label = Label(c3230_frame, text = "Enter Rate Above for 3230")
    c3230_label.pack(pady = 5)

    # Creating Second Input Box
    global c3230_input2
    c3230_input2 = Entry(c3230_frame)
    c3230_input2.pack(pady = 5)

    # Creating Second Label
    global c3230_label2
    c3230_label2 = Label(c3230_frame, text = "Choose from Purchase Amount List Below")
    c3230_label3 = Label(c3230_frame, text = "7,000 – 21,499") 
    c3230_label6 = Label(c3230_frame, text = "21,500 +")
    c3230_label2.pack(pady = 5)
    c3230_label3.pack(pady = 5)
    c3230_label6.pack(pady = 5)

    # Creating Answer Button
    c3230_button = Button(c3230_frame, text = "Calculate WAC", command = c3230_wac)
    c3230_button.pack(pady = 5)

def c3230_wac():
    concat_var4 = c3230_input2.get() + "3230"
    df.loc[df['Concat4'] == concat_var4, 'LOAN_RATE'] = float(c3230_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c3230_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c3230_input.delete(0, 'end')
    c3230_input2.delete(0, 'end')

def c9009_code():
    hide_menu_frames()
    c9009_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c9009_button2 = Button(c9009_frame, text = "Previous Page", command = seventh_home)
    c9009_button2.pack(pady = 10)

    # Creating Input Box
    global c9009_input
    c9009_input = Entry(c9009_frame)
    c9009_input.pack(pady = 5)

    # Creating Label
    global c9009_label
    c9009_label = Label(c9009_frame, text = "Enter Rate Above for 9009")
    c9009_label.pack(pady = 5)

    # Creating Second Input Box
    global c9009_input2
    c9009_input2 = Entry(c9009_frame)
    c9009_input2.pack(pady = 5)

    # Creating Second Label
    global c9009_label2
    c9009_label2 = Label(c9009_frame, text = "Choose from Purchase Amount List Below")
    c9009_label3 = Label(c9009_frame, text = "7,000 – 21,499") 
    c9009_label2.pack(pady = 5)
    c9009_label3.pack(pady = 5)

    # Creating Answer Button
    c9009_button = Button(c9009_frame, text = "Calculate WAC", command = c9009_wac)
    c9009_button.pack(pady = 5)

def c9009_wac():
    concat_var4 = c9009_input2.get() + "9009"
    df.loc[df['Concat4'] == concat_var4, 'LOAN_RATE'] = float(c9009_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c9009_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c9009_input.delete(0, 'end')
    c9009_input2.delete(0, 'end')

def c9010_code():
    hide_menu_frames()
    c9010_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c9010_button2 = Button(c9010_frame, text = "Previous Page", command = seventh_home)
    c9010_button2.pack(pady = 10)

    # Creating Input Box
    global c9010_input
    c9010_input = Entry(c9010_frame)
    c9010_input.pack(pady = 5)

    # Creating Label
    global c9010_label
    c9010_label = Label(c9010_frame, text = "Enter Rate Above for 9010")
    c9010_label.pack(pady = 5)

    # Creating Second Input Box
    global c9010_input2
    c9010_input2 = Entry(c9010_frame)
    c9010_input2.pack(pady = 5)

    # Creating Second Label
    global c9010_label2
    c9010_label2 = Label(c9010_frame, text = "Choose from Purchase Amount List Below")
    c9010_label3 = Label(c9010_frame, text = "7,000 – 21,499") 
    c9010_label2.pack(pady = 5)
    c9010_label3.pack(pady = 5)

    # Creating Answer Button
    c9010_button = Button(c9010_frame, text = "Calculate WAC", command = c9010_wac)
    c9010_button.pack(pady = 5)

def c9010_wac():
    concat_var4 = c9010_input2.get() + "9010"
    df.loc[df['Concat4'] == concat_var4, 'LOAN_RATE'] = float(c9010_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c9010_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c9010_input.delete(0, 'end')
    c9010_input2.delete(0, 'end')

def c9029_code():
    hide_menu_frames()
    c9029_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c9029_button2 = Button(c9029_frame, text = "Previous Page", command = seventh_home)
    c9029_button2.pack(pady = 10)

    # Creating Input Box
    global c9029_input
    c9029_input = Entry(c9029_frame)
    c9029_input.pack(pady = 5)

    # Creating Label
    global c9029_label
    c9029_label = Label(c9029_frame, text = "Enter Rate Above for 9029")
    c9029_label.pack(pady = 5)

    # Creating Second Input Box
    global c9029_input2
    c9029_input2 = Entry(c9029_frame)
    c9029_input2.pack(pady = 5)

    # Creating Second Label
    global c9029_label2
    c9029_label2 = Label(c9029_frame, text = "Choose from Purchase Amount List Below")
    c9029_label3 = Label(c9029_frame, text = "7,000 – 21,499") 
    c9029_label2.pack(pady = 5)
    c9029_label3.pack(pady = 5)

    # Creating Answer Button
    c9029_button = Button(c9029_frame, text = "Calculate WAC", command = c9029_wac)
    c9029_button.pack(pady = 5)

def c9029_wac():
    concat_var4 = c9029_input2.get() + "9029"
    df.loc[df['Concat4'] == concat_var4, 'LOAN_RATE'] = float(c9029_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c9029_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c9029_input.delete(0, 'end')
    c9029_input2.delete(0, 'end')

def c9030_code():
    hide_menu_frames()
    c9030_frame.pack(fill = "both", expand = 1)

    # Creating a Back Button
    c9030_button2 = Button(c9030_frame, text = "Previous Page", command = seventh_home)
    c9030_button2.pack(pady = 10)

    # Creating Input Box
    global c9030_input
    c9030_input = Entry(c9030_frame)
    c9030_input.pack(pady = 5)

    # Creating Label
    global c9030_label
    c9030_label = Label(c9030_frame, text = "Enter Rate Above for 9030")
    c9030_label.pack(pady = 5)

    # Creating Second Input Box
    global c9030_input2
    c9030_input2 = Entry(c9030_frame)
    c9030_input2.pack(pady = 5)

    # Creating Second Label
    global c9030_label2
    c9030_label2 = Label(c9030_frame, text = "Choose from Purchase Amount List Below")
    c9030_label3 = Label(c9030_frame, text = "7,000 – 21,499") 
    c9030_label2.pack(pady = 5)
    c9030_label3.pack(pady = 5)

    # Creating Answer Button
    c9030_button = Button(c9030_frame, text = "Calculate WAC", command = c9030_wac)
    c9030_button.pack(pady = 5)

def c9030_wac():
    concat_var4 = c9030_input2.get() + "9030"
    df.loc[df['Concat4'] == concat_var4, 'LOAN_RATE'] = float(c9030_input.get())

    df["Rate_WT"] = df["ORIG_AMT"] * df["LOAN_RATE"]
    WAC = round(df["Rate_WT"].sum() / df["ORIG_AMT"].sum(),3)
    WAC_label = Label(c9030_frame, text = WAC, font = ("Helvetica", 14))
    WAC_label.pack(pady = 5)

    # Clearing the answer box
    c9030_input.delete(0, 'end')
    c9030_input2.delete(0, 'end')


###############################################################################################################################################################################


# Creating a Hide Frame Function
def hide_menu_frames():
    # Destroying the children widgets in each frame
    for widget in c3186_frame.winfo_children():
        widget.destroy()
    for widget in c3191_frame.winfo_children():
        widget.destroy()
    for widget in c3198_frame.winfo_children():
        widget.destroy()
    for widget in c3199_frame.winfo_children():
        widget.destroy()
    for widget in c3210_frame.winfo_children():
        widget.destroy()
    for widget in c3211_frame.winfo_children():
        widget.destroy()
    for widget in c3214_frame.winfo_children():
        widget.destroy()
    for widget in c3216_frame.winfo_children():
        widget.destroy()
    for widget in c3230_frame.winfo_children():
        widget.destroy()
    for widget in c3231_frame.winfo_children():
        widget.destroy()
    for widget in c3237_frame.winfo_children():
        widget.destroy()
    for widget in c3239_frame.winfo_children():
        widget.destroy()
    for widget in c3241_frame.winfo_children():
        widget.destroy()
    for widget in c3242_frame.winfo_children():
        widget.destroy()
    for widget in c3232_frame.winfo_children():
        widget.destroy()
    for widget in c3233_frame.winfo_children():
        widget.destroy()
    for widget in c3240_frame.winfo_children():
        widget.destroy()
    for widget in c3247_frame.winfo_children():
        widget.destroy()
    for widget in c3248_frame.winfo_children():
        widget.destroy()
    for widget in c9009_frame.winfo_children():
        widget.destroy()
    for widget in c9010_frame.winfo_children():
        widget.destroy()
    for widget in c9029_frame.winfo_children():
        widget.destroy()
    for widget in c9030_frame.winfo_children():
        widget.destroy()
    for widget in start_frame.winfo_children():
        widget.destroy()
    for widget in second_frame.winfo_children():
        widget.destroy()
    for widget in third_frame.winfo_children():
        widget.destroy()
    for widget in fourth_frame.winfo_children():
        widget.destroy()
    for widget in fifth_frame.winfo_children():
        widget.destroy()
    for widget in sixth_frame.winfo_children():
        widget.destroy()
    for widget in seventh_frame.winfo_children():
        widget.destroy()

    # Hiding all frames
    c3186_frame.pack_forget()
    c3191_frame.pack_forget()
    c3198_frame.pack_forget()
    c3199_frame.pack_forget()
    c3210_frame.pack_forget()
    c3211_frame.pack_forget()
    c3216_frame.pack_forget()
    c3214_frame.pack_forget()
    c3230_frame.pack_forget()
    c3231_frame.pack_forget()
    c3237_frame.pack_forget()
    c3239_frame.pack_forget()
    c3232_frame.pack_forget()
    c3233_frame.pack_forget()
    c3240_frame.pack_forget()
    c3241_frame.pack_forget()
    c3242_frame.pack_forget()
    c3247_frame.pack_forget()
    c3248_frame.pack_forget()
    c9009_frame.pack_forget()
    c9010_frame.pack_forget()
    c9029_frame.pack_forget()
    c9030_frame.pack_forget()
    start_frame.pack_forget()
    second_frame.pack_forget()
    third_frame.pack_forget()
    fourth_frame.pack_forget()
    fifth_frame.pack_forget()
    sixth_frame.pack_forget()
    seventh_frame.pack_forget()

# Creating Frames
c3186_frame = Frame(root, width = 600, height = 600)
c3191_frame = Frame(root, width = 600, height = 600)
c3198_frame = Frame(root, width = 600, height = 600)
c3199_frame = Frame(root, width = 600, height = 600)
c3210_frame = Frame(root, width = 600, height = 600)
c3211_frame = Frame(root, width = 600, height = 600)
c3214_frame = Frame(root, width = 600, height = 600)
c3216_frame = Frame(root, width = 600, height = 600)
c3230_frame = Frame(root, width = 600, height = 600)
c3231_frame = Frame(root, width = 600, height = 600)
c3237_frame = Frame(root, width = 600, height = 600)
c3239_frame = Frame(root, width = 600, height = 600)
c3241_frame = Frame(root, width = 600, height = 600)
c3232_frame = Frame(root, width = 600, height = 600)
c3233_frame = Frame(root, width = 600, height = 600)
c3240_frame = Frame(root, width = 600, height = 600)
c3241_frame = Frame(root, width = 600, height = 600)
c3242_frame = Frame(root, width = 600, height = 600)
c3247_frame = Frame(root, width = 600, height = 600)
c3248_frame = Frame(root, width = 600, height = 600)
c9009_frame = Frame(root, width = 600, height = 600)
c9010_frame = Frame(root, width = 600, height = 600)
c9029_frame = Frame(root, width = 600, height = 600)
c9030_frame = Frame(root, width = 600, height = 600)
start_frame = Frame(root, width = 600, height = 600)
second_frame = Frame(root, width = 600, height = 600) 
third_frame = Frame(root, width = 600, height = 600)
fourth_frame = Frame(root, width = 600, height = 600)
fifth_frame = Frame(root, width = 600, height = 600)
sixth_frame = Frame(root, width = 600, height = 600)
seventh_frame = Frame(root, width = 600, height = 600)

# Creating Start Screen & Other Menu Screens
def home():
    hide_menu_frames()
    start_frame.pack(fill = "both", expand = 1)
    start_label = Label(start_frame, text = "Choose Financing Criteria", font = ("Helvetica", 18)).pack(pady = 40) 

    mvc_int_button = Button(start_frame, text = "MVC International Rates", font = ("Helvetica", 13), bg='#ffffff', activeforeground='#4444ff', command = seventh_home).pack(pady = 5)
    mvc_dom_10_button = Button(start_frame, text = "MVC Domestic Standard 10 Yr Rates Points", font = ("Helvetica", 13), bg='#ffffff', activeforeground='#4444ff', command = second_home).pack(pady = 5)
    mvc_dom_15_button = Button(start_frame, text = "MVC Domestic Standard 15 Yr Rates Points", font = ("Helvetica", 13), bg='#ffffff', activeforeground='#4444ff', command = fourth_home).pack(pady = 5)
    mvc_dom_10_deed_button = Button(start_frame, text = "MVC Domestic Standard 10 Yr Rates Deeded Weeks", font = ("Helvetica", 13), bg='#ffffff', activeforeground='#4444ff', command = third_home).pack(pady = 5)
    mvc_dom_15_deed_button = Button(start_frame, text = "MVC Domestic Standard 15 Yr Rates Deeded Weeks", font = ("Helvetica", 13), bg='#ffffff', activeforeground='#4444ff', command = fifth_home).pack(pady = 5)
    mvc_car_lam_fin_button = Button(start_frame, text = "MVCI Caribbean and Latin America Financing Programs", font = ("Helvetica", 13), bg='#ffffff', activeforeground='#4444ff', command = sixth_home).pack(pady = 5)
    
    reset_wac_button = Button(start_frame, text = "Reset WAC Calculation", font = ("Helvetica", 13), bg='#ffffff', activeforeground='#4444ff', command = Reset_WAC).pack(pady = 5)

def second_home():
    hide_menu_frames()
    second_frame.pack(fill = "both", expand = 1)
    start_label = Label(second_frame, text = "Choose Code", font = ("Helvetica", 18)).pack(pady = 40)

    # Creating buttons to codes
    chome_button = Button(second_frame, text = "Home Page", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = home).pack(pady = 5)
    c3231_button = Button(second_frame, text = "Enter Rate for 3231", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3231_code).pack(pady = 5)
    c3239_button = Button(second_frame, text = "Enter Rate for 3239", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3239_code).pack(pady = 5)
    c3232_button = Button(second_frame, text = "Enter Rate for 3232", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3232_code).pack(pady = 5)
    c3247_button = Button(second_frame, text = "Enter Rate for 3247", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3247_code).pack(pady = 5)

def third_home():
    hide_menu_frames()
    third_frame.pack(fill = "both", expand = 1)
    start_label = Label(third_frame, text = "Choose Code", font = ("Helvetica", 18)).pack(pady = 40)

    # Creating buttons to codes
    chome_button = Button(third_frame, text = "Home Page", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = home).pack(pady = 5)
    c3233_button = Button(third_frame, text = "Enter Rate for 3233", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3233_code).pack(pady = 5)
    c3240_button = Button(third_frame, text = "Enter Rate for 3240", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3240_code).pack(pady = 5)

def fourth_home():
    hide_menu_frames()
    fourth_frame.pack(fill = "both", expand = 1)
    start_label = Label(fourth_frame, text = "Choose Code", font = ("Helvetica", 18)).pack(pady = 40)

    # Creating buttons to codes
    chome_button = Button(fourth_frame, text = "Home Page", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = home).pack(pady = 5)
    c3214_button = Button(fourth_frame, text = "Enter Rate for 3214", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3214_code).pack(pady = 5)
    c3241_button = Button(fourth_frame, text = "Enter Rate for 3241", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3241_code).pack(pady = 5)
    c3216_button = Button(fourth_frame, text = "Enter Rate for 3216", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3216_code).pack(pady = 5)
    c3248_button = Button(fourth_frame, text = "Enter Rate for 3248", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3248_code).pack(pady = 5)

def fifth_home():
    hide_menu_frames()
    fifth_frame.pack(fill = "both", expand = 1)
    start_label = Label(fifth_frame, text = "Choose Code", font = ("Helvetica", 18)).pack(pady = 40)

    # Creating buttons to codes
    chome_button = Button(fifth_frame, text = "Home Page", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = home).pack(pady = 5)
    c3237_button = Button(fifth_frame, text = "Enter Rate for 3237", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3237_code).pack(pady = 5)
    c3242_button = Button(fifth_frame, text = "Enter Rate for 3242", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3242_code).pack(pady = 5)

def sixth_home():
    hide_menu_frames()
    sixth_frame.pack(fill = "both", expand = 1)
    start_label = Label(sixth_frame, text = "Choose Code", font = ("Helvetica", 18)).pack(pady = 40)

    # Creating buttons to codes
    chome_button = Button(sixth_frame, text = "Home Page", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = home).pack(pady = 5)
    c3191_button = Button(sixth_frame, text = "Enter Rate for 3191", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3191_code).pack(pady = 5)
    c3186_button = Button(sixth_frame, text = "Enter Rate for 3186", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3186_code).pack(pady = 5)
    c3210_button = Button(sixth_frame, text = "Enter Rate for 3210", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3210_code).pack(pady = 5)
    c3211_button = Button(sixth_frame, text = "Enter Rate for 3211", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3211_code).pack(pady = 5)

def seventh_home():
    hide_menu_frames()
    seventh_frame.pack(fill = "both", expand = 1)
    start_label = Label(seventh_frame, text = "Choose Code", font = ("Helvetica", 18)).pack(pady = 40)

    # Creating buttons to codes
    chome_button = Button(seventh_frame, text = "Home Page", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = home).pack(pady = 5)
    c3198_button = Button(seventh_frame, text = "Enter Rate for 3198", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3198_code).pack(pady = 5)
    c3199_button = Button(seventh_frame, text = "Enter Rate for 3199", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3199_code).pack(pady = 5)
    c3230_button = Button(seventh_frame, text = "Enter Rate for 3230", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c3230_code).pack(pady = 5)
    c9009_button = Button(seventh_frame, text = "Enter Rate for 9009", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c9009_code).pack(pady = 5)
    c9010_button = Button(seventh_frame, text = "Enter Rate for 9010", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c9010_code).pack(pady = 5)
    c9029_button = Button(seventh_frame, text = "Enter Rate for 9029", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c9029_code).pack(pady = 5)
    c9030_button = Button(seventh_frame, text = "Enter Rate for 9030", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 13), command = c9030_code).pack(pady = 5)

# Creating Menu Items
app_menu = Menu(my_menu)
my_menu.add_cascade(label = "Options", menu = app_menu)
app_menu.add_command(label = "Home", command = home)
app_menu.add_separator()
app_menu.add_command(label = "Exit", command = root.quit)

# Adding Images
my_image = ImageTk.PhotoImage(Image.open("mvww.png"))
image_label = Label(image = my_image)
image_label.pack(pady = 30)

# Showing the Start Screen
home()

root.mainloop()

# Created & Written by Matthew Horvath for use by Marriott Vacations Worldwide Capital Markets Team