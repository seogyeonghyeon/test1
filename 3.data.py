# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd


st.title('Unit 3. Data display elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/data')

st.header(' 1. Metric')
st.metric(label="Temperature", value="30.5 °C", delta="2.5 °C")
st.metric(label="Temperature", value="28 °C", delta="-2.5 °C")



st.header('2. columns')
col1, col2, col3 = st.columns(3) 
col1.metric("기온", "30.5 °C", "2.5 °C")
col2.metric("풍속", "9 mph", "-8%")
col3.metric("습도", "86%", "4%")





st.header('3. Dataframe 조회하기')

# 파일 위치- https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv
titanic = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv')


st.markdown('- st.dataframe(상위 15행)')
st.caption('dataframe, write- 10개 행  기준 스크롤, 열 크기조정, 열 정렬, 테이블  확대')
st.dataframe(titanic.head(15))

st.markdown('- st.write(상위 15행)')
st.write(titanic.head(15))

st.markdown('- st.table(상위 15행)')
st.caption('table- 형태 고정')
st.table(titanic.head(15))

st.header('4. Dataframe 수정하기')
st.markdown('- st.experimental_data_editor(df)')
edited_titanic = st.experimental_data_editor(titanic)

# 버튼을 누르면 수정한 결과가 새로운 csv 파일에 저장
if st.button('Press button to Save titanic2.csv'):
    edited_titanic.to_csv('streamlit/titanic2.csv')
    st.write('💾 Saved')


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\3.data.py