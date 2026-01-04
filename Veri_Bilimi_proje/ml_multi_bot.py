import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


HISSE_LISTESI = [
    "THYAO.IS", "GARAN.IS", "ASELS.IS", "SISE.IS", 
    "KCHOL.IS", "BIMAS.IS", "AKBNK.IS", "EREGL.IS"
]

def model_egit_ve_tahmin_et(hisse_kodu):
    """
    Tek bir hisse için veriyi çeker modeli eğitir ve tahmini döndürür
    """
    try:
        # 1. VERİ ÇEKME
        hisse = yf.Ticker(hisse_kodu)
        veri = hisse.history(period="2y")
        
        if len(veri) < 200: # Yeterli veri yoksa atla
            return None

       
        veri["SMA_10"] = veri["Close"].rolling(window=10).mean()
        veri["SMA_50"] = veri["Close"].rolling(window=50).mean()
        
       
        delta = veri["Close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        veri["RSI"] = 100 - (100 / (1 + rs))
        
        veri["Degisim"] = veri["Close"].pct_change()
        
        # Veriyi Temizle
        veri = veri.dropna()

        # 3. ETİKETLEME (HEDEF)
        # Yarın fiyat artarsa 1, artmazsa 0
        veri["Hedef"] = np.where(veri["Close"].shift(-1) > veri["Close"], 1, 0)

        # 4. EĞİTİM
        ozellikler = ["Close", "Volume", "SMA_10", "SMA_50", "RSI", "Degisim"]
        X = veri[ozellikler]
        y = veri["Hedef"]

        # Son satır (Bugün) hariç eğitim yap (Çünkü bugünün Hedef'ini bilmiyoruz, yarın belli olacak)
        X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, shuffle=False)
        
        model = RandomForestClassifier(n_estimators=100, min_samples_split=10, random_state=42)
        model.fit(X_train, y_train)

        # Başarı Oranını Ölç
        tahminler = model.predict(X_test)
        basari = accuracy_score(y_test, tahminler)

        # 5. GELECEK TAHMİNİ (YARIN İÇİN)
        bugunun_verisi = X.iloc[[-1]] # En son veri
        tahmin = model.predict(bugunun_verisi)[0]
        olasilik = model.predict_proba(bugunun_verisi)[0] # [Düşüş %, Yükseliş %]

        return {
            "Hisse": hisse_kodu,
            "Basari": basari * 100,
            "Tahmin": "YÜKSELİŞ 📈" if tahmin == 1 else "DÜŞÜŞ 📉",
            "Guven": olasilik[1] * 100 if tahmin == 1 else olasilik[0] * 100,
            "Son_Fiyat": veri["Close"].iloc[-1]
        }

    except Exception as e:
        print(f"Hata ({hisse_kodu}): {e}")
        return None

# --- ANA PROGRAM ---
print(f" Portföy Analizi Başlıyor... ({len(HISSE_LISTESI)} Hisse)")
print("=" * 75)
print(f"{'HİSSE':<10} | {'FİYAT':<10} | {'TAHMİN':<12} | {'GÜVEN %':<10} | {'MODEL BAŞARISI':<15}")
print("-" * 75)

yukselecekler = []

for sembol in HISSE_LISTESI:
    sonuc = model_egit_ve_tahmin_et(sembol)
    
    if sonuc:
        print(f"{sonuc['Hisse']:<10} | {sonuc['Son_Fiyat']:<10.2f} | {sonuc['Tahmin']:<12} | %{sonuc['Guven']:<9.1f} | %{sonuc['Basari']:.1f}")
        
        # Eğer tahmin Yükseliş ise ve Güven %60'tan fazlaysa listeye al
        if "YÜKSELİŞ" in sonuc["Tahmin"] and sonuc["Guven"] > 60:
            yukselecekler.append(sonuc)

print("=" * 75)
print("\n GÜNÜN YILDIZLARI (Yüksek Güvenli Alış Sinyalleri):")
if not yukselecekler:
    print(" Bugün için güçlü bir fırsat bulunamadı.")
else:
    for y in yukselecekler:
        print(f" {y['Hisse']} (Güven: %{y['Guven']:.1f})")