<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ARCADIA — Premium Game Lounge</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
/* ─── TOKENS ─────────────────────────────────────── */
:root {
  --bg:          #080A0F;
  --surface:     #0E1117;
  --card:        #131820;
  --border:      #1E2530;
  --border-hi:   #2A3545;
  --text:        #E8EDF5;
  --muted:       #5A6478;
  --accent:      #C8A96E;
  --accent-dim:  #8A7148;
  --accent-glow: rgba(200,169,110,0.15);
  --green:       #39D98A;
  --red:         #FF5B5B;
  --blue:        #4D9FFF;
  --yellow:      #FFD166;
  --coin:        #FFD700;
  --radius:      12px;
  --radius-lg:   20px;
  --shadow:      0 8px 40px rgba(0,0,0,0.6);
  --font:        'Space Grotesk', sans-serif;
  --mono:        'DM Mono', monospace;
}

/* ─── RESET ──────────────────────────────────────── */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{font-size:16px;scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--font);min-height:100vh;overflow-x:hidden}
button{cursor:pointer;font-family:var(--font)}
input{font-family:var(--font)}

/* ─── SCROLLBAR ──────────────────────────────────── */
::-webkit-scrollbar{width:4px}
::-webkit-scrollbar-track{background:var(--surface)}
::-webkit-scrollbar-thumb{background:var(--border-hi);border-radius:2px}

/* ─── SCREENS ────────────────────────────────────── */
.screen{display:none;min-height:100vh}
.screen.active{display:flex}

