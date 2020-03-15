import numpy as np
import jieba
import wordcloud
from PIL import Image 
import matplotlib.pyplot as plt

stwlist = [line.strip() for line in open ('stopwords.txt',encoding='utf-8').readlines()]

txt = open("诗词.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
d = dict() 
for word in words:
    if len(word) == 1:
        continue
    elif  word.strip() in stwlist:
        continue
    else:
          rword = word
    d[rword] = d.get(rword,0) + 1

    
items = list(d.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(8):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))

mask = np.array(Image.open('xin.jpeg')) # 定义词频背景
#有背景图的词云
wc = wordcloud.WordCloud(
    font_path='simfang.ttf', # 设置字体格式
    mask=mask, # 设置背景图
    max_words=200, # 最多显示词数
    max_font_size=100 ,# 字体最大值
    background_color='white',
)
#无背景图的词云
# wc = wordcloud.WordCloud(
#     r'simfang.ttf', 
#     width=500, 
#     height=400,
#     background_color='black', 
#     font_step=3,
#     max_words=200, 
#     max_font_size=100 ,
#     random_state=False, 
#     prefer_horizontal=0.9
# )

wc.generate_from_frequencies(d) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像