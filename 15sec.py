
import pandas as pd
import statistics
import math
import numpy


def the_end_of_vector (vector,number):
    #the function returns the number of values from the end of the vector
    NewVector=[]
    if (len(vector)-number)<0:
        print("the length of the vector smaller than the number of rows")
        return None
    for r in range(number):
        NewVector.append(vector[(len(vector)-number)+r])
    return NewVector



def new_data (raw_data): #15sec
    #calculate averge HR
    first_row_flag=False
    sum_all_HR =0
    count_all_HR=0

    HRV_table = pd.DataFrame(columns =['MRR','MHR','HRV','RMSSD','SDNN','HRmaxHRminDifference','SDRR','HRV_div_aveHR','HRV_div_aveHR_MoveLast15','last5secHRave_div_aveHR','last10secHRave_div_aveHR','last15secHRave_div_aveHR', 'swat rank', 'Day', 'TLX Overall', 'Type']) #return table
    n_rows=15000 #ms for one row
    index = 1 # Count the number of ms used in the session - till 15 seconds
    ms_indicator_not_used = 0 # indicator for the amount used from specific row
    HR_Last_Row = 0 #save the last HR value of a split row
    HR_vector = []  #store the HR values in the vector for the group row
    RR_vector = []
    HR_last_vector=[] #store the last HR vector

    for i in range(len(raw_data)):
        #the for run along each row in the tabel
        RR_vector.append(raw_data["R-R (ms)"][i])

        row_indicator = raw_data["R-R (ms)"][i]
        if ms_indicator_not_used != 0: #case 3 - unused row from the last for loop
            for j in range(ms_indicator_not_used):
                HR_vector.append(HR_Last_Row)
            index = index + ms_indicator_not_used
            ms_indicator_not_used = 0
            HR_Last_Row = 0
        if index + row_indicator <= n_rows: #case 1 - full row can enter into the vector
            for j in range(row_indicator):
                HR_vector.append(raw_data["HR (bpm)"][i])
            index = index + row_indicator
        else: #case 2: part of the row can enter the vector
            ms_indicator_to_use = n_rows - index + 1
            ms_indicator_not_used = raw_data["R-R (ms)"][i] - ms_indicator_to_use
            HR_Last_Row = raw_data["HR (bpm)"][i]
            for j in range(ms_indicator_to_use):
                HR_vector.append(raw_data["HR (bpm)"][i])

            #the end of n rows session creating HRV value!!#############################################
            index = 1

            if first_row_flag==True: #Skip the first row with no history values
                #HRV=statistics.variance(HR_vector)
                aveHR=numpy.mean(HR_vector)


                #measure 1:(HRV_div_aveHR) HRV divided by HR average session
                HRV_div_aveHR=(statistics.variance(HR_vector)/aveHR)


                #measure 2: (HRV_div_aveHR_MoveLast15) HRV divided average of HR average both by "moving-average" includes the last 20 second
                num_of_last_vector=15000 #ms
                HR_vector_with_Lastsec=[]
                for k in range(len(HR_vector)): HR_vector_with_Lastsec.append(HR_vector[k])
                end_lastvector=the_end_of_vector(HR_last_vector,num_of_last_vector)
                for k in range(len(end_lastvector)): HR_vector_with_Lastsec.append(end_lastvector[k])
                HRV_moving=statistics.variance(HR_vector_with_Lastsec)
                HRV_div_aveHR_MoveLast15=(HRV_moving/(numpy.mean(HR_vector_with_Lastsec)))

                #measure 3: (last5secHR_div_aveHR) average HR of the last 5 seconds from the last vector divided by HR average of this session
                HR_vector_last5sec =the_end_of_vector(HR_last_vector,5000)
                last5secHRave_div_aveHR= numpy.mean(HR_vector_last5sec)/aveHR


                #measure 4: (last10secHR_div_aveHR) average HR of the last 10 seconds from the last vector divided by HR average of this session
                HR_vector_last10sec =the_end_of_vector(HR_last_vector,10000)
                last10secHRave_div_aveHR= numpy.mean(HR_vector_last10sec)/aveHR


                #measure 5: (last15secHR_div_aveHR) average HR of the last 15 seconds from the last vector divided by HR average of this session
                HR_vector_last15sec =the_end_of_vector(HR_last_vector,15000)
                last15secHRave_div_aveHR=numpy.mean(HR_vector_last15sec)/aveHR


                #measure 1 NEW: (MRR) mean of the RR interval
                MRR=numpy.mean(RR_vector)


                #measure 2 NEW: (MHR) mean of HR in the interval
                MHR=numpy.mean(HR_vector)

                #measur 3 NEW: (HRV) HR Standard deviation
                HRV=statistics.variance(HR_vector)

                #measur 4 NEW: (RMSSD) root ((mean difference between RR i+1 - RR i ) squared)
                for i in range(len(RR_vector)-1):
                    sumRRdifference=math.pow(RR_vector[i+1]-RR_vector[i],2)
                RMSSD=math.sqrt(sumRRdifference/(len(RR_vector)-1))

                #measur 5 NEW: (SDNN) root ((mean difference between RR i - RR ave ) squared)
                RRave=numpy.mean(RR_vector)
                for i in range(len(RR_vector)):
                    sumRRdifference=math.pow(RR_vector[i]-RRave,2)
                SDNN=(math.sqrt(sumRRdifference/(len(RR_vector)-1)))

                #measur 6 NEW: (HRmaxHRminDifference) HRmax-HRmin
                HRmaxHRminDifference= numpy.max(HR_vector)-numpy.min(HR_vector)

                #measur 7 NEW: (SDRR) RR Standard deviation
                SDRR=statistics.variance(RR_vector)

                new_row=pd.DataFrame([(MRR,MHR,HRV,RMSSD,SDNN,HRmaxHRminDifference,SDRR,HRV_div_aveHR,HRV_div_aveHR_MoveLast15,last5secHRave_div_aveHR,last10secHRave_div_aveHR,last15secHRave_div_aveHR,raw_data.iloc[i]["swat rank"],raw_data.iloc[i]["Day"],round(raw_data.iloc[i]["TLX Overall"],3),raw_data.iloc[i]["Type"])],columns = ['MRR','MHR','HRV','RMSSD','SDNN','HRmaxHRminDifference','SDRR','HRV_div_aveHR','HRV_div_aveHR_MoveLast15','last5secHRave_div_aveHR','last10secHRave_div_aveHR','last15secHRave_div_aveHR', 'swat rank', 'Day', 'TLX Overall', 'Type'])

                HRV_table=HRV_table.append(new_row)

            HR_last_vector=HR_vector
            HR_vector = []
            RR_vector =[]
            first_row_flag=True

    return HRV_table





