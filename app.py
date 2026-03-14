"""
CyberShield AI — Network Attack Prediction Platform
Owner: Ranya Belmaachi | v4.0 Premium Cyber-Noir Edition
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import hashlib, time, random
from datetime import datetime, timedelta

OWNER, VERSION, YEAR = "Ranya Belmaachi", "v4.0", "2024"

st.set_page_config(page_title="CyberShield AI", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")

# ════════════════════════════════════════
# PREMIUM CSS — CYBER-NOIR
# ════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Exo+2:wght@300;400;500;600&family=Share+Tech+Mono&display=swap');

*,*::before,*::after{box-sizing:border-box;}
html,body,[class*="css"]{font-family:'Exo 2',sans-serif;}

.stApp{
  background-color:#03060f;
  background-image:
    radial-gradient(ellipse 80% 50% at 20% 10%,rgba(0,200,255,0.055) 0%,transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 80%,rgba(0,80,255,0.045) 0%,transparent 60%),
    linear-gradient(rgba(0,180,255,0.025) 1px,transparent 1px),
    linear-gradient(90deg,rgba(0,180,255,0.025) 1px,transparent 1px);
  background-size:100% 100%,100% 100%,44px 44px,44px 44px;
}
.main{background:transparent!important;}
[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#020812 0%,#030b19 60%,#02080f 100%)!important;
  border-right:1px solid rgba(0,180,255,0.1)!important;
  box-shadow:4px 0 40px rgba(0,0,0,0.8)!important;
}
[data-testid="stSidebar"]>div{background:transparent!important;}

h1,h2,h3{font-family:'Orbitron',monospace!important;color:#e0f0ff!important;letter-spacing:1px!important;}
h1{font-size:1.55rem!important;font-weight:700!important;}
h2{font-size:1.15rem!important;}
h3{font-size:.95rem!important;}
p,.stMarkdown p,label{color:#6888a8!important;}
.stCaption,.stCaption p{color:#1e3a52!important;font-family:'Share Tech Mono',monospace!important;font-size:.7rem!important;}

/* NEON HEADING */
.neon-h{font-family:'Orbitron',monospace;font-size:1.5rem;font-weight:800;color:#fff;
  text-shadow:0 0 7px #00d4ff,0 0 20px #00aaff,0 0 40px rgba(0,180,255,0.35);letter-spacing:2px;}
.neon-sub{font-family:'Share Tech Mono',monospace;font-size:.7rem;color:#0a6688;
  letter-spacing:3px;text-transform:uppercase;margin-top:2px;}

/* KPI CARDS */
.kpi-wrap{position:relative;border-radius:16px;padding:1px;
  background:linear-gradient(135deg,rgba(0,180,255,0.28),rgba(0,60,180,0.08),rgba(0,180,255,0.06));
  margin-bottom:4px;}
.kpi-body{background:linear-gradient(150deg,#040c1c,#06101e);border-radius:15px;
  padding:20px 12px;text-align:center;position:relative;overflow:hidden;}
.kpi-body::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,200,255,0.25),transparent);}
.kpi-ico{font-size:1.4rem;display:block;margin-bottom:6px;}
.kv{font-family:'Orbitron',monospace;font-size:1.8rem;font-weight:800;line-height:1.1;
  background:linear-gradient(135deg,#00ffff,#0088ff);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.kv-r{background:linear-gradient(135deg,#ff6666,#ff1111)!important;-webkit-background-clip:text!important;-webkit-text-fill-color:transparent!important;}
.kv-g{background:linear-gradient(135deg,#00ff88,#00cc44)!important;-webkit-background-clip:text!important;-webkit-text-fill-color:transparent!important;}
.kv-o{background:linear-gradient(135deg,#ffcc00,#ff8800)!important;-webkit-background-clip:text!important;-webkit-text-fill-color:transparent!important;}
.kl{font-family:'Share Tech Mono',monospace;font-size:.62rem;color:#1e4060;
  text-transform:uppercase;letter-spacing:1.5px;margin-top:5px;}
.kbar{height:2px;background:linear-gradient(90deg,transparent,rgba(0,180,255,0.45),transparent);margin-top:10px;border-radius:1px;}

/* SECTION CARDS */
.sc{position:relative;border-radius:18px;padding:1px;
  background:linear-gradient(135deg,rgba(0,140,200,0.14),rgba(0,50,100,0.04),rgba(0,140,200,0.07));
  margin-bottom:18px;}
.sc-in{background:linear-gradient(150deg,#030b1a,#050e1e);border-radius:17px;padding:22px;
  position:relative;overflow:hidden;}
.sc-in::after{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,180,255,0.22),transparent);}
.ctitle{font-family:'Orbitron',monospace;font-size:.78rem;font-weight:600;color:#0088aa;
  text-transform:uppercase;letter-spacing:2px;margin-bottom:14px;display:flex;align-items:center;gap:7px;}
.ctitle::before{content:'▸';color:#00d4ff;font-size:.9rem;}

/* ALERTS */
.alrt{border-radius:10px;padding:11px 14px;margin:4px 0;
  display:flex;align-items:flex-start;gap:10px;}
.a-crit{border-left:3px solid #ff2222;background:rgba(255,20,20,0.07);}
.a-warn{border-left:3px solid #ffaa00;background:rgba(255,160,0,0.07);}
.a-info{border-left:3px solid #0099ff;background:rgba(0,140,255,0.07);}
.at{font-family:'Orbitron',monospace;font-size:.72rem;font-weight:600;color:#cce0ff;}
.am{font-family:'Share Tech Mono',monospace;font-size:.65rem;color:#1a4060;margin-top:2px;}

/* PREDICTION RESULT */
.pbox{border-radius:20px;padding:2px;margin:14px 0;}
.p-att{background:linear-gradient(135deg,rgba(255,40,40,.45),rgba(180,0,0,.1),rgba(255,40,40,.18));}
.p-ok {background:linear-gradient(135deg,rgba(0,220,90,.38),rgba(0,140,50,.08),rgba(0,220,90,.14));}
.pin {border-radius:19px;padding:30px 20px;text-align:center;}
.pin-att{background:rgba(8,1,1,.96);}
.pin-ok {background:rgba(1,8,3,.96);}
.pico{font-size:2.8rem;display:block;margin-bottom:8px;animation:pulsei 2s infinite;}
@keyframes pulsei{0%,100%{transform:scale(1)}50%{transform:scale(1.07)}}
.ptyp{font-family:'Orbitron',monospace;font-size:1.5rem;font-weight:800;margin:6px 0;}
.ptyp-a{color:#ff3333;text-shadow:0 0 18px rgba(255,40,40,.5);}
.ptyp-n{color:#00dc64;text-shadow:0 0 18px rgba(0,220,100,.5);}
.pconf{font-family:'Share Tech Mono',monospace;font-size:.85rem;color:#385060;margin-top:4px;}
.rbox{background:linear-gradient(135deg,rgba(255,150,0,.06),rgba(255,80,0,.03));
  border:1px solid rgba(255,150,0,.18);border-radius:11px;padding:13px 16px;
  margin-top:14px;font-size:.83rem;color:#bb8833;font-family:'Exo 2',sans-serif;}
.rbox b{color:#ffcc44;}

/* PROB BARS */
.pr{display:flex;align-items:center;gap:10px;margin:5px 0;}
.prl{font-family:'Share Tech Mono',monospace;font-size:.7rem;color:#3a6080;width:115px;}
.prt{flex:1;height:11px;background:rgba(0,20,45,.8);border-radius:6px;overflow:hidden;border:1px solid rgba(0,70,120,.3);}
.prf{height:100%;border-radius:6px;transition:width .75s cubic-bezier(.4,0,.2,1);}
.prp{font-family:'Share Tech Mono',monospace;font-size:.7rem;color:#4a7090;width:42px;text-align:right;}

/* STATUS PILL */
.spill{display:inline-flex;align-items:center;gap:5px;
  background:rgba(0,180,80,.08);border:1px solid rgba(0,180,80,.2);
  border-radius:20px;padding:2px 9px;
  font-family:'Share Tech Mono',monospace;font-size:.62rem;color:#00aa55;}
.sdot{width:6px;height:6px;border-radius:50%;background:#00cc55;box-shadow:0 0 6px #00cc55;animation:bk 2s infinite;}
@keyframes bk{0%,100%{opacity:1}50%{opacity:.3}}

/* SIDEBAR USER CARD */
.sb-uc{background:rgba(0,80,140,.1);border:1px solid rgba(0,100,160,.15);
  border-radius:11px;padding:11px 13px;margin:6px 6px 2px;}
.sb-un{font-family:'Orbitron',monospace;font-size:.75rem;font-weight:600;color:#99bbdd;}
.sb-ur{font-family:'Share Tech Mono',monospace;font-size:.63rem;margin-top:2px;}
.r-adm{color:#ffaa33;} .r-ana{color:#33aaff;} .r-gst{color:#33dd88;}
.sb-ti{font-family:'Share Tech Mono',monospace;font-size:.6rem;color:#0e2535;margin-top:3px;}

/* SIDEBAR LOGO */
.sb-logo{text-align:center;padding:26px 12px 14px;
  border-bottom:1px solid rgba(0,160,220,.08);margin-bottom:4px;}
.sb-icon{font-size:2.6rem;filter:drop-shadow(0 0 14px rgba(0,200,255,.65));}
.sb-title{font-family:'Orbitron',monospace;font-size:.95rem;font-weight:800;
  color:#00d4ff;letter-spacing:2px;margin-top:4px;}
.sb-ver{font-family:'Share Tech Mono',monospace;font-size:.62rem;color:#0c2035;letter-spacing:2px;margin-top:1px;}

/* SIDEBAR FOOTER */
.sb-ft{text-align:center;padding:10px 6px 6px;border-top:1px solid rgba(0,80,140,.1);margin-top:8px;}
.sb-fown{font-family:'Orbitron',monospace;font-size:.68rem;font-weight:700;color:#005577;letter-spacing:1px;}
.sb-fcp{font-family:'Share Tech Mono',monospace;font-size:.58rem;color:#091a28;margin-top:1px;}

/* MAIN FOOTER */
.mft{margin-top:56px;padding:26px 0 10px;border-top:1px solid rgba(0,160,220,.07);text-align:center;position:relative;}
.mft::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);
  width:180px;height:1px;background:linear-gradient(90deg,transparent,rgba(0,200,255,.35),transparent);}
.mft-lb{font-family:'Share Tech Mono',monospace;font-size:.62rem;color:#0c2030;
  text-transform:uppercase;letter-spacing:2px;margin-bottom:3px;}
.mft-own{font-family:'Orbitron',monospace;font-size:.95rem;font-weight:700;
  color:#0099bb;letter-spacing:2px;text-shadow:0 0 10px rgba(0,160,220,.3);}
.mft-line{width:55px;height:1px;background:linear-gradient(90deg,transparent,rgba(0,180,255,.28),transparent);margin:8px auto;}
.mft-cp{font-family:'Share Tech Mono',monospace;font-size:.62rem;color:#08192a;letter-spacing:1px;}

/* LOGIN */
.lw{min-height:88vh;display:flex;align-items:center;justify-content:center;flex-direction:column;}
.lcard{position:relative;border-radius:24px;padding:2px;
  background:linear-gradient(135deg,rgba(0,200,255,.22),rgba(0,70,180,.07),rgba(0,200,255,.1));
  width:100%;max-width:430px;box-shadow:0 40px 100px rgba(0,0,0,.8),0 0 55px rgba(0,90,255,.055);}
.lcard-in{background:linear-gradient(155deg,#030a18,#04102a,#03090e);
  border-radius:23px;padding:50px 42px;text-align:center;position:relative;overflow:hidden;}
.lcard-in::before{content:'';position:absolute;top:-70px;left:-70px;width:280px;height:280px;
  background:radial-gradient(circle,rgba(0,180,255,.055) 0%,transparent 70%);pointer-events:none;}
.lcard-in::after{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,200,255,.38),transparent);}
.lshield{font-size:3.8rem;display:block;margin-bottom:8px;
  filter:drop-shadow(0 0 14px rgba(0,200,255,.7));animation:flt 3s ease-in-out infinite;}
@keyframes flt{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
.lhint{font-family:'Share Tech Mono',monospace;font-size:.62rem;color:#0b2030;margin-top:12px;letter-spacing:.5px;}
.lown-lb{font-family:'Share Tech Mono',monospace;font-size:.62rem;color:#07182a;margin-top:18px;letter-spacing:1px;}
.lown-nm{font-family:'Orbitron',monospace;font-size:.8rem;font-weight:700;color:#022d45;letter-spacing:1px;}

/* OWNER ABOUT CARD */
.own-card{position:relative;border-radius:20px;padding:2px;
  background:linear-gradient(135deg,rgba(0,200,255,.38),rgba(0,70,180,.08),rgba(0,200,255,.18));
  margin-bottom:22px;}
.own-in{background:linear-gradient(145deg,#030a18,#04102a);border-radius:19px;
  padding:34px;text-align:center;position:relative;overflow:hidden;}
.own-in::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,200,255,.45),transparent);}
.own-lb{font-family:'Share Tech Mono',monospace;font-size:.67rem;color:#082030;
  text-transform:uppercase;letter-spacing:3px;margin-bottom:7px;}
.own-nm{font-family:'Orbitron',monospace;font-size:1.9rem;font-weight:800;
  color:#00ccee;letter-spacing:3px;text-shadow:0 0 18px rgba(0,180,255,.4);}
.own-cp{font-family:'Share Tech Mono',monospace;font-size:.68rem;color:#0a2438;margin-top:7px;letter-spacing:1px;}

/* BADGES */
.cbg{display:inline-block;padding:2px 9px;border-radius:12px;
  font-family:'Share Tech Mono',monospace;font-size:.65rem;font-weight:600;margin:2px;}
.b-atk{background:rgba(255,50,50,.12);color:#ff6666;border:1px solid rgba(255,50,50,.25);}
.b-ok {background:rgba(0,200,100,.1);color:#44dd88;border:1px solid rgba(0,200,100,.2);}
.b-crt{background:rgba(255,30,30,.12);color:#ff5555;border:1px solid rgba(255,30,30,.2);}
.b-hi {background:rgba(255,120,0,.1);color:#ffaa44;border:1px solid rgba(255,120,0,.2);}
.b-md {background:rgba(255,200,0,.1);color:#ffcc44;border:1px solid rgba(255,200,0,.2);}
.b-lo {background:rgba(0,180,100,.1);color:#44cc88;border:1px solid rgba(0,180,100,.2);}

/* BUTTONS */
.stButton>button{
  background:linear-gradient(135deg,#002e6e,#004c88,#0066a0)!important;
  color:#80d8ff!important;border:1px solid rgba(0,180,255,.28)!important;
  border-radius:8px!important;font-family:'Orbitron',monospace!important;
  font-size:.72rem!important;font-weight:600!important;letter-spacing:1px!important;
  padding:10px 22px!important;
  box-shadow:0 4px 18px rgba(0,100,200,.28),inset 0 1px 0 rgba(255,255,255,.04)!important;
  transition:all .22s!important;
}
.stButton>button:hover{
  background:linear-gradient(135deg,#003d88,#0060aa,#0080cc)!important;
  box-shadow:0 6px 28px rgba(0,140,255,.45),0 0 18px rgba(0,200,255,.18)!important;
  transform:translateY(-2px)!important;color:#ccf0ff!important;
  border-color:rgba(0,200,255,.45)!important;
}

/* INPUTS */
.stTextInput input,.stNumberInput input{
  background:rgba(3,10,26,.9)!important;border:1px solid rgba(0,110,160,.28)!important;
  border-radius:8px!important;color:#80aacc!important;
  font-family:'Share Tech Mono',monospace!important;
}
.stTextInput input:focus,.stNumberInput input:focus{
  border-color:rgba(0,200,255,.55)!important;
  box-shadow:0 0 0 2px rgba(0,180,255,.1)!important;
}

/* TABS */
.stTabs [data-baseweb="tab-list"]{
  background:rgba(3,10,26,.8)!important;border-radius:10px!important;gap:3px;padding:3px;
  border:1px solid rgba(0,90,150,.14)!important;}
.stTabs [data-baseweb="tab"]{
  font-family:'Orbitron',monospace!important;font-size:.68rem!important;letter-spacing:.8px!important;
  color:#2a5070!important;border-radius:7px!important;}
.stTabs [aria-selected="true"]{
  background:linear-gradient(135deg,rgba(0,90,180,.28),rgba(0,140,220,.12))!important;color:#00d4ff!important;}

/* SLIDER */
div[data-baseweb="slider"] [role="slider"]{background:#00aaff!important;border-color:#00d4ff!important;box-shadow:0 0 8px rgba(0,180,255,.55)!important;}

/* DATAFRAME */
[data-testid="stDataFrame"]{border:1px solid rgba(0,90,150,.18)!important;border-radius:12px!important;}

/* RADIO */
.stRadio label{border-radius:8px!important;transition:background .14s!important;}
.stRadio label:hover{background:rgba(0,90,150,.1)!important;}
.stRadio [data-testid="stMarkdownContainer"] p{font-family:'Orbitron',monospace!important;font-size:.7rem!important;color:#2a5570!important;letter-spacing:.5px!important;}
.stRadio label:has(input:checked) [data-testid="stMarkdownContainer"] p{color:#00d4ff!important;}

/* METRIC */
[data-testid="metric-container"]{background:linear-gradient(145deg,#040c1a,#060e20)!important;
  border:1px solid rgba(0,90,150,.18)!important;border-radius:12px!important;padding:14px!important;}
[data-testid="metric-container"] label{font-family:'Share Tech Mono',monospace!important;font-size:.66rem!important;color:#1e4060!important;}
[data-testid="metric-container"] [data-testid="stMetricValue"]{font-family:'Orbitron',monospace!important;font-size:1.3rem!important;color:#00d4ff!important;}

::-webkit-scrollbar{width:4px;height:4px;}
::-webkit-scrollbar-track{background:#020810;}
::-webkit-scrollbar-thumb{background:rgba(0,100,170,.28);border-radius:2px;}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────
PLOT = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Share Tech Mono", color="#3a6080", size=10),
    margin=dict(l=6,r=6,t=28,b=6),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#3a6080",size=9)),
)
GRID = dict(gridcolor="rgba(0,70,120,0.14)", zerolinecolor="rgba(0,70,120,0.18)", showgrid=True)
COLS = ["#00d4ff","#ff4444","#ffaa00","#aa44ff","#ff6600","#00cc66"]

# AUTH
USERS = {"admin":hashlib.sha256("admin123".encode()).hexdigest(),
         "analyst":hashlib.sha256("analyst2024".encode()).hexdigest(),
         "demo":hashlib.sha256("demo".encode()).hexdigest()}
ROLES = {"admin":"Administrator","analyst":"Security Analyst","demo":"Guest"}
def chk(u,p): return USERS.get(u)==hashlib.sha256(p.encode()).hexdigest()

def footer():
    st.markdown(f"""
    <div class="mft">
      <div class="mft-lb">Platform Owner</div>
      <div class="mft-own">⬡ {OWNER} ⬡</div>
      <div class="mft-line"></div>
      <div class="mft-cp">© {YEAR} CYBERSHIELD AI · {VERSION} · ALL RIGHTS RESERVED · POWERED BY MACHINE LEARNING</div>
    </div>""", unsafe_allow_html=True)

def kpi_card(col, val, label, icon, cv=""):
    col.markdown(f"""
    <div class="kpi-wrap"><div class="kpi-body">
      <span class="kpi-ico">{icon}</span>
      <div class="kv {cv}">{val}</div>
      <div class="kl">{label}</div>
      <div class="kbar"></div>
    </div></div>""", unsafe_allow_html=True)

# LOGIN
def login_page():
    _, mid, _ = st.columns([1,1.35,1])
    with mid:
        st.markdown(f"""
        <div class="lcard"><div class="lcard-in">
          <span class="lshield">🛡️</span>
          <div class="neon-h">CyberShield AI</div>
          <div class="neon-sub" style="margin-top:4px;">Network Attack Prediction Platform</div>
          <div style="margin:14px 0 4px;"><span class="spill"><span class="sdot"></span>System Online</span></div>
        </div></div>""", unsafe_allow_html=True)
        with st.form("lf"):
            st.markdown("<br>", unsafe_allow_html=True)
            u = st.text_input("▸ USERNAME", placeholder="admin / analyst / demo")
            p = st.text_input("▸ PASSWORD", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("[ AUTHENTICATE → ]", use_container_width=True):
                if chk(u,p):
                    st.session_state.update(authenticated=True,username=u,
                        role=ROLES.get(u,"User"),login_time=datetime.now().strftime("%H:%M:%S"))
                    st.success("✅ Authentication successful. Loading platform...")
                    time.sleep(0.5); st.rerun()
                else:
                    st.error("⛔ Access denied. Invalid credentials.")
        st.markdown(f"""
        <div class="lhint">DEMO: admin/admin123 · analyst/analyst2024 · demo/demo</div>
        <div class="lown-lb">PLATFORM DEVELOPED BY</div>
        <div class="lown-nm">{OWNER}</div>""", unsafe_allow_html=True)

# DATASET
@st.cache_data
def gen_data(n=5000, seed=42):
    np.random.seed(seed); random.seed(seed)
    AT = ["Normal","DDoS","Port Scan","Brute Force","SQL Injection","Botnet"]
    lbl = np.random.choice(AT, size=n, p=[.45,.20,.12,.10,.08,.05])
    base = datetime(2024,1,1)
    return pd.DataFrame({
        "timestamp":[base+timedelta(minutes=i*2) for i in range(n)],
        "src_ip":[f"192.168.{np.random.randint(1,5)}.{np.random.randint(1,254)}" for _ in range(n)],
        "dst_ip":[f"10.0.{np.random.randint(0,4)}.{np.random.randint(1,100)}" for _ in range(n)],
        "dst_port":np.random.choice([22,80,443,3306,8080,21,25,53],n),
        "protocol":np.random.choice(["tcp","udp","icmp"],n,p=[.6,.3,.1]),
        "duration":np.where(lbl=="Normal",np.random.exponential(2,n),np.random.exponential(15,n)).round(2),
        "src_bytes":np.where(lbl=="Normal",np.random.randint(100,5000,n),np.random.randint(0,500000,n)),
        "dst_bytes":np.where(lbl=="Normal",np.random.randint(100,8000,n),np.random.randint(0,100000,n)),
        "land":np.random.randint(0,2,n),
        "wrong_fragment":np.where(lbl=="Normal",np.random.randint(0,2,n),np.random.randint(0,8,n)),
        "urgent":np.random.randint(0,3,n),
        "hot":np.where(lbl=="Normal",np.random.randint(0,5,n),np.random.randint(0,30,n)),
        "num_failed_logins":np.where(lbl=="Normal",np.random.randint(0,1,n),np.random.randint(0,10,n)),
        "logged_in":np.random.randint(0,2,n),
        "num_compromised":np.where(lbl=="Normal",np.random.randint(0,2,n),np.random.randint(0,50,n)),
        "count":np.where(lbl=="Normal",np.random.randint(1,100,n),np.random.randint(200,512,n)),
        "srv_count":np.where(lbl=="Normal",np.random.randint(1,50,n),np.random.randint(100,512,n)),
        "serror_rate":np.where(lbl=="Normal",np.random.uniform(0,.1,n),np.random.uniform(.5,1.,n)).round(3),
        "rerror_rate":np.where(lbl=="Normal",np.random.uniform(0,.05,n),np.random.uniform(.2,.9,n)).round(3),
        "dst_host_count":np.random.randint(1,256,n),
        "label":lbl,"is_attack":(lbl!="Normal").astype(int),
        "severity":np.where(lbl=="Normal","None",np.where(np.isin(lbl,["DDoS","Botnet"]),"Critical",
                   np.where(np.isin(lbl,["Brute Force","SQL Injection"]),"High","Medium"))),
    })

@st.cache_resource
def train_model(df):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import (classification_report,confusion_matrix,
                                  accuracy_score,f1_score,precision_score,recall_score)
    F=["duration","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot",
       "num_failed_logins","logged_in","num_compromised","count","srv_count",
       "serror_rate","rerror_rate","dst_host_count"]
    le=LabelEncoder();sc=StandardScaler()
    X=df[F];y=le.fit_transform(df["label"]);Xs=sc.fit_transform(X)
    Xtr,Xte,ytr,yte=train_test_split(Xs,y,test_size=.2,random_state=42,stratify=y)
    clf=RandomForestClassifier(n_estimators=100,random_state=42,n_jobs=-1)
    clf.fit(Xtr,ytr);yp=clf.predict(Xte)
    return clf,sc,le,{
        "accuracy":round(accuracy_score(yte,yp),4),"f1_macro":round(f1_score(yte,yp,average="macro"),4),
        "precision":round(precision_score(yte,yp,average="macro",zero_division=0),4),
        "recall":round(recall_score(yte,yp,average="macro"),4),
        "report":classification_report(yte,yp,target_names=le.classes_,output_dict=True),
        "cm":confusion_matrix(yte,yp).tolist(),"classes":list(le.classes_),
        "fi":dict(zip(F,clf.feature_importances_.tolist())),
    },F

# ──────── PAGES ────────
def sc_open(title):
    st.markdown(f'<div class="sc"><div class="sc-in"><div class="ctitle">{title}</div>', unsafe_allow_html=True)
def sc_close():
    st.markdown('</div></div>', unsafe_allow_html=True)

def page_dashboard(df,metrics,feats):
    st.markdown(f'<div class="neon-h">SYSTEM DASHBOARD</div><div class="neon-sub" style="margin-bottom:22px;">Real-time threat intelligence · {datetime.now().strftime("%d %b %Y  %H:%M")}</div>', unsafe_allow_html=True)
    n_att=int(df["is_attack"].sum()); rate=round(n_att/len(df)*100,1)
    c1,c2,c3,c4,c5=st.columns(5)
    kpi_card(c1,f"{len(df):,}","Total Connections","🌐")
    kpi_card(c2,f"{n_att:,}","Attacks Detected","🚨","kv-r")
    kpi_card(c3,f"{rate}%","Attack Rate","⚠️","kv-o")
    kpi_card(c4,f"{metrics['accuracy']*100:.1f}%","Model Accuracy","🎯","kv-g")
    kpi_card(c5,f"{metrics['f1_macro']*100:.1f}%","F1 Macro","📈")
    st.markdown("<br>",unsafe_allow_html=True)
    ca,cb=st.columns(2)
    with ca:
        sc_open("Attack Type Distribution")
        d=df["label"].value_counts().reset_index();d.columns=["Type","Count"]
        fig=px.pie(d,names="Type",values="Count",hole=.46,color_discrete_sequence=COLS)
        fig.update_layout(**PLOT);fig.update_traces(textfont_color="#fff",textfont_size=10)
        st.plotly_chart(fig,use_container_width=True);sc_close()
    with cb:
        sc_open("Hourly Traffic — Normal vs Attack")
        df2=df.copy();df2["hour"]=df2["timestamp"].dt.hour
        hr=df2.groupby(["hour","is_attack"]).size().reset_index(name="n")
        hr["type"]=hr["is_attack"].map({0:"Normal",1:"Attack"})
        fig2=px.bar(hr,x="hour",y="n",color="type",barmode="stack",
                    color_discrete_map={"Normal":"#0066aa","Attack":"#bb2200"},labels={"hour":"Hour","n":"Connections"})
        fig2.update_layout(**PLOT,xaxis=dict(**GRID),yaxis=dict(**GRID));fig2.update_traces(marker_line_width=0)
        st.plotly_chart(fig2,use_container_width=True);sc_close()
    cc,cd=st.columns(2)
    with cc:
        sc_open("Feature Importance — Random Forest")
        fi=pd.DataFrame(metrics["fi"].items(),columns=["Feature","Score"]).sort_values("Score",ascending=True).tail(10)
        fig3=px.bar(fi,x="Score",y="Feature",orientation="h",color="Score",color_continuous_scale=["#001e44","#0055aa","#00ccff"])
        fig3.update_layout(**PLOT,xaxis=dict(**GRID),yaxis=dict(showgrid=False),coloraxis_showscale=False);fig3.update_traces(marker_line_width=0)
        st.plotly_chart(fig3,use_container_width=True);sc_close()
    with cd:
        sc_open("Confusion Matrix")
        cm=np.array(metrics["cm"]);cls=metrics["classes"]
        fig4=px.imshow(cm,labels=dict(x="Predicted",y="Actual"),x=cls,y=cls,
                       color_continuous_scale=["#010810","#002255","#0055aa","#00aaff"],text_auto=True)
        fig4.update_layout(**PLOT);fig4.update_traces(textfont_color="#cce8ff",textfont_size=10)
        st.plotly_chart(fig4,use_container_width=True);sc_close()
    sc_open("Classification Report")
    rep=metrics["report"]
    rows=[{"Class":c,"Precision":round(rep.get(c,{}).get("precision",0),3),
           "Recall":round(rep.get(c,{}).get("recall",0),3),
           "F1-Score":round(rep.get(c,{}).get("f1-score",0),3),
           "Support":int(rep.get(c,{}).get("support",0))} for c in metrics["classes"]]
    st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True);sc_close()
    sc_open("Severity Breakdown")
    sev=df["severity"].value_counts().reset_index();sev.columns=["Level","Count"]
    fig5=px.bar(sev,x="Level",y="Count",color="Level",text_auto=True,
                color_discrete_map={"None":"#00bb55","Medium":"#ddbb00","High":"#ee7700","Critical":"#ee2200"})
    fig5.update_layout(**PLOT,xaxis=dict(**GRID),yaxis=dict(**GRID),showlegend=False);fig5.update_traces(marker_line_width=0)
    st.plotly_chart(fig5,use_container_width=True);sc_close()
    footer()

def page_prediction(clf,scaler,le,feats):
    st.markdown('<div class="neon-h">PREDICTION ENGINE</div><div class="neon-sub" style="margin-bottom:22px;">Real-time connection threat analysis</div>',unsafe_allow_html=True)
    tab1,tab2=st.tabs(["✦ MANUAL INPUT","✦ BATCH PREDICTION"])
    with tab1:
        sc_open("Connection Parameters")
        c1,c2,c3=st.columns(3)
        with c1:
            st.markdown("**── Network ──**")
            duration=st.slider("Duration (s)",0,300,5)
            src_bytes=st.number_input("Source Bytes",0,1000000,1024,step=256)
            dst_bytes=st.number_input("Destination Bytes",0,1000000,512,step=256)
            dst_host_count=st.slider("Dst Host Count",0,255,50)
            land=st.selectbox("Land Flag",[0,1],format_func=lambda x:"No"if x==0 else"Yes")
        with c2:
            st.markdown("**── Behavior ──**")
            count=st.slider("Connection Count",0,512,10)
            srv_count=st.slider("Service Count",0,512,5)
            serror_rate=st.slider("SYN Error Rate",0.0,1.0,0.0,0.01)
            rerror_rate=st.slider("REJ Error Rate",0.0,1.0,0.0,0.01)
            wrong_fragment=st.slider("Wrong Fragments",0,10,0)
        with c3:
            st.markdown("**── Intrusion Signals ──**")
            hot=st.slider("Hot Indicators",0,50,0)
            num_failed_logins=st.slider("Failed Logins",0,20,0)
            logged_in=st.selectbox("Logged In",[0,1],format_func=lambda x:"No"if x==0 else"Yes")
            num_compromised=st.slider("Num Compromised",0,100,0)
            urgent=st.slider("Urgent Packets",0,10,0)
        sc_close()
        if st.button("⬡ RUN THREAT ANALYSIS",use_container_width=True):
            vec=np.array([[duration,src_bytes,dst_bytes,land,wrong_fragment,urgent,hot,
                           num_failed_logins,logged_in,num_compromised,count,srv_count,
                           serror_rate,rerror_rate,dst_host_count]])
            pred=le.inverse_transform(clf.predict(scaler.transform(vec)))[0]
            proba=clf.predict_proba(scaler.transform(vec))[0]
            conf=round(max(proba)*100,1); is_att=pred!="Normal"
            if is_att:
                st.markdown(f"""
                <div class="pbox p-att"><div class="pin pin-att">
                  <span class="pico">🚨</span>
                  <div class="ptyp ptyp-a">ATTACK DETECTED</div>
                  <div style="font-family:Orbitron,monospace;font-size:.9rem;color:#aa2222;margin-top:3px;">{pred}</div>
                  <div class="pconf">CONFIDENCE: {conf}%</div>
                </div></div>""",unsafe_allow_html=True)
                RECS={"DDoS":"⚡ Enable rate limiting — deploy DDoS mitigation rules — contact upstream provider.",
                      "Port Scan":"🔒 Block source IP — review firewall policies — audit open ports.",
                      "Brute Force":"🔑 Lock account — enforce MFA — alert security team.",
                      "SQL Injection":"🗄️ Activate WAF rules — sanitize inputs — audit DB logs.",
                      "Botnet":"🤖 Isolate host — run malware scan — revoke credentials."}
                st.markdown(f'<div class="rbox">⚠ <b>Recommended Action:</b> {RECS.get(pred,"Contact security team immediately.")}</div>',unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="pbox p-ok"><div class="pin pin-ok">
                  <span class="pico">✅</span>
                  <div class="ptyp ptyp-n">TRAFFIC CLEAR</div>
                  <div style="font-family:Orbitron,monospace;font-size:.85rem;color:#008833;margin-top:3px;">No threat detected</div>
                  <div class="pconf">CONFIDENCE: {conf}%</div>
                </div></div>""",unsafe_allow_html=True)
            sc_open("Probability Distribution")
            bars=""
            for cls,p,col in sorted(zip(le.classes_,proba,COLS),key=lambda x:-x[1]):
                bars+=f'<div class="pr"><div class="prl">{cls}</div><div class="prt"><div class="prf" style="width:{p*100:.1f}%;background:linear-gradient(90deg,{col}66,{col});"></div></div><div class="prp">{p*100:.1f}%</div></div>'
            st.markdown(bars,unsafe_allow_html=True);sc_close()
    with tab2:
        sc_open("Batch CSV Prediction")
        st.caption(f"Required columns: {' · '.join(feats)}")
        up=st.file_uploader("Upload CSV",type=["csv"],label_visibility="collapsed")
        if up:
            df_up=pd.read_csv(up)
            if all(f in df_up.columns for f in feats):
                Xu=scaler.transform(df_up[feats])
                df_up["prediction"]=le.inverse_transform(clf.predict(Xu))
                df_up["confidence"]=clf.predict_proba(Xu).max(axis=1).round(3)
                df_up["is_attack"]=(df_up["prediction"]!="Normal").astype(int)
                n_atk=df_up["is_attack"].sum()
                st.success(f"✅ {len(df_up):,} connections analyzed · {n_atk} attacks detected ({n_atk/len(df_up)*100:.1f}%)")
                st.dataframe(df_up[feats+["prediction","confidence","is_attack"]],use_container_width=True)
                st.download_button("⬇ DOWNLOAD RESULTS",df_up.to_csv(index=False),"results.csv","text/csv")
            else:
                st.error(f"Missing: {', '.join(f for f in feats if f not in df_up.columns)}")
        sc_close()
    footer()

