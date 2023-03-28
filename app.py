import streamlit as st
import streamlit.components.v1 as components
import openai

# OPEN AI API KEY
openai.api_key = st.secrets['api_key']

st.set_page_config(
    page_title = "言いなりA-Frame",
#     page_icon = Image.open("favicon.png")
)

if 'a_code' not in st.session_state:
    st.session_state['a_code'] = "<a-scene></a-scene>"

def get_a_frame(order, code):
    PROMPT = f"""
    `下記の指示を実現するA-Frameのa-から始まる要素をコードに追加・修正。ただし下記の条件を満たすこと。
    コード: {code}
    条件:
    - 現在のシーンを踏まえること。
    - a-camera,a-assets,a-animation,a-lightは使用しない。
    - scriptを使用しない。
    - 背景の設定にbackgroundコンポーネントではなくa-sky>を使用。
    - 結果はコードブロックに記述。
    指示： `{order}`
    """
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": PROMPT},
        ]
    )
    code = res.choices[0]['message']['content']
    return code

def make_html(a_code):
    html = f"""
    <html><head>
    <script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>
    <script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>
    <script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script>
    </head><body>
    {a_code}
    </body></html>
    """
    return html

# Layout
st.sidebar.title("ChatGPT で A-Frame")
order = st.sidebar.text_area("**指示を入力してください :**")
if st.sidebar.button('**生成・修正**') and order:
    a_code = get_a_frame(order, st.session_state['a_code'])
    st.session_state['a_code'] = a_code
    st.code(a_code, language='html')
    html = make_html(a_code)
    components.html(html, height=720)
