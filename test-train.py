##test-train###

#test:
#Low - Morning
#Medium - Evening
#High - Noon

#train:
#Low - Evening Noon
#Medium - Morning Noon
#High - Morning Evening

import pandas as pd

def test_set (data):
    Low_Morning=data[data['Type'].str.match('Low')]
    Low_Morning=Low_Morning[Low_Morning['Day'].str.match('Morning')]

    Medium_Evening=data[data['Type'].str.match('Medium')]
    Medium_Evening=Medium_Evening[Medium_Evening['Day'].str.match('Evening')]

    High_Noon=data[data['Type'].str.match('High')]
    High_Noon=High_Noon[High_Noon['Day'].str.match('Noon')]

    test = Low_Morning
    test = test.append(Medium_Evening)
    test = test.append(High_Noon)

    return test

def train_set (data):
    #Low_Evening_Noon
    Low_Evening=data[data['Type'].str.match('Low')]
    Low_Evening=Low_Evening[Low_Evening['Day'].str.match('Evening')]

    Low_Noon=data[data['Type'].str.match('Low')]
    Low_Noon=Low_Noon[Low_Noon['Day'].str.match('Noon')]

    #Medium_Morning_Noon
    Medium_Morning=data[data['Type'].str.match('Medium')]
    Medium_Morning=Medium_Morning[Medium_Morning['Day'].str.match('Morning')]

    Medium_Noon=data[data['Type'].str.match('Medium')]
    Medium_Noon=Medium_Noon[Medium_Noon['Day'].str.match('Noon')]

    #High_Morning_Evening
    High_Morning=data[data['Type'].str.match('High')]
    High_Morning=High_Morning[High_Morning['Day'].str.match('Morning')]

    High_Evening=data[data['Type'].str.match('High')]
    High_Evening=High_Evening[High_Evening['Day'].str.match('Evening')]

    train=Low_Evening
    train=train.append(Low_Noon)
    train=train.append(Medium_Morning)
    train=train.append(Medium_Noon)
    train=train.append(High_Morning)
    train=train.append(High_Evening)

    return train


data = pd.read_csv('all_data_A_15secN.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_A_15sec_testSet.csv",index=False)
train.to_csv("all_data_A_15sec_trainSet.csv",index=False)




'''
data = pd.read_csv('all_data_A_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_A_60sec_testSet.csv",index=False)
train.to_csv("all_data_A_60sec_trainSet.csv",index=False)

data = pd.read_csv('all_data_B_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_B_60sec_testSet.csv",index=False)
train.to_csv("all_data_B_60sec_trainSet.csv",index=False)

data = pd.read_csv('all_data_C_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_C_60sec_testSet.csv",index=False)
train.to_csv("all_data_C_60sec_trainSet.csv",index=False)


data = pd.read_csv('all_data_D_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_D_60sec_testSet.csv",index=False)
train.to_csv("all_data_D_60sec_trainSet.csv",index=False)


data = pd.read_csv('all_data_E_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_E_60sec_testSet.csv",index=False)
train.to_csv("all_data_E_60sec_trainSet.csv",index=False)


data = pd.read_csv('all_data_F_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_F_60sec_testSet.csv",index=False)
train.to_csv("all_data_F_60sec_trainSet.csv",index=False)


data = pd.read_csv('all_data_G_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_G_60sec_testSet.csv",index=False)
train.to_csv("all_data_G_60sec_trainSet.csv",index=False)


data = pd.read_csv('all_data_H_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_H_60sec_testSet.csv",index=False)
train.to_csv("all_data_H_60sec_trainSet.csv",index=False)


data = pd.read_csv('all_data_I_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_I_60sec_testSet.csv",index=False)
train.to_csv("all_data_I_60sec_trainSet.csv",index=False)


data = pd.read_csv('all_data_Total_60sec.csv')
test = test_set(data)
train = train_set(data)
test.to_csv("all_data_Total_60sec_testSet.csv",index=False)
train.to_csv("all_data_Total_60sec_trainSet.csv",index=False)
'''
print(":)")


