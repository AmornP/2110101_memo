import numpy as np

def eq(A, B, p):
    # A และ B เป็นอาเรย์ที่มีขนาดเท่ากัน (กี่มิติก็ได ้), p เป็นจ านวนระหว่าง 0 ถึง 100
    # คืน True ถ้าข ้อมูลใน A กับใน B ที่ต าแหน่งเดียวกันมีค่าเท่ากันอย่างน้อยร้อยละ p ของจ านวนชอ่ งทัง้หมด
    # ถ้ามีไม่ถึงก็คืน False
    x = A == B
    n = np.size(A)
    d = np.sum(x)
    return (d/n) * 100 >= p

def closest_point_indexes(points, p):
    x = points[:,0]
    y = points[:,1]
    dx = x - p[0]
    dy = y - p[1]
    d = ( dx**2 + dy**2 ) ** 0.5
    min_ = np.min(d)
    indexer = np.arange(0,x.shape[0],1)
    return indexer[d == min_]
def number_of_inversions(A):
    # A เป็นอาเรย์หนึ่งมิติเก็บจ านวนเต็ม
    # คืน จ านวนคู่ข ้อมูลใน A ที่ตัวทางซา้ยมากกวา่ ตัวขวา
    # (คือมีข ้อมูล A[i] กับ A[j] ที่ i < j แต่ A[i] > A[j] อยู่กี่คู่)
    # เชน่ [1 2 9 4 8 7] มี4 คู่คือ 9 กับ 4, 9 กับ 8, 9 กับ 7 และ 8 กับ 7
    # [9 7 5 3 2] มี 10 คู่ เพราะทกุ คมู่ ตี ัวซา้ยมากกวาตัวขว ่ า ในขณะที่ [2 4 6 8] มี 0 คู่
    x = A > A.reshape((-1,1))
    return np.sum(np.tril(x))
    # s = 0 # sol 2th Cr. Worralop
    # for i in range(A.shape[0]) :
    #     s += np.sum(A[i+1:] < A[i])
    # return s

exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