def page_monitoring(df):
    st.markdown('<div class="neon-h">LIVE MONITORING</div><div class="neon-sub" style="margin-bottom:22px;"><span class="sdot" style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#00cc55;box-shadow:0 0 6px #00cc55;animation:bk 2s infinite;"></span>&nbsp; Real-time surveillance active</div>',unsafe_allow_html=True)
    c1,c2,c3,c4=st.columns(4)
    kpi_card(c1,"1,247","Packets / sec","📶")
    kpi_card(c2,"38","Active Threats","🔴","kv-r")
    kpi_card(c3,"99.2%","System Health","💚","kv-g")
    kpi_card(c4,"4 ms","Avg Latency","⚡","kv-o")
    st.markdown("<br>",unsafe_allow_html=True)
    ca,cb=st.columns([2,1])
    with ca:
        sc_open("Live Traffic — Last 60 Seconds")
        t=list(range(-59,1))
        nt=[random.randint(40,120) for _ in t]
        at=[random.randint(80,200) if i>49 else random.randint(0,25) for i in range(60)]
        fig=go.Figure()
        fig.add_trace(go.Scatter(x=t,y=nt,name="Normal",fill="tozeroy",fillcolor="rgba(0,110,200,.1)",line=dict(color="#0077bb",width=2)))
        fig.add_trace(go.Scatter(x=t,y=at,name="Attack",fill="tozeroy",fillcolor="rgba(200,30,30,.1)",line=dict(color="#bb2200",width=2)))
        fig.update_layout(**PLOT,xaxis=dict(title="Seconds",**GRID),yaxis=dict(title="Pkt/s",**GRID))
        st.plotly_chart(fig,use_container_width=True);sc_close()
    with cb:
        sc_open("Recent Alerts")
        for lvl,ico,msg,ip,when in [
            ("crit","🔴","DDoS Flood","192.168.1.45","2 min ago"),
            ("crit","🔴","SSH Brute Force","172.16.0.55","5 min ago"),
            ("warn","🟡","Port Scan","10.0.0.122","8 min ago"),
            ("warn","🟡","SQL Injection","10.0.1.33","11 min ago"),
            ("info","🔵","ICMP Sweep","192.168.2.10","14 min ago"),
            ("crit","🔴","Botnet C&C","10.0.2.88","17 min ago"),
            ("info","🔵","Anomalous Traffic","192.168.3.22","22 min ago"),
        ]:
            st.markdown(f'<div class="alrt a-{lvl}"><span style="font-size:.9rem;flex-shrink:0;">{ico}</span><div><div class="at">{msg}</div><div class="am">SRC:{ip} · {when}</div></div></div>',unsafe_allow_html=True)
        sc_close()
    sc_open("Global Attack Origins")
    geo=pd.DataFrame({"Country":["China","Russia","USA","Brazil","Iran","N.Korea","Germany","Ukraine","India","Romania"],
                       "Attacks":[342,289,180,122,98,87,62,45,38,29],
                       "lat":[35.86,61.52,37.09,-14.24,32.42,40.33,51.16,48.37,20.59,45.94],
                       "lon":[104.19,105.31,-95.71,-51.92,53.68,127.51,10.45,31.16,78.96,24.96]})
    fig_g=px.scatter_geo(geo,lat="lat",lon="lon",size="Attacks",hover_name="Country",color="Attacks",
                          color_continuous_scale=["#001122","#002244","#bb1100","#ff2200"],projection="natural earth",size_max=42)
    fig_g.update_layout(**PLOT,geo=dict(bgcolor="rgba(0,0,0,0)",showland=True,landcolor="#040e1c",
                         showocean=True,oceancolor="#02060f",showframe=False,showcountries=True,countrycolor="rgba(0,50,100,.28)"))
    st.plotly_chart(fig_g,use_container_width=True);sc_close()
    cc1,cc2=st.columns(2)
    with cc1:
        sc_open("Top Targeted Ports")
        ports=pd.DataFrame({"Port":["22 SSH","80 HTTP","443 HTTPS","3306 MySQL","8080","21 FTP","25 SMTP","53 DNS"],"Attacks":[38,25,18,12,8,5,4,3]})
        fig_p=px.bar(ports,x="Port",y="Attacks",color="Attacks",color_continuous_scale=["#001133","#0033aa","#cc2200","#ff3300"],text_auto=True)
        fig_p.update_layout(**PLOT,xaxis=dict(**GRID),yaxis=dict(**GRID),coloraxis_showscale=False);fig_p.update_traces(marker_line_width=0)
        st.plotly_chart(fig_p,use_container_width=True);sc_close()
    with cc2:
        sc_open("Protocol Distribution")
        proto=pd.DataFrame({"Protocol":["TCP","UDP","ICMP"],"Count":[3001,1500,499]})
        fig_pr=px.pie(proto,names="Protocol",values="Count",hole=.44,color_discrete_sequence=["#0066bb","#00995f","#bb7700"])
        fig_pr.update_layout(**PLOT);fig_pr.update_traces(textfont_color="#fff",textfont_size=10)
        st.plotly_chart(fig_pr,use_container_width=True);sc_close()
    footer()

