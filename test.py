# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/10/10  6:54



##图片宽，高，图片间隔。死亡图片分割
import pandas as pd
data=[
    (55,296,8,4),
    (78,512,8,4),
    (72,448,8,4),
    (77,472,8,4),
    (107,976,8,4),
    (105,948,12,8),
    (92,1510,10,6),
    (174,1512,12,8),
    (166,2196,12,8),
    (178,1870,10,6),
]
cols=['width','height','space','live']
idx=list(i for i in range(1,11))
fish=pd.DataFrame(data,columns=cols,index=idx)
print(fish)