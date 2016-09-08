#coding: utf-8
"""
符号化領域を求めるプログラム
不均衡$d$を考慮して符号化領域を作成する
"""

import numpy as np
import math
import auxiliary as ax

def ask_trans_vertex(adjust_matrix) :
    """隣接行列を受け取り、隣接行列から各頂点の書き込み可能領域の大きさを求める"""

    #頂点数を求める
    v_num = int(math.sqrt(adjust_matrix.size))
    trans_able_size_table = np.zeros([v_num,2])
    not_define_list = range(v_num)
    define_list = []
    temp_list = []
    
    #リーフ(すべての値が0である列を探す)の書き込み可能領域から求めていく
    leaf_list = ax.ask_leaf(adjust_matrix)

    
            
    #リーフの書き込み可能領域(1)は決まったので、未定義リストから削除
    for i in leaf_list :
        trans_able_size_table[i][1] = 1
        not_define_list.remove(i)


    #すでに書き込み可能領域が定義されている頂点のみに遷移可能な頂点の書き込み可能領域を求める

    while len(not_define_list) > 0 :
        forcus_list = []
        for i in not_define_list :
            """すでに書き込み可能領域のサイズが定義されているもののみに有向辺を持つ頂点を求める"""
            match_count = 0
            for j in not_define_list :
                if adjust_matrix[i][j] == 0 :
                    match_count += 1

                else :
                    break

            if match_count == len(not_define_list) :
                focus_list.append(i)        

    
        for i in range focus_list :
            trans_able_size_table[i][1] = ax.ask_focus_vertex_trans_able(i,trans_able_size_table,adjust_matrix)

            not_define_list.remove(i)

            
    return trans_able_size_table

    
    

if __name__ == '__main__':
    """メイン文"""
    a = np.zeros([3,3])
    a[1][0] = 1
    print 'a = ',a
    ask_trans_vertex(a)

    for i in range(3) :
        print i