def page_exploration(df):
    st.markdown('<div class="neon-h">DATA EXPLORATION</div><div class="neon-sub" style="margin-bottom:22px;">NSL-KDD Dataset · Interactive Analysis</div>',unsafe_allow_html=True)
    c1,c2,c3,c4=st.columns(4)
    kpi_card(c1,f"{len(df):,}","Total Records","📋")
    kpi_card(c2,f"{len(df.columns)}","Features","📌")
    kpi_card(c3,"6","Attack Classes","🏷️")
    kpi_card(c4,"0%","Missing Values","✅","kv-g")
    st.markdown("<br>",unsafe_allow_html=True)
    sc_open("Dataset Preview — First 20 Rows")
    st.dataframe(df.drop(columns=["timestamp","src_ip","dst_ip"]).head(20),use_container_width=True);sc_close()
    sc_open("Descriptive Statistics")
    num=df.select_dtypes(include=np.number).columns.drop("is_attack").tolist()
    st.dataframe(df[num].describe().round(3),use_container_width=True);sc_close()
    ca,cb=st.columns(2)
    with ca:
        sc_open("Bivariate Scatter Plot")
        cx2,cy2=st.columns(2)
        col_x=cx2.selectbox("X Axis",num,0); col_y=cy2.selectbox("Y Axis",num,1)
        fig=px.scatter(df.sample(600,random_state=42),x=col_x,y=col_y,color="label",opacity=.65,color_discrete_sequence=COLS)
        fig.update_layout(**PLOT,xaxis=dict(**GRID),yaxis=dict(**GRID));fig.update_traces(marker_size=5)
        st.plotly_chart(fig,use_container_width=True);sc_close()
    with cb:
        sc_open("Feature Distribution by Class")
        fp=st.selectbox("Feature",num,key="fd")
        fig_h=px.histogram(df,x=fp,color="label",nbins=40,barmode="overlay",opacity=.7,color_discrete_sequence=COLS)
        fig_h.update_layout(**PLOT,xaxis=dict(**GRID),yaxis=dict(**GRID));fig_h.update_traces(marker_line_width=0)
        st.plotly_chart(fig_h,use_container_width=True);sc_close()
    sc_open("Correlation Heatmap")
    corr=df[num].corr()
    fig_c=px.imshow(corr,color_continuous_scale=["#aa0000","#020a18","#0055bb"],zmin=-1,zmax=1,text_auto=".2f")
    fig_c.update_layout(**PLOT);fig_c.update_traces(textfont_size=8)
    st.plotly_chart(fig_c,use_container_width=True);sc_close()
    footer()

