
import sqlite3
from pathlib import Path
import hashlib
import time
import numpy as np
import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

APP_TITLE = "DDoS Attack Detection System"
DATA_PATH = Path(__file__).with_name("ddos_dataset.csv")
DB_PATH = Path(__file__).with_name("users.db")

def hash_pwd(pwd, salt="yanecode"):
    return hashlib.sha256((salt + pwd).encode()).hexdigest()

def init_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)")
    con.commit()
    try:
        cur.execute("INSERT INTO users VALUES (?,?)", ("admin", hash_pwd("admin")))
    except:
        pass
    con.commit()
    con.close()

def check_login(user, pwd):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT password FROM users WHERE username=?", (user,))
    row = cur.fetchone()
    con.close()
    return row and row[0] == hash_pwd(pwd)

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_resource
def train_model(df):
    X = df.drop("label", axis=1)
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=200, random_state=42))
    ])

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    y_proba = pipe.predict_proba(X_test)[:,1]

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_proba),
        "cm": confusion_matrix(y_test, y_pred)
    }
    return pipe, metrics

def main():
    st.set_page_config(layout="wide")
    init_db()
    st.title(APP_TITLE)

    if "auth" not in st.session_state:
        st.session_state.auth = False

    if not st.session_state.auth:
        with st.form("login"):
            user = st.text_input("Username")
            pwd = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                if check_login(user, pwd):
                    st.session_state.auth = True
                    st.success("Login successful")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Invalid credentials")
        return

    df = load_data()
    model, metrics = train_model(df)

    page = st.sidebar.radio("Navigation", ["Dashboard", "Test", "Dataset"])

    if page == "Dashboard":
        for k,v in metrics.items():
            if k!="cm":
                st.metric(k, f"{v:.3f}")
        st.write("Confusion Matrix")
        st.write(metrics["cm"])

    elif page == "Test":
        inputs = {}
        for col in df.columns[:-1]:
            inputs[col] = st.number_input(col, value=float(df[col].mean()))
        if st.button("Predict"):
            input_df = pd.DataFrame([inputs])
            proba = model.predict_proba(input_df)[0][1]
            pred = model.predict(input_df)[0]
            if pred == 1:
                st.error(f"DDoS Attack Detected (prob={proba:.2f})")
            else:
                st.success(f"Normal Traffic (prob={proba:.2f})")

    else:
        st.dataframe(df.head(50))

if __name__ == "__main__":
    main()
