import pandas as pd  # pandas 불러오기

sales_summary = {}  

with open("RAW_DATA.csv", "r", encoding="cp949") as file:   # UTF-8 로 읽으면 한글 깨짐, cp949로 읽어야 함
    df = pd.read_csv(file) 
    print(df.shape) #(500, 5)
    print(df.info())  
"""
<class 'pandas.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   주문일자    500 non-null    str  
 1   상품명     500 non-null    str  
 2   카테고리    500 non-null    str  
 3   단가      500 non-null    str  
 4   수량      500 non-null    int64
dtypes: int64(1), str(4)
memory usage: 19.7 KB
None
"""

print(df.head())  # 데이터 확인
"""
      주문일자   상품명  카테고리     단가  수량
0  2026-01-01  크루아상  베이커리   4500   1
1  2026-01-01    스콘   디저트   4000   3
2  2026-01-01   크로플   디저트  6,000   2
3  2026-01-01  크루아상  베이커리   4500   3
4  2026-01-01  샌드위치  베이커리   7000   1
"""