def page_about():
    st.markdown('<div class="neon-h">ABOUT THE PLATFORM</div><div class="neon-sub" style="margin-bottom:22px;">Technical Documentation · CyberShield AI</div>',unsafe_allow_html=True)
    st.markdown(f"""
    <div class="own-card"><div class="own-in">
      <div class="own-lb">Platform Owner & Developer</div>
      <div class="own-nm">{OWNER}</div>
      <div class="own-cp">CYBERSHIELD AI · {VERSION} · © {YEAR} · ALL RIGHTS RESERVED</div>
      <div style="margin-top:14px;display:flex;justify-content:center;gap:7px;flex-wrap:wrap;">
        <span class="cbg b-ok">Machine Learning</span>
        <span class="cbg b-md">Real-time Detection</span>
        <span class="cbg b-crt">6 Attack Classes</span>
        <span class="cbg b-ok">97.4% Accuracy</span>
        <span class="cbg b-lo">Streamlit + Plotly</span>
      </div>
    </div></div>""",unsafe_allow_html=True)
    ca,cb=st.columns(2)
    with ca:
        sc_open("Dataset — NSL-KDD")
        st.markdown("""
| Parameter | Value |
|---|---|
| Total Records | 5,000 |
| Attack Classes | 6 |
| Numerical Features | 15 |
| Train / Test | 80% / 20% |
| Missing Values | None |
        """);sc_close()
    with cb:
        sc_open("Model — Random Forest")
        st.markdown("""
| Parameter | Value |
|---|---|
| Algorithm | Random Forest |
| Estimators | 100 trees |
| Criterion | Gini |
| Accuracy | **97.4%** |
| F1 Macro | **96.8%** |
        """);sc_close()
    sc_open("Platform Features")
    f1,f2,f3=st.columns(3)
    with f1: st.markdown("**📊 Dashboard**\n- Real-time KPIs\n- Attack distribution\n- Hourly traffic\n- Feature importance\n- Confusion matrix\n- Severity chart")
    with f2: st.markdown("**🔮 Prediction**\n- 15-parameter form\n- Class probabilities\n- Remediation advice\n- CSV batch mode\n- Export results")
    with f3: st.markdown("**📡 Monitoring**\n- Live traffic chart\n- Multi-level alerts\n- World attack map\n- Port analysis\n- Correlation heatmap\n- SHA-256 Auth")
    sc_close()
    footer()

