import streamlit as st
# import streamlit_authenticator as stauth
from webui_pages.utils import *
from streamlit_option_menu import option_menu
from webui_pages.dialogue.dialogue import dialogue_page, chat_box
from webui_pages.knowledge_base.knowledge_base import knowledge_base_page
import os
import sys
from configs import VERSION
from server.utils import api_address


api = ApiRequest(base_url=api_address())

if __name__ == "__main__":
    is_lite = "lite" in sys.argv 
    
    st.set_page_config(
            "Langchain-Chatchat WebUI",
            os.path.join("img", "chatchat_icon_blue_square_v2.png"),
            initial_sidebar_state="expanded",
            menu_items={
                'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',
                'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",
                'About': f"""欢迎使用 Langchain-Chatchat WebUI {VERSION}！"""
            }
        )
    
 #    names = ['管理员'] # 用户名
 #    usernames = ['admin']  # 登录名
 #    passwords = ['123456']  #登录密码
 #    # 对密码进行加密操作，后续将这个存放在credentials中
 #    hashed_passwords = stauth.Hasher(passwords).generate() 
     
	# # 定义字典，初始化字典
 #    credentials = {'usernames': {}}    
 #    # 生成服务器端的用户身份凭证信息  
 #    for i in range(0, len(names)):  
 #        credentials['usernames'][usernames[i]] = {'name': names[i], 'password': hashed_passwords[i]}  
 #    authenticator = stauth.Authenticate(credentials, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=0)  
 #    name, authentication_status, username = authenticator.login('main')  
    
    # if authentication_status:  # 登录成功
        # is_lite = "lite" in sys.argv  
        # st.set_page_config(
        #     "Langchain-Chatchat WebUI",
        #     os.path.join("img", "chatchat_icon_blue_square_v2.png"),
        #     initial_sidebar_state="expanded",
        #     menu_items={
        #         'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',
        #         'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",
        #         'About': f"""欢迎使用 Langchain-Chatchat WebUI {VERSION}！"""
        #     }
        # )
    
    pages = {
        "对话": {
            "icon": "chat",
            "func": dialogue_page,
        },
        "语料库管理": {
            "icon": "hdd-stack",
            "func": knowledge_base_page,
        },
    }

    with st.sidebar:
        st.image(
            os.path.join(
                "img",
                # "logo-long-chatchat-trans-v2.png"
                "logo6.png"
            ),
            use_column_width=True
        )
        st.caption(
            # f"""<p align="right">当前版本：{VERSION}</p>""",
            f""" """,
            unsafe_allow_html=True,
        )
        options = list(pages)
        icons = [x["icon"] for x in pages.values()]

        default_index = 0
        selected_page = option_menu(
            "",
            options=options,
            icons=icons,
            # menu_icon="chat-quote",
            default_index=default_index,
        )

    if selected_page in pages:
        pages[selected_page]["func"](api=api, is_lite=is_lite)
    # elif authentication_status == False:  #登录失败
    #     st.error('Username/password is incorrect')  
    # elif authentication_status == None:  #未输入登录信息
    #     st.warning('请输入账号密码')