/* ════════════════════════════════════════════════════
   LOGIN SCREEN
════════════════════════════════════════════════════ */
#login-screen{
  align-items:center;justify-content:center;
  background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(200,169,110,0.08) 0%, transparent 70%);
}
.login-card{
  width:420px;padding:56px 48px;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--radius-lg);
  box-shadow:var(--shadow), 0 0 0 1px rgba(200,169,110,0.05);
}
.logo{
  text-align:center;margin-bottom:40px;
}
.logo-mark{
  display:inline-flex;align-items:center;justify-content:center;
  width:56px;height:56px;
  background:linear-gradient(135deg,#C8A96E,#8A7148);
  border-radius:14px;margin-bottom:16px;
  font-size:24px;
}
.logo h1{font-size:28px;font-weight:700;letter-spacing:4px;color:var(--accent)}
.logo p{color:var(--muted);font-size:13px;letter-spacing:1px;margin-top:4px}
.field{margin-bottom:20px}
.field label{display:block;font-size:12px;font-weight:600;letter-spacing:1px;color:var(--muted);margin-bottom:8px;text-transform:uppercase}
.field input{
  width:100%;padding:14px 16px;
  background:var(--card);border:1px solid var(--border);
  border-radius:var(--radius);color:var(--text);font-size:15px;
  transition:border-color 0.2s;outline:none;
}
.field input:focus{border-color:var(--accent)}
.field input::placeholder{color:var(--muted)}
.btn-primary{
  width:100%;padding:15px;
  background:linear-gradient(135deg,#C8A96E,#A0824A);
  border:none;border-radius:var(--radius);
  color:#000;font-size:14px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
  transition:opacity 0.2s,transform 0.1s;
}
.btn-primary:hover{opacity:0.9;transform:translateY(-1px)}
.btn-primary:active{transform:translateY(0)}
.login-note{text-align:center;margin-top:20px;font-size:12px;color:var(--muted);line-height:1.6}

/* ════════════════════════════════════════════════════
   APP LAYOUT
════════════════════════════════════════════════════ */
#app-screen{flex-direction:column}

/* ─── TOPBAR ──────────────────────────────────────── */
.topbar{
  position:sticky;top:0;z-index:100;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 32px;height:64px;
  background:rgba(8,10,15,0.95);
  border-bottom:1px solid var(--border);
  backdrop-filter:blur(20px);
}
.topbar-logo{font-size:18px;font-weight:700;letter-spacing:3px;color:var(--accent)}
.topbar-user{display:flex;align-items:center;gap:12px}
.user-badge{
  display:flex;align-items:center;gap:10px;
  padding:6px 14px;
  background:var(--card);border:1px solid var(--border);border-radius:50px;
}
.user-icon{font-size:16px;line-height:1}
.user-name{font-size:14px;font-weight:600}
.user-tags{display:flex;gap:4px;align-items:center}
.tag-pill{
  font-size:10px;font-weight:700;letter-spacing:.5px;padding:2px 7px;
  background:rgba(200,169,110,0.12);border:1px solid rgba(200,169,110,0.25);
  border-radius:20px;color:var(--accent);white-space:nowrap;
}
.coin-display{
  display:flex;align-items:center;gap:6px;
  padding:6px 14px;
  background:var(--card);border:1px solid var(--border);border-radius:50px;
  font-size:14px;font-weight:700;color:var(--coin);
}
.coin-icon{font-size:14px}

/* ─── MAIN LAYOUT ─────────────────────────────────── */
.main-layout{display:flex;flex:1;height:calc(100vh - 64px)}
.sidebar{
  width:220px;flex-shrink:0;
  background:var(--surface);border-right:1px solid var(--border);
  padding:24px 12px;display:flex;flex-direction:column;gap:4px;
  overflow-y:auto;
}
.nav-section{font-size:10px;font-weight:700;letter-spacing:1.5px;color:var(--muted);text-transform:uppercase;padding:8px 12px 6px}
.nav-item{
  display:flex;align-items:center;gap:10px;
  padding:10px 12px;border-radius:var(--radius);
  font-size:13px;font-weight:500;color:var(--muted);
  border:none;background:none;width:100%;text-align:left;
  cursor:pointer;transition:all 0.15s;
}
.nav-item:hover{color:var(--text);background:var(--card)}
.nav-item.active{color:var(--accent);background:rgba(200,169,110,0.08);font-weight:600}
.nav-item .nav-icon{font-size:16px;width:20px;text-align:center}
.nav-item .nav-badge{
  margin-left:auto;font-size:10px;padding:2px 6px;
  background:var(--accent);color:#000;border-radius:20px;font-weight:700;
}

.content{flex:1;overflow-y:auto;padding:32px}

/* ─── STAT BAR ────────────────────────────────────── */
.stat-bar{
  display:flex;gap:12px;margin-bottom:28px;
}
.stat-tile{
  flex:1;padding:20px;background:var(--card);border:1px solid var(--border);
  border-radius:var(--radius);
}
.stat-tile .label{font-size:11px;font-weight:600;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:6px}
.stat-tile .value{font-size:24px;font-weight:700;color:var(--text);font-variant-numeric:tabular-nums}
.stat-tile .sub{font-size:11px;color:var(--muted);margin-top:2px}
.xp-bar{height:3px;background:var(--border);border-radius:2px;margin-top:8px}
.xp-fill{height:100%;background:linear-gradient(90deg,var(--accent),#E8C98A);border-radius:2px;transition:width 0.5s}

/* ─── GAME GRID ───────────────────────────────────── */
.section-title{font-size:11px;font-weight:700;letter-spacing:2px;color:var(--muted);text-transform:uppercase;margin-bottom:16px}
.game-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin-bottom:32px}
.game-card{
  padding:24px;background:var(--card);border:1px solid var(--border);
  border-radius:var(--radius-lg);cursor:pointer;
  transition:border-color 0.2s,transform 0.15s,box-shadow 0.2s;
  position:relative;overflow:hidden;
}
.game-card::before{
  content:'';position:absolute;inset:0;
  background:radial-gradient(circle at top right, var(--accent-glow), transparent 60%);
  opacity:0;transition:opacity 0.3s;
}
.game-card:hover{border-color:var(--border-hi);transform:translateY(-2px);box-shadow:0 12px 40px rgba(0,0,0,0.4)}
.game-card:hover::before{opacity:1}
.game-emoji{font-size:36px;margin-bottom:14px;display:block}
.game-name{font-size:18px;font-weight:700;margin-bottom:6px}
.game-desc{font-size:13px;color:var(--muted);line-height:1.5;margin-bottom:16px}
.game-reward{
  display:inline-flex;align-items:center;gap:5px;
  font-size:11px;font-weight:700;padding:4px 10px;
  background:rgba(255,215,0,0.08);border:1px solid rgba(255,215,0,0.15);
  border-radius:20px;color:var(--coin);
}

/* ════════════════════════════════════════════════════
   GAME PANELS
════════════════════════════════════════════════════ */
.panel{display:none}
.panel.active{display:block}

.game-panel{
  max-width:800px;margin:0 auto;
}
.game-header{
  display:flex;align-items:center;gap:16px;margin-bottom:24px;
}
.back-btn{
  width:36px;height:36px;border-radius:50%;
  background:var(--card);border:1px solid var(--border);
  color:var(--muted);font-size:18px;display:flex;align-items:center;justify-content:center;
  transition:all 0.15s;flex-shrink:0;
}
.back-btn:hover{color:var(--text);border-color:var(--border-hi)}
.game-panel-title{font-size:24px;font-weight:700}
.game-panel-sub{font-size:13px;color:var(--muted);margin-top:2px}

/* ─── MESSAGE BOX ─────────────────────────────────── */
.msg-box{
  padding:14px 18px;border-radius:var(--radius);
  background:var(--surface);border:1px solid var(--border);
  font-size:14px;font-weight:500;color:var(--text);margin-bottom:20px;
  text-align:center;min-height:48px;display:flex;align-items:center;justify-content:center;
}
.msg-box.win{border-color:rgba(57,217,138,0.3);background:rgba(57,217,138,0.05);color:var(--green)}
.msg-box.lose{border-color:rgba(255,91,91,0.3);background:rgba(255,91,91,0.05);color:var(--red)}

/* ════════════════════════════════════════════════════
   UNO GAME
════════════════════════════════════════════════════ */
.uno-field{
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);
  padding:24px;margin-bottom:20px;
}
.uno-top-area{
  display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;
}
.ai-info{
  display:flex;align-items:center;gap:10px;
  font-size:13px;color:var(--muted);
}
.ai-cards{display:flex;gap:4px}
.ai-card-back{
  width:32px;height:46px;border-radius:6px;
  background:linear-gradient(135deg,#1A2535,#0E1820);
  border:1px solid var(--border-hi);
}
.center-area{display:flex;align-items:center;justify-content:center;gap:20px}
.uno-discard{
  width:72px;height:104px;border-radius:10px;
  display:flex;align-items:center;justify-content:center;
  font-size:20px;font-weight:900;border:2px solid rgba(255,255,255,0.1);
  box-shadow:0 4px 20px rgba(0,0,0,0.4);
  transition:transform 0.2s;
}
.uno-deck-pile{
  width:72px;height:104px;border-radius:10px;cursor:pointer;
  background:linear-gradient(135deg,#1A2535,#0E1820);
  border:2px solid var(--border-hi);display:flex;align-items:center;justify-content:center;
  font-size:28px;transition:transform 0.15s,box-shadow 0.15s;
  box-shadow:0 4px 16px rgba(0,0,0,0.4);
}
.uno-deck-pile:hover{transform:scale(1.05);box-shadow:0 6px 24px rgba(0,0,0,0.5)}
.deck-count{font-size:10px;color:var(--muted);margin-top:4px;text-align:center}

.color-circle{
  width:28px;height:28px;border-radius:50%;
  border:2px solid rgba(255,255,255,0.2);
}

.player-hand{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-bottom:16px}
.uno-card{
  width:64px;height:92px;border-radius:9px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  font-weight:900;font-size:18px;cursor:pointer;
  border:2px solid rgba(255,255,255,0.08);
  transition:transform 0.15s,box-shadow 0.15s,border-color 0.15s;
  position:relative;user-select:none;flex-shrink:0;
  box-shadow:0 3px 12px rgba(0,0,0,0.3);
}
.uno-card:hover{transform:translateY(-8px);box-shadow:0 12px 28px rgba(0,0,0,0.5);border-color:rgba(255,255,255,0.3)}
.uno-card.unplayable{opacity:0.35;cursor:not-allowed}
.uno-card.unplayable:hover{transform:none}
.uno-card span{font-size:10px;opacity:0.7}
.uno-card-red{background:linear-gradient(145deg,#e63946,#9d0208)}
.uno-card-green{background:linear-gradient(145deg,#2d6a4f,#1b4332)}
.uno-card-blue{background:linear-gradient(145deg,#1d3557,#023e8a)}
.uno-card-yellow{background:linear-gradient(145deg,#e9c46a,#a47e1b);color:#000}
.uno-card-wild{background:linear-gradient(145deg,#2D1B69,#11001C)}

.color-picker{
  display:flex;gap:10px;justify-content:center;padding:16px;
  background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
  margin-bottom:16px;
}
.color-btn{
  width:44px;height:44px;border-radius:50%;border:3px solid rgba(255,255,255,0.1);
  cursor:pointer;transition:transform 0.15s,border-color 0.15s;
  font-size:0;
}
.color-btn:hover{transform:scale(1.15);border-color:rgba(255,255,255,0.4)}
.color-btn.selected{border-color:white;transform:scale(1.15)}
.color-btn.red{background:#e63946}
.color-btn.green{background:#2d6a4f}
.color-btn.blue{background:#1d3557}
.color-btn.yellow{background:#e9c46a}

.start-btn{
  width:100%;padding:14px;border-radius:var(--radius);border:none;
  background:linear-gradient(135deg,var(--accent),var(--accent-dim));
  color:#000;font-size:14px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
  transition:opacity 0.2s;
}
.start-btn:hover{opacity:0.85}

/* ════════════════════════════════════════════════════
   BLACKJACK
════════════════════════════════════════════════════ */
.bj-table{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius-lg);padding:28px;margin-bottom:20px;
}
.bj-zone{margin-bottom:20px}
.bj-zone-label{font-size:11px;font-weight:700;letter-spacing:1.5px;color:var(--muted);text-transform:uppercase;margin-bottom:12px}
.card-row{display:flex;gap:10px;flex-wrap:wrap}
.play-card{
  width:60px;height:86px;border-radius:8px;
  background:var(--card);border:1px solid var(--border-hi);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  font-size:16px;font-weight:700;gap:2px;
  box-shadow:0 3px 10px rgba(0,0,0,0.3);
}
.play-card .suit{font-size:18px}
.play-card.red-card{color:#e63946}
.play-card.black-card{color:var(--text)}
.play-card.hidden{background:linear-gradient(135deg,#1A2535,#0E1820);font-size:24px}
.bj-total{
  font-size:13px;color:var(--muted);margin-top:8px;
}
.bj-total span{color:var(--text);font-weight:600}

.action-row{display:flex;gap:10px}
.action-btn{
  flex:1;padding:13px;border-radius:var(--radius);border:1px solid var(--border);
  background:var(--card);color:var(--text);font-size:14px;font-weight:600;
  transition:all 0.15s;
}
.action-btn:hover{border-color:var(--accent);color:var(--accent);background:rgba(200,169,110,0.05)}
.action-btn.danger:hover{border-color:var(--red);color:var(--red);background:rgba(255,91,91,0.05)}

/* ════════════════════════════════════════════════════
   HIGHER OR LOWER
════════════════════════════════════════════════════ */
.hol-stage{
  text-align:center;padding:40px;
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);
  margin-bottom:20px;
}
.hol-card-display{
  display:inline-flex;flex-direction:column;align-items:center;justify-content:center;
  width:100px;height:145px;border-radius:12px;
  background:var(--card);border:2px solid var(--border-hi);
  margin:20px auto;font-size:28px;font-weight:700;gap:4px;
  box-shadow:0 6px 24px rgba(0,0,0,0.4);
}
.hol-card-display .rank{font-size:32px;font-weight:900}
.hol-card-display .suit{font-size:28px}
.hol-card-display.red-card{color:#e63946}
.streak-counter{
  display:inline-flex;align-items:center;gap:8px;
  font-size:28px;font-weight:700;
  margin-top:8px;color:var(--accent);
}
.hol-buttons{display:flex;gap:12px}
.hol-btn{
  flex:1;padding:16px;border-radius:var(--radius);border:1px solid var(--border);
  background:var(--card);font-size:15px;font-weight:700;
  color:var(--text);transition:all 0.15s;
}
.hol-btn:hover{border-color:var(--accent);background:rgba(200,169,110,0.08);color:var(--accent)}

/* ════════════════════════════════════════════════════
   DICE DUEL
════════════════════════════════════════════════════ */
.dice-stage{
  text-align:center;padding:48px 32px;
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);
  margin-bottom:20px;
}
.dice-arena{display:flex;align-items:center;justify-content:center;gap:32px;margin:24px 0}
.dice-side{text-align:center}
.dice-side .label{font-size:11px;letter-spacing:1.5px;color:var(--muted);text-transform:uppercase;margin-bottom:12px}
.dice-row{display:flex;gap:10px;justify-content:center}
.die{
  width:64px;height:64px;border-radius:12px;
  background:var(--card);border:2px solid var(--border-hi);
  display:flex;align-items:center;justify-content:center;
  font-size:30px;
  box-shadow:0 4px 16px rgba(0,0,0,0.4);
  transition:transform 0.3s;
}
.die.rolling{animation:roll 0.5s ease-out}
@keyframes roll{0%{transform:rotate(0) scale(1)}50%{transform:rotate(180deg) scale(1.2)}100%{transform:rotate(360deg) scale(1)}}
.vs-divider{font-size:13px;font-weight:700;letter-spacing:2px;color:var(--muted);margin-top:24px}
.dice-sum{
  font-size:36px;font-weight:900;color:var(--text);margin-top:4px;
  font-variant-numeric:tabular-nums;
}

/* ════════════════════════════════════════════════════
   SHOP
════════════════════════════════════════════════════ */
.shop-tabs{display:flex;gap:4px;margin-bottom:24px;background:var(--surface);padding:4px;border-radius:var(--radius);border:1px solid var(--border)}
.shop-tab{
  flex:1;padding:10px 16px;border-radius:8px;border:none;
  background:none;color:var(--muted);font-size:13px;font-weight:600;
  cursor:pointer;transition:all 0.15s;
}
.shop-tab.active{background:var(--card);color:var(--text);box-shadow:0 2px 8px rgba(0,0,0,0.3)}
.shop-tab:hover:not(.active){color:var(--text)}

.shop-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px}
.shop-item{
  padding:20px;background:var(--card);border:1px solid var(--border);
  border-radius:var(--radius);transition:border-color 0.2s,transform 0.15s;
  display:flex;flex-direction:column;
}
.shop-item:hover{border-color:var(--border-hi);transform:translateY(-2px)}
.shop-item.owned{border-color:rgba(57,217,138,0.25);background:rgba(57,217,138,0.03)}
.shop-emoji{font-size:28px;margin-bottom:10px;display:block}
.shop-name{font-size:14px;font-weight:700;margin-bottom:4px}
.shop-desc{font-size:12px;color:var(--muted);line-height:1.4;margin-bottom:14px;flex:1}
.shop-color-swatch{
  width:100%;height:32px;border-radius:8px;margin-bottom:10px;
  border:1px solid rgba(255,255,255,0.1);
}
.shop-price-row{display:flex;align-items:center;justify-content:space-between}
.shop-price{font-size:13px;font-weight:700;color:var(--coin);display:flex;align-items:center;gap:4px}
.shop-buy-btn{
  padding:7px 14px;border-radius:8px;border:1px solid var(--accent-dim);
  background:rgba(200,169,110,0.1);color:var(--accent);font-size:12px;font-weight:600;
  transition:all 0.15s;
}
.shop-buy-btn:hover{background:rgba(200,169,110,0.2)}
.shop-buy-btn.owned{border-color:rgba(57,217,138,0.3);background:rgba(57,217,138,0.08);color:var(--green);cursor:default}
.shop-buy-btn:disabled{opacity:0.4;cursor:not-allowed}

/* ─── TOASTS ──────────────────────────────────────── */
#toast-stack{position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;flex-direction:column;gap:8px}
.toast{
  padding:12px 18px;background:var(--card);border:1px solid var(--border);
  border-radius:var(--radius);font-size:13px;font-weight:500;
  animation:slideIn 0.25s ease;box-shadow:var(--shadow);
  max-width:280px;
}
.toast.good{border-color:rgba(57,217,138,0.3);color:var(--green)}
.toast.bad{border-color:rgba(255,91,91,0.3);color:var(--red)}
@keyframes slideIn{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}

/* ─── RESULT OVERLAY ──────────────────────────────── */
.result-overlay{
  position:fixed;inset:0;z-index:200;
  background:rgba(8,10,15,0.85);backdrop-filter:blur(10px);
  display:none;align-items:center;justify-content:center;
}
.result-overlay.show{display:flex}
.result-modal{
  width:360px;padding:48px 40px;text-align:center;
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius-lg);
  box-shadow:var(--shadow),0 0 0 1px rgba(200,169,110,0.05);
}
.result-icon{font-size:56px;margin-bottom:16px;display:block}
.result-title{font-size:28px;font-weight:700;margin-bottom:8px}
.result-sub{font-size:14px;color:var(--muted);margin-bottom:24px}
.result-reward{
  display:inline-flex;align-items:center;gap:8px;
  padding:10px 20px;border-radius:30px;
  background:rgba(255,215,0,0.08);border:1px solid rgba(255,215,0,0.2);
  font-size:18px;font-weight:700;color:var(--coin);margin-bottom:24px;
}
.result-buttons{display:flex;gap:10px}
.result-btn-play{
  flex:1;padding:12px;border-radius:var(--radius);border:none;
  background:linear-gradient(135deg,var(--accent),var(--accent-dim));
  color:#000;font-weight:700;font-size:14px;
}
.result-btn-home{
  flex:1;padding:12px;border-radius:var(--radius);
  border:1px solid var(--border);background:var(--card);
  color:var(--text);font-weight:600;font-size:14px;
}

/* ─── RESPONSIVE ─────────────────────────────────── */
@media(max-width:680px){
  .sidebar{display:none}
  .stat-bar{flex-wrap:wrap}
  .topbar{padding:0 16px}
  .content{padding:20px 16px}
  .player-hand{gap:5px}
  .uno-card{width:52px;height:76px;font-size:15px}
}
</style>
</head>
<body>

<!-- ══════════════════════════════════════════════════
     LOGIN
══════════════════════════════════════════════════ -->
<div id="login-screen" class="screen active">
  <div class="login-card">
    <div class="logo">
      <div class="logo-mark">🃏</div>
      <h1>ARCADIA</h1>
      <p>PREMIUM GAME LOUNGE</p>
    </div>
    <div class="field">
      <label>Username</label>
      <input type="text" id="username-input" placeholder="Enter your name" maxlength="20" autocomplete="off">
    </div>
    <button class="btn-primary" onclick="doLogin()">Enter the Lounge</button>
    <p class="login-note">New players start with <strong style="color:var(--coin)">500 coins</strong>.<br>Win games to earn more.</p>
  </div>
</div>

<!-- ══════════════════════════════════════════════════
     APP
══════════════════════════════════════════════════ -->
<div id="app-screen" class="screen">

  <!-- TOPBAR -->
  <div class="topbar">
    <div class="topbar-logo">ARCADIA</div>
    <div class="topbar-user">
      <div class="user-badge">
        <span class="user-icon" id="top-icon"></span>
        <span class="user-name" id="top-name"></span>
        <div class="user-tags" id="top-tags"></div>
      </div>
      <div class="coin-display">
        <span class="coin-icon">🪙</span>
        <span id="top-coins">0</span>
      </div>
    </div>
  </div>

  <div class="main-layout">
    <!-- SIDEBAR -->
    <nav class="sidebar">
      <div class="nav-section">Games</div>
      <button class="nav-item active" onclick="showPanel('lobby')" id="nav-lobby">
        <span class="nav-icon">🏠</span>Lobby
      </button>
      <button class="nav-item" onclick="showPanel('uno')" id="nav-uno">
        <span class="nav-icon">🃏</span>UNO <span class="nav-badge">+200</span>
      </button>
      <button class="nav-item" onclick="showPanel('blackjack')" id="nav-blackjack">
        <span class="nav-icon">🂡</span>Blackjack <span class="nav-badge">+150</span>
      </button>
      <button class="nav-item" onclick="showPanel('hol')" id="nav-hol">
        <span class="nav-icon">🔢</span>Hi or Lo <span class="nav-badge">+30</span>
      </button>
      <button class="nav-item" onclick="showPanel('dice')" id="nav-dice">
        <span class="nav-icon">🎲</span>Dice Duel <span class="nav-badge">+80</span>
      </button>
      <div class="nav-section" style="margin-top:12px">Account</div>
      <button class="nav-item" onclick="showPanel('shop')" id="nav-shop">
        <span class="nav-icon">🛍️</span>Shop
      </button>
    </nav>

    <!-- CONTENT -->
    <main class="content">

      <!-- ── LOBBY ───────────────────────────────── -->
      <div id="panel-lobby" class="panel active">
        <div class="stat-bar" id="stats-bar"></div>
        <div class="section-title">Choose a game</div>
        <div class="game-grid">
          <div class="game-card" onclick="showPanel('uno')">
            <span class="game-emoji">🃏</span>
            <div class="game-name">UNO</div>
            <div class="game-desc">Classic card battle. Match colours and values against the AI. Specials, wilds — the works.</div>
            <span class="game-reward">🪙 200 coins per win</span>
          </div>
          <div class="game-card" onclick="showPanel('blackjack')">
            <span class="game-emoji">🂡</span>
            <div class="game-name">Blackjack</div>
            <div class="game-desc">Get closer to 21 than the dealer without busting. A pure test of nerve.</div>
            <span class="game-reward">🪙 150 coins per win</span>
          </div>
          <div class="game-card" onclick="showPanel('hol')">
            <span class="game-emoji">🔢</span>
            <div class="game-name">Higher or Lower</div>
            <div class="game-desc">Each correct guess builds your streak. How far can you go before it breaks?</div>
            <span class="game-reward">🪙 30 coins per correct</span>
          </div>
          <div class="game-card" onclick="showPanel('dice')">
            <span class="game-emoji">🎲</span>
            <div class="game-name">Dice Duel</div>
            <div class="game-desc">Roll two dice against the AI. Highest total wins. Fast, clean, decisive.</div>
            <span class="game-reward">🪙 80 coins per win</span>
          </div>
        </div>
      </div>

      <!-- ── UNO PANEL ─────────────────────────── -->
      <div id="panel-uno" class="panel">
        <div class="game-header">
          <button class="back-btn" onclick="showPanel('lobby')">←</button>
          <div>
            <div class="game-panel-title">🃏 UNO</div>
            <div class="game-panel-sub">First to empty their hand wins</div>
          </div>
        </div>

        <div id="uno-start">
          <div style="text-align:center;padding:60px 0">
            <div style="font-size:64px;margin-bottom:20px">🃏</div>
            <div style="font-size:20px;font-weight:700;margin-bottom:8px">Ready to play UNO?</div>
            <div style="font-size:14px;color:var(--muted);margin-bottom:28px">You vs the AI. First to 0 cards wins 200 coins.</div>
            <button class="start-btn" style="max-width:260px;margin:0 auto;display:block" onclick="unoNew()">Deal Cards</button>
          </div>
        </div>

        <div id="uno-game" style="display:none">
          <div class="msg-box" id="uno-msg">Loading…</div>
          <div class="uno-field">
            <div class="uno-top-area">
              <div class="ai-info">
                <span>🤖 AI</span>
                <div class="ai-cards" id="ai-cards-display"></div>
                <span id="ai-count" style="font-size:13px;color:var(--muted)"></span>
              </div>
              <div style="display:flex;align-items:center;gap:8px">
                <div class="color-circle" id="chosen-color-dot"></div>
                <span id="color-label" style="font-size:12px;color:var(--muted)"></span>
              </div>
            </div>
            <div class="center-area">
              <div>
                <div class="uno-discard" id="uno-top-card"></div>
                <div class="deck-count" id="uno-deck-count"></div>
              </div>
              <div>
                <div class="uno-deck-pile" id="uno-draw-btn" onclick="unoDraw()">🃏</div>
                <div class="deck-count">Draw</div>
              </div>
            </div>
          </div>

          <div id="color-picker-area" style="display:none">
            <div style="text-align:center;margin-bottom:8px;font-size:13px;color:var(--muted);font-weight:600">Choose a colour for your Wild</div>
            <div class="color-picker">
              <div class="color-btn red selected" data-color="red" onclick="pickColor('red',this)"></div>
              <div class="color-btn green" data-color="green" onclick="pickColor('green',this)"></div>
              <div class="color-btn blue" data-color="blue" onclick="pickColor('blue',this)"></div>
              <div class="color-btn yellow" data-color="yellow" onclick="pickColor('yellow',this)"></div>
            </div>
          </div>

          <div class="player-hand" id="uno-hand"></div>

          <div style="text-align:center;margin-top:8px">
            <button class="start-btn" style="max-width:200px;display:inline-block" onclick="unoNew()">New Game</button>
          </div>
        </div>
      </div>

      <!-- ── BLACKJACK PANEL ─────────────────────── -->
      <div id="panel-blackjack" class="panel">
        <div class="game-header">
          <button class="back-btn" onclick="showPanel('lobby')">←</button>
          <div>
            <div class="game-panel-title">🂡 Blackjack</div>
            <div class="game-panel-sub">Beat the dealer. Bet 100 coins per round.</div>
          </div>
        </div>

        <div id="bj-start">
          <div style="text-align:center;padding:60px 0">
            <div style="font-size:64px;margin-bottom:20px">🂡</div>
            <div style="font-size:20px;font-weight:700;margin-bottom:8px">Ready to play Blackjack?</div>
            <div style="font-size:14px;color:var(--muted);margin-bottom:28px">Get closer to 21 than the dealer. Win: +150 coins.</div>
            <button class="start-btn" style="max-width:260px;margin:0 auto;display:block" onclick="bjNew()">Deal Hand</button>
          </div>
        </div>

        <div id="bj-game" style="display:none">
          <div class="msg-box" id="bj-msg"></div>
          <div class="bj-table">
            <div class="bj-zone">
              <div class="bj-zone-label">Dealer's Hand</div>
              <div class="card-row" id="dealer-hand"></div>
              <div class="bj-total">Total: <span id="dealer-total">?</span></div>
            </div>
            <div class="bj-zone">
              <div class="bj-zone-label">Your Hand</div>
              <div class="card-row" id="player-hand-bj"></div>
              <div class="bj-total">Total: <span id="player-total-bj">0</span></div>
            </div>
          </div>
          <div class="action-row" id="bj-actions">
            <button class="action-btn" onclick="bjAction('hit')">Hit</button>
            <button class="action-btn danger" onclick="bjAction('stand')">Stand</button>
          </div>
          <div style="margin-top:12px">
            <button class="start-btn" onclick="bjNew()">New Hand</button>
          </div>
        </div>
      </div>

      <!-- ── HIGHER OR LOWER ───────────────────── -->
      <div id="panel-hol" class="panel">
        <div class="game-header">
          <button class="back-btn" onclick="showPanel('lobby')">←</button>
          <div>
            <div class="game-panel-title">🔢 Higher or Lower</div>
            <div class="game-panel-sub">Each correct guess earns coins. Build your streak.</div>
          </div>
        </div>

        <div id="hol-start">
          <div style="text-align:center;padding:60px 0">
            <div style="font-size:64px;margin-bottom:20px">🔢</div>
            <div style="font-size:20px;font-weight:700;margin-bottom:8px">Higher or Lower?</div>
            <div style="font-size:14px;color:var(--muted);margin-bottom:28px">Will the next card be higher or lower? Each correct guess: +30×streak coins.</div>
            <button class="start-btn" style="max-width:260px;margin:0 auto;display:block" onclick="holNew()">Start Game</button>
          </div>
        </div>

        <div id="hol-game" style="display:none">
          <div class="hol-stage">
            <div style="font-size:12px;letter-spacing:2px;color:var(--muted);text-transform:uppercase;margin-bottom:8px">Current Card</div>
            <div class="hol-card-display" id="hol-card-display">
              <div class="rank" id="hol-rank">—</div>
              <div class="suit" id="hol-suit">—</div>
            </div>
            <div>
              <div style="font-size:12px;color:var(--muted);margin-bottom:4px">STREAK</div>
              <div class="streak-counter" id="hol-streak">0 🔥</div>
            </div>
          </div>
          <div class="msg-box" id="hol-msg"></div>
          <div class="hol-buttons">
            <button class="hol-btn" id="hol-higher" onclick="holGuess('higher')">⬆️ Higher</button>
            <button class="hol-btn" id="hol-lower" onclick="holGuess('lower')">⬇️ Lower</button>
          </div>
          <div style="margin-top:12px">
            <button class="start-btn" onclick="holNew()">New Game</button>
          </div>
        </div>
      </div>

      <!-- ── DICE DUEL ─────────────────────────── -->
      <div id="panel-dice" class="panel">
        <div class="game-header">
          <button class="back-btn" onclick="showPanel('lobby')">←</button>
          <div>
            <div class="game-panel-title">🎲 Dice Duel</div>
            <div class="game-panel-sub">Roll 2 dice. Beat the AI. Win 80 coins.</div>
          </div>
        </div>
        <div class="dice-stage">
          <div class="dice-arena">
            <div class="dice-side">
              <div class="label">You</div>
              <div class="dice-row">
                <div class="die" id="d1">⚀</div>
                <div class="die" id="d2">⚀</div>
              </div>
              <div class="dice-sum" id="player-sum">—</div>
            </div>
            <div class="vs-divider">VS</div>
            <div class="dice-side">
              <div class="label">AI</div>
              <div class="dice-row">
                <div class="die" id="d3">⚀</div>
                <div class="die" id="d4">⚀</div>
              </div>
              <div class="dice-sum" id="ai-sum">—</div>
            </div>
          </div>
        </div>
        <div class="msg-box" id="dice-msg">Press Roll to challenge the AI!</div>
        <button class="start-btn" onclick="diceRoll()">🎲 Roll Dice</button>
      </div>

      <!-- ── SHOP ──────────────────────────────── -->
      <div id="panel-shop" class="panel">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px">
          <div>
            <div style="font-size:24px;font-weight:700;margin-bottom:4px">🛍️ Shop</div>
            <div style="font-size:13px;color:var(--muted)">Customise your identity in the lounge</div>
          </div>
          <div class="coin-display" style="font-size:16px;padding:10px 18px">
            <span>🪙</span><span id="shop-coins">0</span>
          </div>
        </div>
        <div class="shop-tabs">
          <button class="shop-tab active" onclick="shopTab('tags',this)">🏷️ Tags</button>
          <button class="shop-tab" onclick="shopTab('colors',this)">🎨 Name Colours</button>
          <button class="shop-tab" onclick="shopTab('icons',this)">✨ Icons</button>
        </div>
        <div id="shop-tags" class="shop-section">
          <div class="shop-grid" id="tags-grid"></div>
        </div>
        <div id="shop-colors" class="shop-section" style="display:none">
          <div class="shop-grid" id="colors-grid"></div>
        </div>
        <div id="shop-icons" class="shop-section" style="display:none">
          <div class="shop-grid" id="icons-grid"></div>
        </div>
      </div>

    </main>
  </div>
</div>

<!-- RESULT OVERLAY -->
<div class="result-overlay" id="result-overlay">
  <div class="result-modal">
    <span class="result-icon" id="res-icon"></span>
    <div class="result-title" id="res-title"></div>
    <div class="result-sub" id="res-sub"></div>
    <div class="result-reward" id="res-reward"></div>
    <div class="result-buttons">
      <button class="result-btn-play" id="res-play-btn">Play Again</button>
      <button class="result-btn-home" onclick="hideResult();showPanel('lobby')">Lobby</button>
    </div>
  </div>
</div>

<!-- TOAST STACK -->
<div id="toast-stack"></div>

<script>
/* ─── STATE ───────────────────────────────────────── */
let player = null;
let username = '';
let shopCatalog = null;
let unoSelectedColor = 'red';
let unoWildPending = false;
let unoGameActive = false;
let holActive = false;
let bjActive = false;

const DICE_FACES = ['⚀','⚁','⚂','⚃','⚄','⚅'];
const UNO_COLOR_MAP = {red:'#e63946',green:'#2d6a4f',blue:'#1d3557',yellow:'#e9c46a',wild:'#2D1B69'};
const UNO_TEXT_MAP = {yellow:'#000000'};

/* ─── LOGIN ───────────────────────────────────────── */
document.getElementById('username-input').addEventListener('keydown', e => {
  if(e.key === 'Enter') doLogin();
});

async function doLogin(){
  const name = document.getElementById('username-input').value.trim();
  if(!name) return;
  const res = await fetch('/api/login', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({username:name})});
  const d = await res.json();
  if(d.error){ toast(d.error,'bad'); return; }
  username = d.username;
  player = d.player;
  document.getElementById('login-screen').classList.remove('active');
  document.getElementById('app-screen').classList.add('active');
  updateUI();
  loadShopCatalog();
  toast('Welcome back, ' + username + '! 🎉','good');
}

/* ─── UI UPDATE ──────────────────────────────────── */
function updateUI(){
  if(!player) return;
  document.getElementById('top-coins').textContent = player.coins.toLocaleString();
  document.getElementById('shop-coins').textContent = player.coins.toLocaleString();

  const nameEl = document.getElementById('top-name');
  nameEl.textContent = (player.icon || '') + ' ' + username;
  nameEl.style.color = player.name_color || '#fff';

  const tagsEl = document.getElementById('top-tags');
  tagsEl.innerHTML = '';
  (player.tags||[]).slice(0,3).forEach(tid => {
    const item = findShopItem(tid);
    if(item){ const p = document.createElement('span'); p.className='tag-pill'; p.textContent=item.emoji+' '+item.name; tagsEl.appendChild(p); }
  });

  document.getElementById('top-icon').textContent = player.icon || '';
  renderStatsBar();
  if(document.getElementById('panel-shop').classList.contains('active')) renderShop();
}

function renderStatsBar(){
  const xpPct = Math.min(100, Math.round((player.xp/(player.level*100))*100));
  document.getElementById('stats-bar').innerHTML = `
    <div class="stat-tile">
      <div class="label">Coins</div>
      <div class="value" style="color:var(--coin)">🪙 ${player.coins.toLocaleString()}</div>
      <div class="sub">Earn by winning games</div>
    </div>
    <div class="stat-tile">
      <div class="label">Level</div>
      <div class="value">${player.level}</div>
      <div class="xp-bar"><div class="xp-fill" style="width:${xpPct}%"></div></div>
      <div class="sub">${player.xp} / ${player.level*100} XP</div>
    </div>
    <div class="stat-tile">
      <div class="label">Wins</div>
      <div class="value" style="color:var(--green)">${player.wins}</div>
      <div class="sub">${player.losses} losses</div>
    </div>
    <div class="stat-tile">
      <div class="label">Win Rate</div>
      <div class="value">${player.wins+player.losses ? Math.round(player.wins/(player.wins+player.losses)*100)+'%' : '—'}</div>
      <div class="sub">${player.wins+player.losses} games</div>
    </div>
  `;
}

/* ─── PANEL NAV ───────────────────────────────────── */
function showPanel(id){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('panel-'+id).classList.add('active');
  const nav = document.getElementById('nav-'+id);
  if(nav) nav.classList.add('active');
  refreshMe();
}

async function refreshMe(){
  const res = await fetch('/api/me');
  if(res.ok){ const d = await res.json(); player = d.player; updateUI(); }
}

/* ─── SHOP ────────────────────────────────────────── */
async function loadShopCatalog(){
  const res = await fetch('/api/shop/catalog');
  shopCatalog = await res.json();
}

function findShopItem(id){
  if(!shopCatalog) return null;
  for(const cat of Object.values(shopCatalog)){
    const found = cat.find(i=>i.id===id);
    if(found) return found;
  }
  return null;
}

function shopTab(tab, el){
  document.querySelectorAll('.shop-tab').forEach(t=>t.classList.remove('active'));
  el.classList.add('active');
  document.querySelectorAll('.shop-section').forEach(s=>s.style.display='none');
  document.getElementById('shop-'+tab).style.display='block';
  renderShopSection(tab);
}

function renderShop(){
  renderShopSection('tags');
}

function renderShopSection(section){
  if(!shopCatalog||!player) return;
  const items = shopCatalog[section] || [];
  const gridId = section.replace('colors','colors') + '-grid';
  const grid = document.getElementById(gridId) || document.getElementById(section+'-grid');
  if(!grid) return;
  grid.innerHTML = '';
  items.forEach(item => {
    const owned = isOwned(item);
    const card = document.createElement('div');
    card.className = 'shop-item' + (owned ? ' owned' : '');
    const colorSwatch = item.hex ? `<div class="shop-color-swatch" style="background:${item.hex}"></div>` : '';
    const emoji = item.emoji ? `<span class="shop-emoji">${item.emoji}</span>` : '';
    card.innerHTML = `
      ${emoji}${colorSwatch}
      <div class="shop-name">${item.name}</div>
      <div class="shop-desc">${item.desc}</div>
      <div class="shop-price-row">
        <div class="shop-price">🪙 ${item.price.toLocaleString()}</div>
        <button class="shop-buy-btn ${owned?'owned':''}" onclick="buyItem('${item.id}')" ${owned?'disabled':''}>
          ${owned ? '✓ Owned' : 'Buy'}
        </button>
      </div>`;
    grid.appendChild(card);
  });
}

function isOwned(item){
  if(!player) return false;
  if(item.id.startsWith('tag_')) return (player.tags||[]).includes(item.id);
  if(item.id.startsWith('col_')) return player.name_color === item.hex;
  if(item.id.startsWith('icon_')) return player.icon === item.emoji;
  return false;
}

async function buyItem(id){
  const res = await fetch('/api/shop/buy',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({item_id:id})});
  const d = await res.json();
  if(d.error){ toast(d.error,'bad'); return; }
  player = d.player;
  updateUI();
  renderShop();
  const item = findShopItem(id);
  toast('🎉 Purchased ' + (item ? item.name : id) + '!', 'good');
}

/* ─── UNO ─────────────────────────────────────────── */
async function unoNew(){
  const res = await fetch('/api/uno/new',{method:'POST'});
  const d = await res.json();
  document.getElementById('uno-start').style.display='none';
  document.getElementById('uno-game').style.display='block';
  unoGameActive = true;
  renderUno(d);
}

async function unoPlayCard(idx){
  if(!unoGameActive) return;
  const hand = currentUnoHand;
  const card = hand[idx];
  if(card.color === 'wild'){
    unoWildPending = true;
    unoWildIdx = idx;
    document.getElementById('color-picker-area').style.display='block';
    return;
  }
  await sendUnoPlay(idx, unoSelectedColor);
}

let unoWildIdx = -1;
let currentUnoHand = [];

async function confirmWildPlay(){
  if(unoWildPending){
    unoWildPending = false;
    document.getElementById('color-picker-area').style.display='none';
    await sendUnoPlay(unoWildIdx, unoSelectedColor);
  }
}

async function sendUnoPlay(idx, color){
  const res = await fetch('/api/uno/play',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action:'play',card_index:idx,chosen_color:color})});
  const d = await res.json();
  renderUno(d);
  if(d.status==='win') showResult('win','You Win!','Your hand is empty!',200,'unoNew');
  if(d.status==='lose') showResult('lose','AI Wins','Better luck next time.',20,'unoNew');
  refreshMe();
}

async function unoDraw(){
  if(!unoGameActive) return;
  const res = await fetch('/api/uno/play',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action:'draw'})});
  const d = await res.json();
  renderUno(d);
  refreshMe();
}

function pickColor(color, el){
  unoSelectedColor = color;
  document.querySelectorAll('.color-btn').forEach(b=>b.classList.remove('selected'));
  el.classList.add('selected');
  if(unoWildPending) confirmWildPlay();
}

function renderUno(d){
  if(!d) return;
  currentUnoHand = d.hand || [];

  const msgEl = document.getElementById('uno-msg');
  msgEl.textContent = d.message || '';
  msgEl.className = 'msg-box' + (d.status==='win'?' win':d.status==='lose'?' lose':'');

  // top card
  const top = d.top;
  const topEl = document.getElementById('uno-top-card');
  const bg = UNO_COLOR_MAP[top.color] || '#333';
  const txt = UNO_TEXT_MAP[top.color] || '#fff';
  topEl.style.background = `linear-gradient(145deg, ${bg}, ${shadeColor(bg,-30)})`;
  topEl.style.color = txt;
  topEl.textContent = top.value;

  // chosen color dot
  const dot = document.getElementById('chosen-color-dot');
  dot.style.background = UNO_COLOR_MAP[d.chosen_color] || '#fff';
  document.getElementById('color-label').textContent = (d.chosen_color||'').toUpperCase();

  // deck count
  document.getElementById('uno-deck-count').textContent = d.deck_count + ' left';

  // AI cards
  const aiCount = d.ai_count || 0;
  document.getElementById('ai-count').textContent = aiCount + ' cards';
  const aiDisplay = document.getElementById('ai-cards-display');
  aiDisplay.innerHTML = '';
  for(let i=0;i<Math.min(aiCount,10);i++){
    const c = document.createElement('div');
    c.className = 'ai-card-back';
    aiDisplay.appendChild(c);
  }

  // player hand
  const handEl = document.getElementById('uno-hand');
  handEl.innerHTML = '';
  (d.hand||[]).forEach((card,i)=>{
    const el = document.createElement('div');
    const canPlay = canPlayCard(card, d.top, d.chosen_color);
    el.className = 'uno-card uno-card-' + card.color + (canPlay ? '' : ' unplayable');
    const col = UNO_TEXT_MAP[card.color] || '#fff';
    el.style.color = col;
    el.innerHTML = `${card.value}<span>${card.color !== 'wild' ? card.color : 'WILD'}</span>`;
    if(canPlay) el.onclick = () => unoPlayCard(i);
    handEl.appendChild(el);
  });

  if(d.status !== 'playing') unoGameActive = false;
}

function canPlayCard(card, top, chosenColor){
  if(card.color==='wild') return true;
  if(card.color===chosenColor) return true;
  if(card.value===top.value) return true;
  return false;
}

function shadeColor(hex, pct){
  const n = parseInt(hex.slice(1), 16);
  const r = Math.min(255, Math.max(0, (n>>16) + pct));
  const g = Math.min(255, Math.max(0, ((n>>8)&0xFF) + pct));
  const b = Math.min(255, Math.max(0, (n&0xFF) + pct));
  return `rgb(${r},${g},${b})`;
}

/* ─── BLACKJACK ──────────────────────────────────── */
async function bjNew(){
  const res = await fetch('/api/bj/new',{method:'POST'});
  const d = await res.json();
  document.getElementById('bj-start').style.display='none';
  document.getElementById('bj-game').style.display='block';
  document.getElementById('bj-actions').style.display='flex';
  bjActive = true;
  renderBj(d.player, d.dealer_visible, d.message, false, null, '?');
}

async function bjAction(action){
  if(!bjActive) return;
  const res = await fetch('/api/bj/action',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action})});
  const d = await res.json();
  const reveal = action === 'stand' || d.status !== 'playing';
  renderBj(d.player, d.dealer, d.message, reveal, d.status, d.dealer_total);
  if(d.status !== 'playing'){
    bjActive = false;
    document.getElementById('bj-actions').style.display='none';
    refreshMe();
    setTimeout(()=>{
      if(d.status==='win') showResult('win','You Win!','Beat the dealer!',150,'bjNew');
      else if(d.status==='lose') showResult('lose','Dealer Wins','Better luck next time.',15,'bjNew');
      else showResult('draw','Push!','Tie game. Your bet is returned.',0,'bjNew');
    }, 600);
  }
}

function renderBj(playerHand, dealerHand, msg, revealDealer, status, dealerTotal){
  const msgEl = document.getElementById('bj-msg');
  msgEl.textContent = msg;
  msgEl.className = 'msg-box' + (status==='win'?' win':status==='lose'?' lose':'');

  const RED_SUITS = ['♥','♦'];
  const renderHand = (cards, hidden) => cards.map((c,i) => {
    if(hidden && i>0) return `<div class="play-card hidden">🂠</div>`;
    const isRed = RED_SUITS.includes(c.suit);
    return `<div class="play-card ${isRed?'red-card':'black-card'}"><div>${c.rank}</div><div class="suit">${c.suit}</div></div>`;
  }).join('');

  const showHidden = !revealDealer && dealerHand.length === 1;
  document.getElementById('dealer-hand').innerHTML = renderHand(dealerHand, !revealDealer && dealerHand.length > 1);
  document.getElementById('player-hand-bj').innerHTML = renderHand(playerHand, false);
  document.getElementById('dealer-total').textContent = revealDealer ? dealerTotal : '?';
  
  let pv = 0;
  playerHand.forEach(c => {
    if(['J','Q','K'].includes(c.rank)) pv+=10;
    else if(c.rank==='A') pv+=11;
    else pv+=parseInt(c.rank);
  });
  document.getElementById('player-total-bj').textContent = pv > 21 ? pv + ' (BUST)' : pv;
}

/* ─── HIGHER OR LOWER ────────────────────────────── */
async function holNew(){
  const res = await fetch('/api/hol/new',{method:'POST'});
  const d = await res.json();
  document.getElementById('hol-start').style.display='none';
  document.getElementById('hol-game').style.display='block';
  holActive = true;
  enableHolButtons();
  renderHolCard(d.current, d.streak, d.message, 'playing');
}

async function holGuess(dir){
  if(!holActive) return;
  const res = await fetch('/api/hol/guess',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({guess:dir})});
  const d = await res.json();
  renderHolCard(d.next, d.streak, d.message, d.status);
  refreshMe();
  if(d.status === 'lose'){
    holActive = false;
    disableHolButtons();
    setTimeout(()=>showResult('lose','Streak Broken!',`You reached ${d.streak} in a row.`,d.streak*15,'holNew'),700);
  }
}

function renderHolCard(card, streak, msg, status){
  const RED_SUITS = ['♥','♦'];
  const isRed = RED_SUITS.includes(card.suit);
  const disp = document.getElementById('hol-card-display');
  disp.className = 'hol-card-display' + (isRed?' red-card':'');
  document.getElementById('hol-rank').textContent = card.rank;
  document.getElementById('hol-suit').textContent = card.suit;
  document.getElementById('hol-streak').textContent = streak + (streak >= 5 ? ' 🔥' : '');
  const msgEl = document.getElementById('hol-msg');
  msgEl.textContent = msg;
  msgEl.className = 'msg-box' + (status==='playing'?'':status==='lose'?' lose':' win');
}

function enableHolButtons(){ document.getElementById('hol-higher').disabled=false; document.getElementById('hol-lower').disabled=false; }
function disableHolButtons(){ document.getElementById('hol-higher').disabled=true; document.getElementById('hol-lower').disabled=true; }

/* ─── DICE ────────────────────────────────────────── */
async function diceRoll(){
  ['d1','d2','d3','d4'].forEach(id=>{
    const el = document.getElementById(id);
    el.classList.remove('rolling');
    void el.offsetWidth;
    el.classList.add('rolling');
  });
  await new Promise(r=>setTimeout(r,200));
  const res = await fetch('/api/dice/roll',{method:'POST'});
  const d = await res.json();
  document.getElementById('d1').textContent = DICE_FACES[d.player[0]-1];
  document.getElementById('d2').textContent = DICE_FACES[d.player[1]-1];
  document.getElementById('d3').textContent = DICE_FACES[d.ai[0]-1];
  document.getElementById('d4').textContent = DICE_FACES[d.ai[1]-1];
  document.getElementById('player-sum').textContent = d.player[0]+d.player[1];
  document.getElementById('ai-sum').textContent = d.ai[0]+d.ai[1];
  const msgEl = document.getElementById('dice-msg');
  msgEl.textContent = d.message;
  msgEl.className = 'msg-box' + (d.result==='win'?' win':d.result==='lose'?' lose':'');
  refreshMe();
  if(d.result !== 'draw') setTimeout(()=>{
    if(d.result==='win') showResult('win','You Win!','Your dice rolled higher!',80,'diceRoll');
    else showResult('lose','AI Wins','The dice weren\'t in your favour.',0,'diceRoll');
  },800);
}

/* ─── RESULT OVERLAY ──────────────────────────────── */
function showResult(type, title, sub, coins, playAgainFn){
  const icons = {win:'🎉',lose:'💀',draw:'🤝'};
  document.getElementById('res-icon').textContent = icons[type]||'🎮';
  document.getElementById('res-title').textContent = title;
  document.getElementById('res-sub').textContent = sub;
  document.getElementById('res-reward').textContent = coins > 0 ? '🪙 +' + coins + ' coins' : coins === 0 ? 'No coins lost' : '—';
  document.getElementById('res-reward').style.display = 'inline-flex';
  document.getElementById('res-play-btn').onclick = () => { hideResult(); window[playAgainFn](); };
  document.getElementById('result-overlay').classList.add('show');
}
function hideResult(){ document.getElementById('result-overlay').classList.remove('show'); }

/* ─── TOAST ───────────────────────────────────────── */
function toast(msg, type=''){
  const el = document.createElement('div');
  el.className = 'toast' + (type ? ' '+type : '');
  el.textContent = msg;
  document.getElementById('toast-stack').appendChild(el);
  setTimeout(()=>el.remove(), 3000);
}

/* ─── INIT ────────────────────────────────────────── */
renderShop;
</script>
</body>
</html>
