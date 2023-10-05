import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text
import numpy as np
'''
我希望计算出2020-2021年度最优秀的球员们
I need to tell a story,
Why I chose them, why they are the best


1. basic filter:
1) I don't want players who cannot play.(whose time is less than the avg of the league)

2. use some high-level metrices to select the best players:
1) I don't want players who play badly.(whose BPM is less than the avg of the league)

'''
# path
data_path = "./"
advanced = "nba2021_advanced.csv"
per36min = "nba2021_per36min.csv"
pergame = "nba2021_per_game.csv"

# dataframe: source of data
advancedData = pd.read_csv(data_path+advanced, encoding="UTF-8",sep=',')
gameBasicData = pd.read_csv(data_path+pergame)



# 1. 过滤掉上场时间不足的人、再过滤掉高阶数据太低的人（不然展示效果不好看），可以看出，约基奇统治了高阶数据bpm和ws
# data clear: if minutes playing is too small, we regard this player as an unimportant player in his team.
advancedData_clear = advancedData.drop(advancedData[advancedData['MP']<advancedData['MP'].mean()].index)
# advancedData_clear = advancedData.drop(advancedData[advancedData['MP']<150].index)
# advancedData_clear = advancedData_clear.drop(advancedData_clear[advancedData_clear['BPM']<4].index)

# we sort in a new sequence
# bpm = advancedData_clear.sort_values(by=['BPM'], ascending=False)
bpm = advancedData_clear

Xcate = "WS"
Ycate = "BPM"
XValue = bpm[Xcate]
YValue = bpm[Ycate]
fig, ax = plt.subplots(figsize=(8, 8))
for i in bpm.index:
    if bpm.loc[i, "Pos"] == 'C':
        s1 = ax.scatter(x=XValue[i], y=YValue[i],c='Red',marker='*')
    elif bpm.loc[i, "Pos"] == 'PF':
        s2 = ax.scatter(x=XValue[i], y=YValue[i],c='Orange',marker='D')
    elif bpm.loc[i, "Pos"] == 'SF':
        s3 = ax.scatter(x=XValue[i], y=YValue[i],c='Yellow',marker='s')
    elif bpm.loc[i, "Pos"] == 'SG':
        s4 = ax.scatter(x=XValue[i], y=YValue[i],c='Gray',marker='^')
    elif bpm.loc[i, "Pos"] == 'PG':
        s5 = ax.scatter(x=XValue[i], y=YValue[i],c='Blue',marker='o')

# 拟合曲线
param = np.polyfit(bpm[Xcate],bpm[Ycate],1)
f1 = np.poly1d(param)
Yfit = f1(bpm[Xcate])
plt.plot(bpm[Xcate],Yfit,'red',label='polyfit')

plt.xlabel(loc="right",xlabel=Xcate)
plt.ylabel(loc= "top", ylabel=Ycate)
plt.title(label=f"relationship between {Xcate} and {Ycate}", loc="center")
plt.legend((s1,s2,s3,s4,s5),["C","PF","SF","SG","PG"], title= 'position',loc='best')
# texts = [plt.text(s=f'{bpm.loc[i,"Player"]}',x=bpm.loc[i,Xcate],y=bpm.loc[i,Ycate]) for i in bpm.index]
# adjust_text(texts=texts,only_move={"text":'xy'})
# adjust_text(texts, save_steps=True, save_prefix = data_path+"temp/")## I have some problems here.
plt.show()



'''
# these are basic data
score_file = file.sort_values(by=['PTS'], ascending=False)
print(score_file.head(20))

defence_file = file.sort_values(by=['TRB','STL','BLK'], ascending=False)
print(defence_file.head(20))
'''


