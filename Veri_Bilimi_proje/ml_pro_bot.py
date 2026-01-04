import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- AYARLAR ---
HISSE_LISTESI = ["THYAO.IS", "GARAN.IS", "ASELS.IS", "EREGL.IS", "FROTO.IS", "ATLAS.IS",
                  "MTRYO.IS", "A1YEN.IS", "MANAS.IS","AKSUE.IS"
                 ]

print(" Dolar ve Altın Verileri ile hesaplamalar yapılıyor ")

# DÜZELTME 1: Verileri ayrı ayrı indirip biz birleştireceğiz (En garanti yöntem)
try:
    dolar = yf.download("TRY=X", period="2y", progress=False, auto_adjust=True)
    altin = yf.download("GC=F", period="2y", progress=False, auto_adjust=True)
    
    # .squeeze() tek sütunlu DataFrame'i Series'e çevirir, olası boyut hatalarını önler
    piyasa_verileri = pd.DataFrame({
        "Dolar": dolar["Close"],
        "Altin": altin["Close"]
    })
    
    # Eksik günleri doldur
    piyasa_verileri = piyasa_verileri.ffill()

# Hata olursa boş bir DataFrame oluştur
except Exception as e:
    print(f"Piyasa verisi indirilirken hata: {e}")
    
    piyasa_verileri = pd.DataFrame()

def rsi_hesapla(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def gelismis_analiz_yap(hisse_kodu):
    try:
        # HİSSE VERİSİNİ ÇEK
        hisse = yf.Ticker(hisse_kodu)
        hisse_veri = hisse.history(period="2y")
        
        if len(hisse_veri) < 200:
            return None

        # Sadece gerekli sütunları al
        veri = hisse_veri[["Close", "Volume"]].copy()
        
        # Zaman dilimi (Timezone) uyumsuzluğunu gidermek için
        if not piyasa_verileri.empty:
            # İndekslerin timezone bilgisini kaldırıyoruz ki eşleşebilsinler
            veri.index = veri.index.tz_localize(None)
            piyasa_verileri.index = piyasa_verileri.index.tz_localize(None)
            
            # 2. VERİLERİ BİRLEŞTİR (MERGE)
            veri = veri.join(piyasa_verileri)
            veri = veri.ffill().dropna()
        else:
            # Piyasa verisi çekilemediyse Dolar/Altın sütunlarını 0 yap
            veri["Dolar"] = 1
            veri["Altin"] = 1

        # 3. ÖZELLİK MÜHENDİSLİĞİ
        veri["SMA_10"] = veri["Close"].rolling(window=10).mean()
        veri["SMA_50"] = veri["Close"].rolling(window=50).mean()
        veri["RSI"] = rsi_hesapla(veri["Close"])
        
        # Makro Sinyaller
        veri["Dolar_Degisim"] = veri["Dolar"].pct_change()
        veri["Altin_Degisim"] = veri["Altin"].pct_change()
        veri["Dolar_Bazli_Fiyat"] = veri["Close"] / veri["Dolar"]
        
        veri = veri.dropna()

        # 4. ETİKETLEME
        veri["Hedef"] = np.where(veri["Close"].shift(-1) > veri["Close"], 1, 0)

        # 5. EĞİTİM
        ozellikler = [
            "Close", "Volume", "SMA_10", "SMA_50", "RSI", 
            "Dolar_Degisim", "Altin_Degisim", "Dolar_Bazli_Fiyat"
        ]
        
        X = veri[ozellikler]
        y = veri["Hedef"]

        X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, shuffle=False)
        
        model = RandomForestClassifier(n_estimators=200, min_samples_split=5, random_state=42)
        model.fit(X_train, y_train)

        tahminler = model.predict(X_test)
        basari = accuracy_score(y_test, tahminler)

        # BUGÜNÜ TAHMİN ET
        son_veri = X.iloc[[-1]]
        tahmin = model.predict(son_veri)[0]
        olasilik = model.predict_proba(son_veri)[0]

        return {
            "Hisse": hisse_kodu,
            "Basari": basari * 100,
            "Tahmin": "YÜKSELİŞ " if tahmin == 1 else "DÜŞÜŞ ",
            "Guven": olasilik[1] * 100 if tahmin == 1 else olasilik[0] * 100
        }

    except Exception as e:

        return None


print("\n" + "="*60)
print(f"{'HİSSE':<10} | {'TAHMİN':<12} | {'GÜVEN %':<10} | {'BAŞARI %':<10} | {'ANALİZ'}")
print("-" * 60)

for hisse in HISSE_LISTESI:
    sonuc = gelismis_analiz_yap(hisse)
    if sonuc:
        yorum = "Zayıf"
        if sonuc["Guven"] > 55: yorum = "Orta"
        if sonuc["Guven"] > 65: yorum = "** Güçlü **"
        
        print(f"{sonuc['Hisse']:<10} | {sonuc['Tahmin']:<12} | %{sonuc['Guven']:<9.1f} | %{sonuc['Basari']:<9.1f} | {yorum}")
    else:
        print(f"{hisse:<10} | Veri Hatası veya Yetersiz Veri")

print("=" * 80)