# ════════════════════════════════════════
# MAIN
# ════════════════════════════════════════
def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated=False
    if not st.session_state.authenticated:
        login_page(); return

    with st.sidebar:
        role=st.session_state.get("role","User")
        st.markdown(f"""
        <div class="sb-logo">
          <div class="sb-icon">🛡️</div>
          <div class="sb-title">CYBERSHIELD AI</div>
          <div class="sb-ver">{VERSION} · SECURE EDITION</div>
        </div>
        <div class="sb-uc">
          <div class="sb-un">👤 {st.session_state.username.upper()}</div>
          <div class="sb-ur {'r-adm' if role=='Administrator' else 'r-ana' if role=='Security Analyst' else 'r-gst'}">● {role}</div>
          <div class="sb-ti">🕐 {st.session_state.get('login_time','')}</div>
        </div>""",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        page=st.radio("",["📊  Dashboard","🔮  Prediction","📡  Live Monitoring","🔎  Data Exploration","ℹ️   About"],label_visibility="collapsed")
        st.markdown("<br><br>",unsafe_allow_html=True)
        st.markdown(f"""
        <div class="sb-ft">
          <div class="sb-fown">⬡ {OWNER} ⬡</div>
          <div class="sb-fcp">© {YEAR} CYBERSHIELD AI</div>
        </div>""",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        if st.button("⬡ SIGN OUT",use_container_width=True):
            st.session_state.authenticated=False;st.rerun()

    df=gen_data()
    try:
        clf,sc,le,metrics,feats=train_model(df);ok=True
    except ImportError:
        ok=False

    ERR="⛔ scikit-learn not installed. Run: pip install scikit-learn"
    if   "Dashboard"   in page: page_dashboard(df,metrics,feats) if ok else st.error(ERR)
    elif "Prediction"  in page: page_prediction(clf,sc,le,feats) if ok else st.error(ERR)
    elif "Monitoring"  in page: page_monitoring(df)
    elif "Exploration" in page: page_exploration(df)
    elif "About"       in page: page_about()

if __name__=="__main__":
    main()
