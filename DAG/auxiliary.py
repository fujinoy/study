#coding: utf-8
"""
符号化領域を求めるプログラム
不均衡$d$を考慮して符号化領域を作成する
"""

import numpy as np
import math

def ask_focus_vertex_trans_able(focus_vertex,table,adjust_matrix) :
    """すでに書き込み可能領域が定義されている頂点とその書き込み可能領域の大きさを格納したtableと隣接行列を使って、forcus_vertexの書き込み可能領域を求める"""

    #頂点自身も書き込み可能領域となる
    v_num = int(math.sqrt(adjust_matrix.size))
    ta = 1

    
    for i in v_num :
        if adjust_matrix[forcus_vertex][i] == 1 :
            ta += table[i][1]

    return ta
