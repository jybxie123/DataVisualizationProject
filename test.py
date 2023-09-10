import pandas as pd
import matplotlib.pyplot as plt

'''
我希望计算出2020-2021年度最优秀的球员们
'''
data_path = "./"
advanced = "nba2021_advanced.csv"
per36min = "nba2021_per36min.csv"
advancedData = pd.read_csv(data_path+advanced, encoding="gbk",sep=',')
# print(advancedData.head(20))

advancedData_clear = advancedData.drop(advancedData[advancedData['MP']<800].index)
# print(advancedData_clear.head(20))
bpm = advancedData_clear.sort_values(by=['BPM'], ascending=False)
bpm = bpm.head(20)

bpm.loc[bpm["Pos"]=='C',"Pos_index"] = 5
bpm.loc[bpm["Pos"]=='PF',"Pos_index"] = 4
bpm.loc[bpm["Pos"]=='SF',"Pos_index"] = 3
bpm.loc[bpm["Pos"]=='SG',"Pos_index"] = 2
bpm.loc[bpm["Pos"]=='PG',"Pos_index"] = 1
color_list = ["red",'green','blue','black','orange']
plt.scatter(x=bpm["MP"], y=bpm["TS%"],c=bpm['Pos_index'],cmap='Oranges')
for i in bpm.index:
    # print(bpm.loc[i,"Player"])
    plt.annotate(text= bpm.loc[i,"Player"],xy=(bpm.loc[i,"MP"],bpm.loc[i,"TS%"]), xytext=(bpm.loc[i,"MP"],bpm.loc[i,"TS%"]))
plt.show()
'''
# these are basic data
score_file = file.sort_values(by=['PTS'], ascending=False)
print(score_file.head(20))

defence_file = file.sort_values(by=['TRB','STL','BLK'], ascending=False)
print(defence_file.head(20))
'''


