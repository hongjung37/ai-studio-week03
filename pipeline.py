import pandas as pd  # pandas 불러오기

sales_summary = {}  

with open("RAW_DATA.csv", "r", encoding="cp949") as file:   # UTF-8 로 읽으면 한글 깨짐, cp949로 읽어야 함
    df = pd.read_csv(file) 
    #print(df.shape) #(500, 5)
    #print(df.info())  
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

# 정제 및 파생
df["월"] = pd.to_datetime(df["주문일자"], format="%Y-%m-%d").dt.month #월만 추출
df["단가"] = ( pd.to_numeric( df["단가"].astype(str).str.replace(",", "", regex=False), errors="coerce").astype("Int64")) # , 제거 후 정수형으로 변환
df["총액"] = df["단가"] * df["수량"] # 총액 열 추가

#추가 후 info 확인 (정상적으로 단가가 정제 및 월 ,총액 열 생성 확인)
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   주문일자    500 non-null    str  
 1   상품명     500 non-null    str  
 2   카테고리    500 non-null    str  
 3   단가      500 non-null    Int64
 4   수량      500 non-null    int64
 5   월       500 non-null    int32
 6   총액      500 non-null    Int64
dtypes: Int64(2), int32(1), int64(1), str(3)
memory usage: 26.5 KB
None"""