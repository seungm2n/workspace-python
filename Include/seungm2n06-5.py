# seungm2n06-5
'''
    6. Dataframe
        - index 행
        - columns 열
        - 데이터 선택 (slicing)
            - 데이터 위치를 활용한 데이터 가공 : loc(), iloc()
        - 데이터 삭제 (drop)
            - 필요없는 데이터 삭제
            - 행(index), 열(column) 단위로 삭제
        - 중복 데이터 삭제 (duplicated(), drop_duplicates())
        
'''
import pandas as pd

df = pd.DataFrame()
print(type(df))

stu_list = ['Susan', 'Jessica', 'John', 'Michael']
