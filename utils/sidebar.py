import streamlit as st
from streamlit_option_menu import option_menu

def create_sidebar():
    '''사이드바 생성'''
    with st.sidebar:
        choose = option_menu("Project", ["Home", "News", "U.S. Stock"],
                            icons=['house', 'newspaper', 'kanban'],
                            menu_icon="diagram-3", default_index=0,
                            styles={
                                "container": {"padding": "5!important", "background-color": "#FAFAFA"},
                                "icon": {"color": "orange", "font-size": "25px"},
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "#02AB21"},
                            }
                            )
        # News 메뉴 선택 시
        if choose == "News":
            st.session_state.show_news_buttons = True
        else:
            st.session_state.show_news_buttons = False
        # 하위 버튼 추가
        if st.session_state.get("show_news_buttons", False):
            with st.sidebar:
                sub_choose = option_menu("News", ["Politics", "Economy", "Society", "Culture/Lifestyle", "IT/Science", "World"],
                                    icons=['bookmark-fill', 'bookmark-fill', 'bookmark-fill', 'bookmark-fill', 'bookmark-fill', 'bookmark-fill'],
                                    menu_icon="newspaper", default_index=0,
                                    styles={
                                        "container": {"padding": "5!important", "background-color": "#FAFAFA"},
                                        "icon": {"color": "orange", "font-size": "25px"},
                                        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                                        "nav-link-selected": {"background-color": "#02AB21"},
                                }
                                )

        if choose == "U.S. Stock":
            st.session_state.show_news_buttons = True
        else:
            st.session_state.show_news_buttons = False
        # 하위 버튼 추가
        if st.session_state.get("show_news_buttons", False):
            with st.sidebar:
                sub_choose = option_menu("U.S. Stock", ["S&P 500", "NASDAQ", "Dow Jones"],
                                    icons=['bookmark-fill', 'bookmark-fill', 'bookmark-fill'],
                                    menu_icon="kanban", default_index=0,
                                    styles={
                                        "container": {"padding": "5!important", "background-color": "#FAFAFA"},
                                        "icon": {"color": "orange", "font-size": "25px"},
                                        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                                        "nav-link-selected": {"background-color": "#02AB21"},
                                    }
                                    )
        if choose == "Home":
            sub_choose = "Home"
        
    return sub_choose
