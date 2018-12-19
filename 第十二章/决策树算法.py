import numpy as np
from pandas import DataFrame, Series
from math import log2
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



def cal_shannon(frame):
    val_count = frame.iloc[:, -1].value_counts()
    pct_val = val_count / val_count.sum()
    log_pct = pct_val.map(np.log2)
    shannon_ent = -(pct_val * log_pct).sum()
    return shannon_ent


def bfts(frame):
    fea_num = frame.shape[1] - 1
    ent_ser = Series([])
    for i in range(fea_num):
        ent_ser[i] = frame.groupby(frame.iloc[:, i]).apply(cal_shannon).sum()
    best_features_tosplit = ent_ser.argsort()[0]
    return best_features_tosplit


def create_tree(frame, labels):
    if len(frame.iloc[:, -1].unique()) == 1:
        return frame.iloc[0, -1]
    if frame.shape[1] == 1:
        return frame.iloc[:, -1].value_counts().index[0]
    bestfeat = bfts(frame)
    bestfeatlabel = labels[bestfeat]
    mytree = {bestfeatlabel: {}}
    del (labels[bestfeat])
    unique_values = frame.iloc[:, bestfeat].unique()
    for value in unique_values:
        sublabels = labels
        subframe = frame[frame.iloc[:, bestfeat] == value].drop(frame.columns[bestfeat], axis=1)
        mytree[bestfeatlabel][value] = create_tree(subframe, sublabels)
    return mytree


#绘制决策
def get_num_leafs(decision_tree):
    num_leafs = 0
    first_str = next(iter(decision_tree))
    second_dict = decision_tree[first_str]
    for k in second_dict.keys():
        if isinstance(second_dict[k], dict):
            num_leafs += get_num_leafs(second_dict[k])
        else:
            num_leafs += 1
    return num_leafs

# 获取树的深度
def get_tree_depth(decision_tree):
    max_depth = 0
    first_str = next(iter(decision_tree))
    second_dict = decision_tree[first_str]
    for k in second_dict.keys():
        if isinstance(second_dict[k], dict):
            this_depth = 1 + get_tree_depth(second_dict[k])
        else:
            this_depth = 1
        if this_depth > max_depth:
            max_depth = this_depth
    return max_depth

# 绘制节点
def plot_node(node_txt, center_pt, parent_pt, node_type):
    arrow_args = dict(arrowstyle='<-')
    font = FontProperties(fname=r'C:\Windows\Fonts\simkai.TTF', size=15)
    create_plot.ax1.annotate(node_txt, xy=parent_pt,  xycoords='axes fraction', xytext=center_pt,
                            textcoords='axes fraction', va="center", ha="center", bbox=node_type,
                            arrowprops=arrow_args, FontProperties=font)

# 标注划分属性
def plot_mid_text(cntr_pt, parent_pt, txt_str):
    font = FontProperties(fname=r'C:\Windows\Fonts\simsun.TTC', size=10)
    x_mid = (parent_pt[0] - cntr_pt[0]) / 2.0 + cntr_pt[0]
    y_mid = (parent_pt[1] - cntr_pt[1]) / 2.0 + cntr_pt[1]
    create_plot.ax1.text(x_mid, y_mid, txt_str, va="center", ha="center", color='red', FontProperties=font)

# 绘制决策树
def plot_tree(decision_tree, parent_pt, node_txt):
    d_node = dict(boxstyle="sawtooth", fc="0.8")
    leaf_node = dict(boxstyle="round4", fc='0.8')
    num_leafs = get_num_leafs(decision_tree)
    first_str = next(iter(decision_tree))
    cntr_pt = (plot_tree.xoff + (1.0 +float(num_leafs))/2.0/plot_tree.totalW, plot_tree.yoff)
    plot_mid_text(cntr_pt, parent_pt, node_txt)
    plot_node(first_str, cntr_pt, parent_pt, d_node)
    second_dict = decision_tree[first_str]
    plot_tree.yoff = plot_tree.yoff - 1.0/plot_tree.totalD
    for k in second_dict.keys():
        if isinstance(second_dict[k], dict):
            plot_tree(second_dict[k], cntr_pt, k)
        else:
            plot_tree.xoff = plot_tree.xoff + 1.0/plot_tree.totalW
            plot_node(second_dict[k], (plot_tree.xoff, plot_tree.yoff), cntr_pt, leaf_node)
            plot_mid_text((plot_tree.xoff, plot_tree.yoff), cntr_pt, k)
    plot_tree.yoff = plot_tree.yoff + 1.0/plot_tree.totalD

def create_plot(dtree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    create_plot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plot_tree.totalW = float(get_num_leafs(dtree))
    plot_tree.totalD = float(get_tree_depth(dtree))
    plot_tree.xoff = -0.5/plot_tree.totalW
    plot_tree.yoff = 1.0
    plot_tree(dtree, (0.5, 1.0), '')
    plt.show()


frame = DataFrame([[1, 1, 'yes'],
                   [1, 1, 'yes'],
                   [1, 0, 'no'],
                   [0, 1, 'no'],
                   [0, 1, 'no']])
labels = ['no surfacing', 'flippers']
decision_tree=create_tree(frame, labels)
#print( create_tree(frame, labels))

create_plot(decision_tree)
