import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text 
'''
我希望计算出2020-2021年度最优秀的球员们
I need to tell a story,
Why I chose them, why they are the best
'''
# path
data_path = "./"
advanced = "nba2021_advanced.csv"
per36min = "nba2021_per36min.csv"
pergame = "nba2021_per_game.csv"

# dataframe: source of data
advancedData = pd.read_csv(data_path+advanced, encoding="UTF-8",sep=',')
gameBasicData = pd.read_csv(data_path+pergame)

# data clear: if minutes playing is too small, we regard this player as an unimportant player in his team.
advancedData_clear = advancedData.drop(advancedData[advancedData['MP']<100].index)
advancedData_clear = advancedData_clear.drop(advancedData_clear[advancedData_clear['BPM']<4].index)

# we sort in a new sequence
# bpm = advancedData_clear.sort_values(by=['BPM'], ascending=False)
bpm = advancedData_clear

bpm.loc[bpm["Pos"]=='C',"Pos_index"] = 5
bpm.loc[bpm["Pos"]=='PF',"Pos_index"] = 4
bpm.loc[bpm["Pos"]=='SF',"Pos_index"] = 3
bpm.loc[bpm["Pos"]=='SG',"Pos_index"] = 2
bpm.loc[bpm["Pos"]=='PG',"Pos_index"] = 1
color_list = ["red",'green','blue','black','orange']
Xcate = "MP"
Ycate = "BPM"
XValue = bpm[Xcate]
YValue = bpm[Ycate]
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x=XValue, y=YValue,c=bpm['Pos_index'],cmap="Dark2_r")
# plt.xlabel(loc="right",xlabel=Xcate)
# plt.ylabel(loc= "top", ylabel=Ycate)
# plt.title(label=f"relationship between {Xcate} and {Ycate}", loc="center")

texts = [plt.text(s=bpm.loc[i,"Player"],x=bpm.loc[i,Xcate],y=bpm.loc[i,Ycate]) for i in bpm.index]
# adjust_text(texts=texts,only_move={"text":'xy'})
adjust_text(texts, save_steps=True)## I have some problems here.
plt.show()
'''
# these are basic data
score_file = file.sort_values(by=['PTS'], ascending=False)
print(score_file.head(20))

defence_file = file.sort_values(by=['TRB','STL','BLK'], ascending=False)
print(defence_file.head(20))
'''


