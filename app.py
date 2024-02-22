import streamlit as st
from openai import OpenAI
import os

# Streamlitのユーザインターフェースを設定
st.title("OpenAIの音声合成デモ")
user_input = st.text_area("テキストを入力してください", "", height=200)

# 利用可能な声のリスト
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

# ユーザーが声を選択
selected_voice = st.radio("声を選択してください", voices)

api_key = os.environ["OPENAI_API_KEY"]

# ユーザがテキストを入力し、Enterを押したら処理を開始
if st.button('音声合成'):
    if user_input:
        try:
            # OpenAIクライアントの初期化
            client = OpenAI(api_key=api_key)

            # 音声合成リクエストの送信
            response = client.audio.speech.create(
                model="tts-1",
                voice=selected_voice,
                input=user_input,
            )

            # 結果をファイルに保存
            output_file = "output.mp3"
            response.stream_to_file(output_file)

            # ユーザに音声ファイルをダウンロードするオプションを提供
            st.audio(output_file)
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("テキストを入力してください。")
        
        
        
        