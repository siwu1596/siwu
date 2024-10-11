import numpy as np
import matplotlib.pyplot as mp
import matplotlib.lines as mlines

x = np.linspace(-np.pi, np.pi, 1000)
cosx = np.cos(x)
sinx = np.sin(x)

# 绘制折线图
mp.plot(x, cosx/2, linestyle='-.', linewidth=2, color='dodgerblue', alpha=0.8,label='cosx')
mp.plot(x, sinx, linestyle='--', linewidth=2, color='green', alpha=0.8,label='sinx')

# Create custom line objects for the legend
line1 = mlines.Line2D([], [], color='dodgerblue', linestyle='solid', label=r'$sin(\frac{3\pi}{4}) = - \frac{\sqrt{2}}{2}$')
line2 = mlines.Line2D([], [], color='dodgerblue', linestyle='solid', label=r'$\frac{1}{2}cos(\frac{3\pi}{4}) = - \frac{\sqrt{2}}{4} $')

# 添加垂直直线
x_intercept = np.pi*3/4
y_min = min(np.sin(x_intercept), np.cos(x_intercept)/2)
y_max = max(np.sin(x_intercept), np.cos(x_intercept)/2)
mp.vlines(x_intercept, y_min, y_max, colors='dodgerblue', linestyles='solid', label='vertical line')

# 添加交点
mp.scatter([x_intercept], [np.sin(x_intercept)], color='green', edgecolor='green', facecolor='none', s=100, label='intersection sinx')
mp.scatter([x_intercept], [np.cos(x_intercept) / 2], color='green', edgecolor='green', facecolor='none', s=100, label='intersection cosx')

arrowprops1=dict(
    arrowstyle='->',      #定义箭头样式
    connectionstyle='arc'  #定义连接线的样式
)

# 添加箭头和公式标注
mp.annotate(r'$sin(\frac{3\pi}{4}) = - \frac{\sqrt{2}}{2}$',
            xy=(x_intercept, np.sin(x_intercept)), xycoords='data',
            xytext=(70, 15), textcoords='offset points',
            arrowprops=arrowprops1,
            horizontalalignment='right', verticalalignment='bottom', fontsize=12)

mp.annotate(r'$\frac{1}{2}cos(\frac{3\pi}{4}) = - \frac{\sqrt{2}}{4} $',
            xy=(x_intercept, np.cos(x_intercept) / 2), xycoords='data',
            xytext=(30, -20), textcoords='offset points',
            arrowprops=arrowprops1,
            horizontalalignment='right', verticalalignment='top', fontsize=12)

#设置坐标轴范围
mp.xlim(-np.pi, np.pi)
mp.ylim(-1, 1)

# 设置坐标刻度

vals = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi*3/4, np.pi]
texts = [r'$-\pi$', r'$-\frac{\pi}{2}$', '0',
       r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$']
mp.xticks(vals, texts)
mp.yticks([-1.0, -0.5, 0.5, 1.0])

#设置坐标轴位置
ax = mp.gca()
axis_b = ax.spines['bottom']
axis_b.set_position(('data', 0))
axis_l = ax.spines['left']
axis_l.set_position(('data', 0))
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# 特殊点
mp.scatter([-np.pi/2,np.pi/2], [0, 0],
   s=[100,200], marker='*', edgecolor='red',
   facecolor='green', zorder=30)

# 添加备注
mp.annotate(r'$sin(\frac{\pi}{2})=0}$',xy=(np.pi/2,0),xycoords='data',
            xytext=(20,20),textcoords='offset points',fontsize=14,arrowprops=dict(arrowstyle='simple',
            connectionstyle='arc3,rad=.2'))

# Add legend to the plot
mp.legend(handles=[line1, line2], loc='upper left', fontsize=12, frameon=True)

mp.show()