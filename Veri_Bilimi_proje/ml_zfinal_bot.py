import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#! istenen hisseleri gir 
HISSE_LISTESI = ["THYAO.IS", "GARAN.IS", "ASELS.IS", "EREGL.IS", "FROTO.IS", "KCHOL.IS", "SISE.IS", "MTRYO.IS", "A1YEN.IS", "MANAS.IS","AKSUE.IS", "ATLAS.IS"
                 ]

print(" Piyasa verileri indiriliyor. LÜTFEN BEKLE! ")

try:
    # auto_adjust=True (bu sayede gerçek zamanlı veri çekiyor)
    dolar = yf.download("TRY=X", period="2y", progress=False, auto_adjust=True)
    altin = yf.download("GC=F", period="2y", progress=False, auto_adjust=True)
    
    # Sadece Close sütunlarını alıp birleştiriyoruz
    piyasa_verileri = pd.DataFrame({
        "Dolar": dolar["Close"],
        "Altin": altin["Close"]
    })
    piyasa_verileri = piyasa_verileri.ffill()  # NaN sütunların bugün veri yoksa dünü kabul etmesi için 

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
        hisse = yf.Ticker(hisse_kodu)
        hisse_veri = hisse.history(period="2y")
        
        if len(hisse_veri) < 200: return None
         
         #! Data ayıklama 
         # İstediğimiz sütunları çektik 
        veri = hisse_veri[["Close", "Volume"]].copy()
        
        # Saat dilimi farkı hata veriyordu localize(none) yaparak saatleri eşitledik 
        if not piyasa_verileri.empty:
            veri.index = veri.index.tz_localize(None)
            piyasa_verileri.index = piyasa_verileri.index.tz_localize(None)
            veri = veri.join(piyasa_verileri)  # Dolar ile Altın verileri 
            veri = veri.ffill().dropna() # tatil günlerinde boş yerleri doldurur
        else:
            veri["Dolar"] = 1
            veri["Altin"] = 1
            # hata çıktısını engeller

        veri["SMA_10"] = veri["Close"].rolling(window=10).mean()  # ortalamalar al
        veri["SMA_50"] = veri["Close"].rolling(window=50).mean()
        veri["RSI"] = rsi_hesapla(veri["Close"]) 
        
        veri["Dolar_Degisim"] = veri["Dolar"].pct_change()  # yüzdelik değişimler aldık makina öğrenmesi için daha iyi
        veri["Altin_Degisim"] = veri["Altin"].pct_change()
        veri["Dolar_Bazli_Fiyat"] = veri["Close"] / veri["Dolar"]
        
        veri = veri.dropna() # boş satır temizleme sıralama için


        veri["Hedef"] = np.where(veri["Close"].shift(-1) > veri["Close"], 1, 0) 
        ## print(veri.head()) komutu ile temizlediğimiz veriyi görebiliriz
    
        
        ozellikler = ["Close", "Volume", "SMA_10", "SMA_50", "RSI", "Dolar_Degisim", "Altin_Degisim", "Dolar_Bazli_Fiyat"]
        X = veri[ozellikler]
        y = veri["Hedef"]

        X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, shuffle=False)
        
        model = RandomForestClassifier(n_estimators=200, min_samples_split=5, random_state=42)
        model.fit(X_train, y_train)   #FİT x ve y arasındaki ilişkiyi öğrenmesi 

        tahminler = model.predict(X_test) # kendini test etmesi 
        basari = accuracy_score(y_test, tahminler)

        # Tahmin ve Son Durum Verileri
        son_veri = X.iloc[[-1]]
        tahmin = model.predict(son_veri)[0]
        olasilik = model.predict_proba(son_veri)[0]
        
        # Rapora eklemek için son günün Dolar ve Altın değişim oranlarını alıyoruz
        son_dolar_degisim = son_veri["Dolar_Degisim"].iloc[0] * 100
        son_altin_degisim = son_veri["Altin_Degisim"].iloc[0] * 100

        return {
            "Hisse": hisse_kodu,
            "Basari": basari * 100,
            "Tahmin": "YÜKSELİŞ " if tahmin == 1 else "DÜŞÜŞ ",
            "Guven": olasilik[1] * 100 if tahmin == 1 else olasilik[0] * 100,
            "Dolar_Degisim": son_dolar_degisim,
            "Altin_Degisim": son_altin_degisim
        }
###  BAŞARI MODELİN GEÇMİŞTE NE KADAR BAŞARILI OLDUĞUNU BELİRTİR
    except Exception as e:
        return None

#! çıktılar 
print("\n" + "="*95)
# Başlıklara Dolar ve Altın'ı ekledik
print(f"{'HİSSE':<9} | {'TAHMİN':<11} | {'GÜVEN %':<8} | {'BAŞARI %':<8} | {'DOLAR 1G%':<9} | {'ALTIN 1G%':<9} | {'ANALİZ'}")
print("-" * 95)

for hisse in HISSE_LISTESI:
    sonuc = gelismis_analiz_yap(hisse)
    if sonuc:
        yorum = "Zayıf"
        if sonuc["Guven"] > 55: yorum = "-Orta-"
        if sonuc["Guven"] > 65: yorum = "***Güçlü*** "
        
        # Dolar ve Altın verilerini yazdır
        dolar_str = f"%{sonuc['Dolar_Degisim']:.2f}"
        altin_str = f"%{sonuc['Altin_Degisim']:.2f}"
        
        print(f"{sonuc['Hisse']:<9} | {sonuc['Tahmin']:<11} | %{sonuc['Guven']:<7.1f} | %{sonuc['Basari']:<7.1f} | {dolar_str:<9} | {altin_str:<9} | {yorum}")
    else:
        print(f"{hisse:<9} | Veri Hatası")

print("=" * 95)
print(" İSTENİLEN SONUÇLAR ALINMIŞTIR. BOL ŞANS!!! ")