############################################################################################################

'''

##A
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_A_15sec.csv",index=False)
print ("A :)")
all_data=[]


##B
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_B_15sec.csv",index=False)
print ("B :)")
all_data=[]

##C
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_C_15sec.csv",index=False)
print ("C :)")
all_data=[]


##D
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_D_15sec.csv",index=False)
print ("D :)")
all_data=[]
'''
##E
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_E_15sec.csv",index=False)
print ("E :)")
all_data=[]



##F
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_F_15sec.csv",index=False)
print ("F :)")
all_data=[]

##G
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_G_15sec.csv",index=False)
print ("G :)")
all_data=[]


##H
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_H_15sec.csv",index=False)
print ("H :)")
all_data=[]


##I
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

all_data=all_data.append(new_data(Morning_Low))
all_data=all_data.append(new_data(Morning_Medium))
all_data=all_data.append(new_data(Morning_High))
all_data=all_data.append(new_data(Noon_Low))
all_data=all_data.append(new_data(Noon_Medium))
all_data=all_data.append(new_data(Noon_High))
all_data=all_data.append(new_data(Evening_Low))
all_data=all_data.append(new_data(Evening_Medium))
all_data=all_data.append(new_data(Evening_High))

all_data.to_csv("all_data_I_15sec.csv",index=False)
print ("I :)")
all_data=[]




all_data=pd.DataFrame()

all_data=all_data.append(pd.read_csv('all_data_A_15sec.csv'))
all_data=all_data.append(pd.read_csv('all_data_B_15sec.csv'))
all_data=all_data.append(pd.read_csv('all_data_C_15sec.csv'))
all_data=all_data.append(pd.read_csv('all_data_D_15sec.csv'))
all_data=all_data.append(pd.read_csv('all_data_E_15sec.csv'))
all_data=all_data.append(pd.read_csv('all_data_F_15sec.csv'))
all_data=all_data.append(pd.read_csv('all_data_G_15sec.csv'))
all_data=all_data.append(pd.read_csv('all_data_H_15sec.csv'))
all_data=all_data.append(pd.read_csv('all_data_I_15sec.csv'))

all_data.to_csv("all_data_Total_15sec.csv",index=False)
print ("total :)")



