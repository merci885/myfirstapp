import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="📚 MBTI 고전 책 추천",
    page_icon="📚",
    layout="centered"
)

# 사용자 정의 CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        color: #4A90E2;
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    .description {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        padding: 0 1rem;
    }
    
    .book-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #4A90E2;
    }
    
    .book-title {
        color: #2c3e50;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .book-author {
        color: #7f8c8d;
        font-size: 1rem;
        margin-bottom: 0.8rem;
    }
    
    .book-description {
        color: #34495e;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    .mbti-badge {
        background: #4A90E2;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9rem;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    .select-container {
        margin: 2rem 0;
    }
    
    .footer {
        text-align: center;
        color: #95a5a6;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# MBTI별 책 추천 데이터
book_recommendations = {
    "INTJ": [
        {
            "title": "1984",
            "author": "조지 오웰",
            "description": "체계적이고 미래지향적인 사고를 가진 INTJ에게 완벽한 디스토피아 소설입니다. 권력과 통제에 대한 깊이 있는 분석이 전략적 사고를 자극할 것입니다."
        },
        {
            "title": "파우스트",
            "author": "괴테",
            "description": "지식에 대한 갈망과 인간 본성에 대한 철학적 탐구가 담긴 작품으로, 완벽주의적 성향의 INTJ가 깊이 공감할 수 있습니다."
        },
        {
            "title": "죄와 벌",
            "author": "도스토예프스키",
            "description": "도덕적 딜레마와 인간 심리의 복잡성을 다룬 작품으로, 분석적 사고를 즐기는 INTJ에게 지적 자극을 제공합니다."
        }
    ],
    "INTP": [
        {
            "title": "이상한 나라의 앨리스",
            "author": "루이스 캐럴",
            "description": "논리와 모순이 공존하는 환상적인 세계로, 창의적이고 논리적인 사고를 즐기는 INTP의 호기심을 자극합니다."
        },
        {
            "title": "소크라테스의 변명",
            "author": "플라톤",
            "description": "철학적 사고와 질문하는 자세의 중요성을 강조하는 작품으로, 진리 탐구를 좋아하는 INTP에게 이상적입니다."
        },
        {
            "title": "걸리버 여행기",
            "author": "조나단 스위프트",
            "description": "사회 비판과 인간 본성에 대한 날카로운 관찰이 담긴 작품으로, 독립적 사고를 즐기는 INTP에게 적합합니다."
        }
    ],
    "ENTJ": [
        {
            "title": "군주론",
            "author": "마키아벨리",
            "description": "리더십과 권력에 대한 실용적 접근이 담긴 고전으로, 지도력을 추구하는 ENTJ에게 통찰력을 제공합니다."
        },
        {
            "title": "전쟁과 평화",
            "author": "톨스토이",
            "description": "거대한 스케일의 서사와 인간 드라마를 통해 리더십과 역사의 흐름을 다룬 작품으로, 야심찬 ENTJ에게 영감을 줍니다."
        },
        {
            "title": "햄릿",
            "author": "셰익스피어",
            "description": "복잡한 정치적 상황과 결단력 있는 행동에 대한 탐구가 담긴 작품으로, 전략적 사고를 중시하는 ENTJ에게 적합합니다."
        }
    ],
    "ENTP": [
        {
            "title": "돈키호테",
            "author": "미겔 데 세르반테스",
            "description": "창의적이고 모험적인 정신이 담긴 작품으로, 새로운 아이디어를 추구하는 ENTP의 성향과 완벽하게 일치합니다."
        },
        {
            "title": "캔디드",
            "author": "볼테르",
            "description": "기존 관념에 도전하고 날카로운 위트가 담긴 철학 소설로, 토론과 논쟁을 즐기는 ENTP에게 이상적입니다."
        },
        {
            "title": "한여름 밤의 꿈",
            "author": "셰익스피어",
            "description": "상상력과 유머가 가득한 환상적인 작품으로, 창의적이고 유연한 사고를 가진 ENTP에게 재미와 영감을 제공합니다."
        }
    ],
    "INFJ": [
        {
            "title": "데미안",
            "author": "헤르만 헤세",
            "description": "자아 발견과 내적 성장에 대한 깊이 있는 탐구가 담긴 작품으로, 내향적이고 직관적인 INFJ에게 큰 공감을 불러일으킵니다."
        },
        {
            "title": "제인 에어",
            "author": "샬롯 브론테",
            "description": "독립적인 여성의 내적 여정과 도덕적 가치를 다룬 작품으로, 이상주의적 성향의 INFJ가 깊이 공감할 수 있습니다."
        },
        {
            "title": "레 미제라블",
            "author": "빅토르 위고",
            "description": "인간애와 사회 정의에 대한 깊은 통찰이 담긴 작품으로, 인류애를 중시하는 INFJ의 가치관과 일치합니다."
        }
    ],
    "INFP": [
        {
            "title": "어린 왕자",
            "author": "앙투안 드 생텍쥐페리",
            "description": "순수함과 진정한 가치에 대한 아름다운 이야기로, 감성적이고 이상주의적인 INFP에게 깊은 감동을 선사합니다."
        },
        {
            "title": "폭풍의 언덕",
            "author": "에밀리 브론테",
            "description": "강렬한 감정과 내적 갈등이 담긴 작품으로, 감정의 깊이를 이해하는 INFP가 공감할 수 있는 소설입니다."
        },
        {
            "title": "월든",
            "author": "헨리 데이비드 소로",
            "description": "자연과 단순한 삶에 대한 철학적 성찰이 담긴 작품으로, 개인적 가치를 중시하는 INFP에게 영감을 제공합니다."
        }
    ],
    "ENFJ": [
        {
            "title": "앵무새 죽이기",
            "author": "하퍼 리",
            "description": "사회 정의와 인간 존엄성에 대한 깊은 메시지가 담긴 작품으로, 타인을 돕고자 하는 ENFJ의 가치관과 일치합니다."
        },
        {
            "title": "크리스마스 캐럴",
            "author": "찰스 디킨스",
            "description": "인간 변화와 선행의 중요성을 다룬 감동적인 작품으로, 따뜻한 마음을 가진 ENFJ에게 영감을 줍니다."
        },
        {
            "title": "오만과 편견",
            "author": "제인 오스틴",
            "description": "인간관계와 사회적 상호작용에 대한 예리한 관찰이 담긴 작품으로, 사교적인 ENFJ가 즐길 수 있습니다."
        }
    ],
    "ENFP": [
        {
            "title": "안네의 일기",
            "author": "안네 프랑크",
            "description": "희망과 긍정적 에너지가 가득한 작품으로, 낙관적이고 감정 표현이 풍부한 ENFP에게 큰 영감을 제공합니다."
        },
        {
            "title": "톰 소여의 모험",
            "author": "마크 트웨인",
            "description": "자유로운 모험 정신과 창의적 상상력이 담긴 작품으로, 활동적이고 모험을 좋아하는 ENFP에게 완벽합니다."
        },
        {
            "title": "위대한 개츠비",
            "author": "F. 스콧 피츠제럴드",
            "description": "꿈과 이상에 대한 추구가 담긴 작품으로, 가능성을 믿고 열정적인 ENFP의 성향과 잘 맞습니다."
        }
    ],
    "ISTJ": [
        {
            "title": "오디세이",
            "author": "호메로스",
            "description": "전통적 가치와 끈기 있는 여정이 담긴 고전으로, 책임감 있고 성실한 ISTJ에게 깊은 의미를 제공합니다."
        },
        {
            "title": "로빈슨 크루소",
            "author": "다니엘 디포",
            "description": "실용적 해결책과 체계적 접근이 돋보이는 작품으로, 현실적이고 계획적인 ISTJ가 공감할 수 있습니다."
        },
        {
            "title": "멋진 신세계",
            "author": "올더스 헉슬리",
            "description": "사회 질서와 안정성에 대한 탐구가 담긴 작품으로, 구조와 질서를 중시하는 ISTJ에게 흥미로운 관점을 제공합니다."
        }
    ],
    "ISFJ": [
        {
            "title": "작은 아씨들",
            "author": "루이자 메이 올컷",
            "description": "가족애와 희생 정신이 아름답게 그려진 작품으로, 타인을 배려하는 따뜻한 마음의 ISFJ에게 완벽합니다."
        },
        {
            "title": "비밀의 화원",
            "author": "프랜시스 호지슨 버넷",
            "description": "치유와 보살핌의 이야기가 담긴 작품으로, 돌봄을 중시하는 ISFJ의 성향과 잘 어울립니다."
        },
        {
            "title": "샬롯의 거미줄",
            "author": "E.B. 화이트",
            "description": "우정과 희생에 대한 감동적인 이야기로, 헌신적이고 충성스러운 ISFJ에게 깊은 감명을 줍니다."
        }
    ],
    "ESTJ": [
        {
            "title": "백 년의 고독",
            "author": "가브리엘 가르시아 마르케스",
            "description": "가족의 역사와 전통에 대한 방대한 서사로, 조직적이고 전통을 중시하는 ESTJ에게 의미 있는 작품입니다."
        },
        {
            "title": "모비딕",
            "author": "허먼 멜빌",
            "description": "목표 달성에 대한 강인한 의지와 리더십이 그려진 작품으로, 결단력 있는 ESTJ가 감명받을 수 있습니다."
        },
        {
            "title": "호밀밭의 파수꾼",
            "author": "J.D. 샐린저",
            "description": "사회적 책임과 성인으로서의 역할에 대한 성찰이 담긴 작품으로, 책임감 있는 ESTJ에게 통찰력을 제공합니다."
        }
    ],
    "ESFJ": [
        {
            "title": "센스 앤 센서빌리티",
            "author": "제인 오스틴",
            "description": "가족 관계와 사회적 조화에 대한 섬세한 묘사가 담긴 작품으로, 사교적이고 배려심 깊은 ESFJ에게 적합합니다."
        },
        {
            "title": "크리스마스 캐럴",
            "author": "�찰스 디킨스",
            "description": "공동체 정신과 나눔의 가치를 강조하는 작품으로, 따뜻한 마음을 가진 ESFJ에게 큰 감동을 줍니다."
        },
        {
            "title": "폴리아나",
            "author": "엘리너 포터",
            "description": "긍정적 태도와 타인에 대한 배려가 돋보이는 작품으로, 낙관적이고 사교적인 ESFJ의 성향과 잘 맞습니다."
        }
    ],
    "ISTP": [
        {
            "title": "노인과 바다",
            "author": "어니스트 헤밍웨이",
            "description": "간결하고 실용적인 문체로 개인의 도전과 기술을 다룬 작품으로, 독립적이고 실용적인 ISTP에게 완벽합니다."
        },
        {
            "title": "2001: 스페이스 오디세이",
            "author": "아서 C. 클라크",
            "description": "기술과 논리적 사고가 중심이 되는 SF 고전으로, 분석적이고 기술적 사고를 즐기는 ISTP에게 흥미로운 작품입니다."
        },
        {
            "title": "보물섬",
            "author": "로버트 루이스 스티븐슨",
            "description": "모험과 실용적 문제해결이 돋보이는 작품으로, 행동 중심적이고 현실적인 ISTP가 즐길 수 있습니다."
        }
    ],
    "ISFP": [
        {
            "title": "시드하르타",
            "author": "헤르만 헤세",
            "description": "개인적 여정과 내적 평화에 대한 아름다운 탐구가 담긴 작품으로, 예술적 감성과 개인적 가치를 중시하는 ISFP에게 이상적입니다."
        },
        {
            "title": "빨간 머리 앤",
            "author": "L.M. 몽고메리",
            "description": "상상력과 자연에 대한 사랑이 가득한 작품으로, 감성적이고 창의적인 ISFP의 마음을 따뜻하게 해줍니다."
        },
        {
            "title": "차라투스트라는 이렇게 말했다",
            "author": "프리드리히 니체",
            "description": "개인적 가치와 자기 실현에 대한 철학적 성찰이 담긴 작품으로, 독립적이고 개성적인 ISFP에게 영감을 제공합니다."
        }
    ],
    "ESTP": [
        {
            "title": "삼총사",
            "author": "알렉상드르 뒤마",
            "description": "모험과 액션이 가득한 흥미진진한 작품으로, 활동적이고 현재 순간을 즐기는 ESTP에게 완벽한 엔터테인먼트를 제공합니다."
        },
        {
            "title": "바람과 함께 사라지다",
            "author": "마거릿 미첼",
            "description": "강인한 주인공과 역동적인 시대 배경이 돋보이는 작품으로, 도전을 즐기는 ESTP의 성향과 잘 맞습니다."
        },
        {
            "title": "카운트 오브 몬테크리스토",
            "author": "알렉상드르 뒤마",
            "description": "복수와 모험이 얽힌 스릴 넘치는 작품으로, 스릴을 추구하고 행동 중심적인 ESTP가 몰입할 수 있습니다."
        }
    ],
    "ESFP": [
        {
            "title": "이상한 나라의 앨리스",
            "author": "루이스 캐럴",
            "description": "상상력과 즐거움이 가득한 환상적인 작품으로, 창의적이고 재미를 추구하는 ESFP에게 완벽한 모험을 선사합니다."
        },
        {
            "title": "마담 보바리",
            "author": "귀스타브 플로베르",
            "description": "감정과 로맨스에 대한 생생한 묘사가 담긴 작품으로, 감성적이고 사교적인 ESFP가 공감할 수 있습니다."
        },
        {
            "title": "프랑켄슈타인",
            "author": "메리 셸리",
            "description": "인간 감정과 드라마틱한 상황이 어우러진 작품으로, 감정 표현이 풍부하고 창의적인 ESFP에게 흥미로운 경험을 제공합니다."
        }
    ]
}

# 메인 헤더
st.markdown('<h1 class="main-header">📚 MBTI 고전 책 추천</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">당신의 성격 유형에 맞는 완벽한 고전 문학을 찾아보세요!</p>', unsafe_allow_html=True)

# MBTI 선택
st.markdown('<div class="select-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    mbti_types = list(book_recommendations.keys())
    selected_mbti = st.selectbox(
        "🎯 당신의 MBTI를 선택해주세요:",
        ["선택해주세요"] + mbti_types,
        help="16가지 MBTI 유형 중 하나를 선택하면 맞춤형 고전 책을 추천해드립니다!"
    )

st.markdown('</div>', unsafe_allow_html=True)

# 책 추천 표시
if selected_mbti and selected_mbti != "선택해주세요":
    st.markdown(f'<div class="mbti-badge">{selected_mbti}</div>', unsafe_allow_html=True)
    
    st.markdown("### 📖 추천 고전 도서")
    st.markdown("---")
    
    books = book_recommendations[selected_mbti]
    
    for i, book in enumerate(books):
        st.markdown(f'''
        <div class="book-card">
            <div class="book-title">📚 {book["title"]}</div>
            <div class="book-author">✍️ {book["author"]}</div>
            <div class="book-description">{book["description"]}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # 추가 정보
    st.markdown("---")
    st.markdown("### 💡 왜 이 책들을 추천했나요?")
    
    mbti_descriptions = {
        "INTJ": "전략적이고 독립적인 사고를 가진 INTJ는 복잡한 아이디어와 미래 비전을 다룬 작품을 선호합니다.",
        "INTP": "논리적이고 호기심 많은 INTP는 철학적 사고와 창의적 아이디어를 자극하는 작품을 좋아합니다.",
        "ENTJ": "리더십과 목표 달성을 중시하는 ENTJ는 권력과 전략, 성공에 대한 통찰이 담긴 작품에 끌립니다.",
        "ENTP": "창의적이고 모험을 좋아하는 ENTP는 새로운 아이디어와 도전적인 관점을 제시하는 작품을 선호합니다.",
        "INFJ": "이상주의적이고 통찰력 있는 INFJ는 인간 본성과 내적 성장에 대한 깊은 탐구가 담긴 작품에 공감합니다.",
        "INFP": "감성적이고 개인적 가치를 중시하는 INFP는 순수함과 진정성이 담긴 아름다운 작품을 사랑합니다.",
        "ENFJ": "타인을 돕고 사회적 가치를 중시하는 ENFJ는 인간애와 긍정적 변화를 다룬 작품에 감동받습니다.",
        "ENFP": "열정적이고 낙관적인 ENFP는 희망과 가능성, 모험이 가득한 작품에서 영감을 얻습니다.",
        "ISTJ": "전통과 안정성을 중시하는 ISTJ는 확고한 가치와 체계적인 접근이 돋보이는 작품을 선호합니다.",
        "ISFJ": "배려심 깊고 헌신적인 ISFJ는 가족애와 희생, 돌봄의 가치가 담긴 작품에 깊이 공감합니다.",
        "ESTJ": "조직적이고 책임감 있는 ESTJ는 리더십과 전통적 가치, 목표 달성을 다룬 작품을 좋아합니다.",
        "ESFJ": "사교적이고 따뜻한 ESFJ는 인간관계와 공동체 정신, 조화를 중시하는 작품에 마음이 끌립니다.",
        "ISTP": "실용적이고 독립적인 ISTP는 기술과 논리, 개인적 도전을 다룬 간결한 작품을 선호합니다.",
        "ISFP": "예술적이고 개성적인 ISFP는 아름다움과 개인적 여정, 자연에 대한 사랑이 담긴 작품을 좋아합니다.",
        "ESTP": "활동적이고 현실적인 ESTP는 모험과 액션, 즉시성이 돋보이는 흥미진진한 작품을 선호합니다.",
        "ESFP": "사교적이고 즐거움을 추구하는 ESFP는 감정과 창의성, 재미가 가득한 작품에서 기쁨을 찾습니다."
    }
    
    st.info(f"💭 {mbti_descriptions[selected_mbti]}")

# 푸터
st.markdown('''
<div class="footer">
    <p>📚 고전 문학의 세계로 떠나는 여행을 시작해보세요!</p>
    <p>✨ 책을 통해 새로운 자신을 발견할 수 있을 거예요 ✨</p>
</div>
''', unsafe_allow_html=True)

# 사이드바 정보
with st.sidebar:
    st.markdown("### 📖 MBTI 고전 책 추천")
    st.markdown("---")
    st.markdown("""
    **🎯 이 앱의 특징:**
    - 16가지 MBTI 유형별 맞춤 추천
    - 엄선된 고전 문학 작품
    - 각 책의 추천 이유 설명
    
    **📚 추천 기준:**
    - 성격 유형별 선호도
    - 고전 문학의 가치
    - 읽기 경험의 만족도
    
    **✨ 팁:**
    추천받은 책 중 하나를 선택해서 
    천천히 읽어보세요. 고전은 
    시간을 두고 음미할 때 
    더 깊은 감동을 줍니다.
    """)
    
    st.markdown("---")
    st.markdown("💡 **더 많은 책이 궁금하다면?**")
    st.markdown("같은 MBTI 유형의 추천을 참고하거나, 비슷한 성향의 다른 유형도 확인해보세요!")
