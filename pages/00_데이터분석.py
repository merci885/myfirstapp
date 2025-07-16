import streamlit as st
import pandas as pd
import altair as alt

# 데이터 로드
df = pd.read_csv('countriesMBTI_16types.csv')

st.set_page_config(page_title='국가별 MBTI Top3', page_icon='🌍', layout='centered')

st.title('🌍 국가별 MBTI Top 3 시각화')
st.write('국가를 선택하면 해당 국가에서 비율이 가장 높은 **MBTI 상위 3개 유형**을 시각화해서 보여줍니다.')

# 국가 선택
countries = df['Country'].unique().tolist()
selected_country = st.selectbox('국가를 선택하세요', countries)

if selected_country:
    country_data = df[df['Country'] == selected_country].iloc[0]
    mbti_scores = country_data.drop('Country')
    top3 = mbti_scores.sort_values(ascending=False).head(3)

    top3_df = pd.DataFrame({
        'MBTI': top3.index,
        '비율': top3.values * 100  # 퍼센트로 변환
    })

    st.subheader(f'{selected_country}의 MBTI Top 3')
    chart = alt.Chart(top3_df).mark_bar().encode(
        x=alt.X('MBTI', sort='-y'),
        y='비율',
        color='MBTI'
    ).properties(
        width=500,
        height=300,
        title=f'{selected_country}의 MBTI Top 3 비율 (%)'
    )

    st.altair_chart(chart, use_container_width=True)

    for idx, row in top3_df.iterrows():
        st.write(f"**{row['MBTI']}**: {row['비율']:.2f}%")

st.markdown('---')
st.markdown('📊 **다른 국가도 선택해보세요! MBTI 유형의 흥미로운 분포를 발견할 수 있어요.**')
