import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text
import numpy as np
'''
根据选择出来的高阶数据最优秀的球员，比较他们的基础数据。
'''
# path
data_path = "./"
advanced = "nba2021_advanced.csv"
per36min = "nba2021_per36min.csv"
pergame = "nba2021_per_game.csv"

# dataframe: source of data
advancedData = pd.read_csv(data_path+advanced, encoding="ISO-8859-1",sep=',')
gameBasicData = pd.read_csv(data_path+pergame, encoding="UTF-8",sep=',')

selectedPlayers = ['Nikola Jokić','Luka Dončić', 'Giannis Antetokounmpo', 'Kawhi Leonard', 'James Harden', 'CJ McCollum', 'Damian Lillard', 'Stephen Curry']
selectIndex= [237,117,13,268,181,299,272,108]

# 场均得分和有效命中率
Xcate = "Player"
Ycate1 = "PTS"
Ycate2 = "PTS"
XValue = gameBasicData[Xcate]
# YValue = gameBasicData[Ycate]
selectedData = pd.DataFrame(columns=gameBasicData.columns)

for i in selectIndex:
   selectedData = pd.concat([selectedData, gameBasicData[gameBasicData.index == i]])

#sort
selectData = selectedData.sort_values(by=[Ycate1], ascending=False, inplace=True)
# print(selectData)

# num = len(selectedPlayers)
# xpos = np.arange(num)
# total_width, n = 0.8, 2
# width = total_width / n
# xpos = xpos - (total_width - width) / 2

# fig, ax1 = plt.subplots()
# # 设置左侧Y轴对应的figure
# ax1.set_ylabel(Ycate1)
# ax1.set_ylim(0.52, 0.62)
# s1 = ax1.bar(xpos - width/2, selectedData[Ycate1], width=width, color='green', align='edge')

# ax1.set_xticklabels(ax1.get_xticklabels(),rotation=270)  # 设置共用的x轴

# # 设置右侧Y轴对应的figure
# ax2 = ax1.twinx()
# ax2.set_ylabel(Ycate2)
# ax2.set_ylim(24, 31)
# s2 = ax2.bar(xpos + width/2, selectedData[Ycate2], width=width, color='blue', align='edge', tick_label=selectedData['Player'])

# plt.legend((s1,s2),[Ycate1,Ycate2], title= 'position',loc='best')
# plt.tight_layout()
# plt.show()

# single character display.
for i in selectedData.index:
    if selectedData.loc[i,'Pos'] == 'PG':
        s1 = plt.bar(selectedData.loc[i,Xcate],selectedData.loc[i,Ycate1],color="blue")
        plt.text(x=selectedData.loc[i,Xcate],y=selectedData.loc[i,Ycate1],s=selectedData.loc[i,Ycate1])
    else:
        s2 = plt.bar(selectedData.loc[i,Xcate],selectedData.loc[i,Ycate1],color="gray")
        plt.text(x=selectedData.loc[i,Xcate],y=selectedData.loc[i,Ycate1],s=selectedData.loc[i,Ycate1])
plt.xticks(rotation=270)
plt.ylabel(Ycate1)
plt.ylim(24,31)
plt.tight_layout()
plt.legend((s1,s2),['PG','Other positions'])
plt.savefig('./result/pts.svg',format='svg',dpi=200)
plt.show()