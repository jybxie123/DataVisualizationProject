import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text
import numpy as np
'''
针对部分球员，比较他们和他们队友的高阶数据。
'''
# path
data_path = "./"
advanced = "nba2021_advanced.csv"
per36min = "nba2021_per36min.csv"
pergame = "nba2021_per_game.csv"

# dataframe: source of data
advancedData = pd.read_csv(data_path+advanced, encoding="UTF-8",sep=',')
gameBasicData = pd.read_csv(data_path+pergame, encoding="UTF-8",sep=',')

# selectedPlayers = ['Kevin Durant', 'James Harden', 'CJ McCollum', 'Damian Lillard']
# selectIndex= [126,181,299,272]
selectedPlayers = ['Nikola Jokić','Luka Dončić', 'Giannis Antetokounmpo', 'Kawhi Leonard', 'James Harden', 'CJ McCollum', 'Damian Lillard', 'Stephen Curry']
selectIndex= [237,117,13,268,181,299,272,108]

# 场均得分和真实命中率
Xcate = "Player"
Ycate1 = "VORP"
Ycate2 = ""
selectedData = pd.DataFrame(columns=advancedData.columns)

for i in selectIndex:
   selectedData = pd.concat([selectedData, advancedData[advancedData.index == i]])

#sort
selectedData.sort_values(by=[Ycate1], ascending=False, inplace=True)
# print(selectedData)

# associated plot with two characters
# num = len(selectedPlayers)
# xpos = np.arange(num)
# total_width, n = 0.8, 2
# width = total_width / n
# xpos = xpos - (total_width - width) / 2

# fig, ax1 = plt.subplots()
# # 设置左侧Y轴对应的figure
# ax1.set_ylabel(Ycate1)
# ax1.set_ylim(5,8)
# s1 = ax1.bar(xpos - width/2, selectedData[Ycate1], width=width, color='green', align='edge')

# ax1.set_xticklabels(ax1.get_xticklabels(),rotation=270)  # 设置共用的x轴

# # 设置右侧Y轴对应的figure
# ax2 = ax1.twinx()
# ax2.set_ylabel(Ycate2)
# ax2.set_ylim(2,5)
# s2 = ax2.bar(xpos + width/2, selectedData[Ycate2], width=width, color='blue', align='edge', tick_label=selectedData['Player'])

# plt.legend((s1,s2),[Ycate1,Ycate2], title= 'position',loc='best')
# plt.tight_layout()
# plt.show()

# single character display.
for i in selectedData.index:
    if selectedData.loc[i,'Pos'] == 'PG':
        s1 = plt.bar(selectedData.loc[i,Xcate],selectedData.loc[i,Ycate1],color="blue")
        plt.text(x=selectedData.loc[i,Xcate],y=selectedData.loc[i,Ycate1],s=selectedData.loc[i,Ycate1])
    elif selectedData.loc[i,'Pos'] == 'SG':
        s2 = plt.bar(selectedData.loc[i,Xcate],selectedData.loc[i,Ycate1],color="red")
        plt.text(x=selectedData.loc[i,Xcate],y=selectedData.loc[i,Ycate1],s=selectedData.loc[i,Ycate1])
    else:
        s3 = plt.bar(selectedData.loc[i,Xcate],selectedData.loc[i,Ycate1],color="gray")
        plt.text(x=selectedData.loc[i,Xcate],y=selectedData.loc[i,Ycate1],s=selectedData.loc[i,Ycate1])
plt.xticks(rotation=270)
plt.ylabel(Ycate1)
plt.ylim(0.5,3.5)
plt.tight_layout()
plt.legend((s1,s2,s3),['PG','SG','Other positions'])
plt.savefig('./result/vorp.svg',format='svg',dpi=200)
plt.show()