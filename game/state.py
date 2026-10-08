import streamlit as st
import pandas as pd

def init_game_state():
    if "current_round" not in st.session_state:
        st.session_state.current_round = 1
    if "chaos_score" not in st.session_state:
        st.session_state.chaos_score = 0
    if "defender_score" not in st.session_state:
        st.session_state.defender_score = 0
    if "game_logs" not in st.session_state:
        st.session_state.game_logs = []
    if "chaos_hp" not in st.session_state:
        st.session_state.chaos_hp = 100
    if "defender_hp" not in st.session_state:
        st.session_state.defender_hp = 100

def log_round_data(round_num, topic, chaos_action, defender_action, true_prob, defender_pred, points_gained):
    log_entry = {
        "Round": round_num,
        "Topic": topic,
        "Chaos_Action": str(chaos_action),
        "Defender_Action": str(defender_action),
        "True_Probability": round(true_prob, 4),
        "Defender_Prediction": round(defender_pred, 4),
        "Prediction_Error": round(abs(true_prob - defender_pred), 4),
        "Points_Awarded": points_gained
    }
    st.session_state.game_logs.append(log_entry)

def get_logs_df():
    return pd.DataFrame(st.session_state.game_logs)