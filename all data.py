import pandas as pd


all_data=pd.DataFrame()

Morning_Low = pd.read_csv('A_Morning_Low.csv')
Morning_Medium = pd.read_csv('A_Morning_Medium.csv')
Morning_High = pd.read_csv('A_Morning_High.csv')
Noon_Low = pd.read_csv('A_Noon_Low.csv')
Noon_Medium = pd.read_csv('A_Noon_Medium.csv')
Noon_High = pd.read_csv('A_Noon_High.csv')
Evening_Low = pd.read_csv('A_Evening_Low.csv')
Evening_Medium = pd.read_csv('A_Evening_Medium.csv')
Evening_High = pd.read_csv('A_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("A_DATA.csv",index=False)
print ("A :)")

########################################################################

all_data=pd.DataFrame()

Morning_Low = pd.read_csv('B_Morning_Low.csv')
Morning_Medium = pd.read_csv('B_Morning_Medium.csv')
Morning_High = pd.read_csv('B_Morning_High.csv')
Noon_Low = pd.read_csv('B_Noon_Low.csv')
Noon_Medium = pd.read_csv('B_Noon_Medium.csv')
Noon_High = pd.read_csv('B_Noon_High.csv')
Evening_Low = pd.read_csv('B_Evening_Low.csv')
Evening_Medium = pd.read_csv('B_Evening_Medium.csv')
Evening_High = pd.read_csv('B_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("B_DATA.csv",index=False)
print ("B :)")

########################################################################

all_data=pd.DataFrame()


Morning_Low = pd.read_csv('C_Morning_Low.csv')
Morning_Medium = pd.read_csv('C_Morning_Medium.csv')
Morning_High = pd.read_csv('C_Morning_High.csv')
Noon_Low = pd.read_csv('C_Noon_Low.csv')
Noon_Medium = pd.read_csv('C_Noon_Medium.csv')
Noon_High = pd.read_csv('C_Noon_High.csv')
Evening_Low = pd.read_csv('C_Evening_Low.csv')
Evening_Medium = pd.read_csv('C_Evening_Medium.csv')
Evening_High = pd.read_csv('C_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("C_DATA.csv",index=False)
print ("C :)")

########################################################################

all_data=pd.DataFrame()

Morning_Low = pd.read_csv('D_Morning_Low.csv')
Morning_Medium = pd.read_csv('D_Morning_Medium.csv')
Morning_High = pd.read_csv('D_Morning_High.csv')
Noon_Low = pd.read_csv('D_Noon_Low.csv')
Noon_Medium = pd.read_csv('D_Noon_Medium.csv')
Noon_High = pd.read_csv('D_Noon_High.csv')
Evening_Low = pd.read_csv('D_Evening_Low.csv')
Evening_Medium = pd.read_csv('D_Evening_Medium.csv')
Evening_High = pd.read_csv('D_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("D_DATA.csv",index=False)
print ("D :)")

########################################################################

all_data=pd.DataFrame()

Morning_Low = pd.read_csv('E_Morning_Low.csv')
Morning_Medium = pd.read_csv('E_Morning_Medium.csv')
Morning_High = pd.read_csv('E_Morning_High.csv')
Noon_Low = pd.read_csv('E_Noon_Low.csv')
Noon_Medium = pd.read_csv('E_Noon_Medium.csv')
Noon_High = pd.read_csv('E_Noon_High.csv')
Evening_Low = pd.read_csv('E_Evening_Low.csv')
Evening_Medium = pd.read_csv('E_Evening_Medium.csv')
Evening_High = pd.read_csv('E_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("E_DATA.csv",index=False)
print ("E :)")

########################################################################

all_data=pd.DataFrame()

Morning_Low = pd.read_csv('F_Morning_Low.csv')
Morning_Medium = pd.read_csv('F_Morning_Medium.csv')
Morning_High = pd.read_csv('F_Morning_High.csv')
Noon_Low = pd.read_csv('F_Noon_Low.csv')
Noon_Medium = pd.read_csv('F_Noon_Medium.csv')
Noon_High = pd.read_csv('F_Noon_High.csv')
Evening_Low = pd.read_csv('F_Evening_Low.csv')
Evening_Medium = pd.read_csv('F_Evening_Medium.csv')
Evening_High = pd.read_csv('F_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("F_DATA.csv",index=False)
print ("F :)")

########################################################################


all_data=pd.DataFrame()

Morning_Low = pd.read_csv('G_Morning_Low.csv')
Morning_Medium = pd.read_csv('G_Morning_Medium.csv')
Morning_High = pd.read_csv('G_Morning_High.csv')
Noon_Low = pd.read_csv('G_Noon_Low.csv')
Noon_Medium = pd.read_csv('G_Noon_Medium.csv')
Noon_High = pd.read_csv('G_Noon_High.csv')
Evening_Low = pd.read_csv('G_Evening_Low.csv')
Evening_Medium = pd.read_csv('G_Evening_Medium.csv')
Evening_High = pd.read_csv('G_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("G_DATA.csv",index=False)
print ("G :)")


########################################################################


all_data=pd.DataFrame()

Morning_Low = pd.read_csv('H_Morning_Low.csv')
Morning_Medium = pd.read_csv('H_Morning_Medium.csv')
Morning_High = pd.read_csv('H_Morning_High.csv')
Noon_Low = pd.read_csv('H_Noon_Low.csv')
Noon_Medium = pd.read_csv('H_Noon_Medium.csv')
Noon_High = pd.read_csv('H_Noon_High.csv')
Evening_Low = pd.read_csv('H_Evening_Low.csv')
Evening_Medium = pd.read_csv('H_Evening_Medium.csv')
Evening_High = pd.read_csv('H_Evening_High.csv')
Evening_High = pd.read_csv('H_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("H_DATA.csv",index=False)
print ("H :)")


########################################################################


all_data=pd.DataFrame()

Morning_Low = pd.read_csv('I_Morning_Low.csv')
Morning_Medium = pd.read_csv('I_Morning_Medium.csv')
Morning_High = pd.read_csv('I_Morning_High.csv')
Noon_Low = pd.read_csv('I_Noon_Low.csv')
Noon_Medium = pd.read_csv('I_Noon_Medium.csv')
Noon_High = pd.read_csv('I_Noon_High.csv')
Evening_Low = pd.read_csv('I_Evening_Low.csv')
Evening_Medium = pd.read_csv('I_Evening_Medium.csv')
Evening_High = pd.read_csv('I_Evening_High.csv')

all_data=all_data.append(Morning_Low)
all_data=all_data.append(Morning_Medium)
all_data=all_data.append(Morning_High)
all_data=all_data.append(Noon_Low)
all_data=all_data.append(Noon_Medium)
all_data=all_data.append(Noon_High)
all_data=all_data.append(Evening_Low)
all_data=all_data.append(Evening_Medium)
all_data=all_data.append(Evening_High)

all_data.to_csv("I_DATA.csv",index=False)
print ("I :)")









