import yfinance as yf
import pandas as pd
import time
from datetime import datetime


HISSE_KODU = "THYAO.IS"  # Takip edilecek hisse
KONTROL_SURESI = 60      # Kaç saniyede bir baksın? (Örn: 60 saniye)

def rsi_hesapla(veri, pencere=14):
    
    fark = veri["Close"].diff()
    kazanc = fark.where(fark > 0, 0)
    kayip = -fark.where(fark < 0, 0)

    # Standart RSI formülü
    ortalama_kazanc = kazanc.ewm(com=pencere - 1, min_periods=pencere).mean()
    ortalama_kayip = kayip.ewm(com=pencere - 1, min_periods=pencere).mean()

    rs = ortalama_kazanc / ortalama_kayip
    rsi = 100 - (100 / (1 + rs))
    return rsi

print(f" Borsa Botu v2 Başlatıldı.. ({HISSE_KODU})")
print(" Durdurmak için: Ctrl + C  bas. ")
print("-" * 50)

try:
    while True:
        hisse = yf.Ticker(HISSE_KODU)
        # RSI için geriye dönük veri
        veri = hisse.history(period="1mo", interval="1h") 

        if veri.empty:
            print("Veri alınamadı, tekrar deneniyor...")
            time.sleep(10)
            continue

        #  İNDİKATÖRLERİ HESAPLA
        
        veri["SMA20"] = veri["Close"].rolling(window=20).mean()
        
        veri["RSI"] = rsi_hesapla(veri)

        # Son değerleri al
        son_fiyat = veri["Close"].iloc[-1]
        son_sma = veri["SMA20"].iloc[-1]
        son_rsi = veri["RSI"].iloc[-1]
        tarih = datetime.now().strftime("%H:%M:%S")

        # 3. KARAR MEKANİZMASI VE EKRANA YAZDIRMA
        print(f"\n Saat: {tarih}")
        print(f" Fiyat: {son_fiyat:.2f} TL")
        print(f" SMA20: {son_sma:.2f} | 📊 RSI: {son_rsi:.2f}")

        # Strateji Mantığı
        if son_fiyat > son_sma and son_rsi < 70:
            print(" SİGNAL: GÜÇLÜ AL! (Trend yukarı ve RSI uygun)")
        elif son_fiyat < son_sma:
            print(" SİGNAL: SAT (Trend aşağı döndü)")
        elif son_rsi > 70:
            print(" SİGNAL: DİKKAT (Hisse aşırı pahalı düzeltme gelebilir)")
        else:
            print(" SİGNAL: BEKLE (Yön belirsiz)")

        # 4. BEKLEME (OTOMASYON KISMI)
        print(f"{KONTROL_SURESI} saniye bekleniyor...")
        time.sleep(KONTROL_SURESI)

except KeyboardInterrupt:
    print("\n Bot kullanıcı taraf. durduruldu.")