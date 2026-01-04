import yfinance as yf
import pandas as pd
import time
from datetime import datetime

# --- AYARLAR ---
# Takip etmek istediğin hisseleri bu listeye ekle
HISSE_LISTESI = ["THYAO.IS", "GARAN.IS", "ASELS.IS", "KCHOL.IS", "SISE.IS"]
KONTROL_SURESI = 60  # Döngü bitince kaç saniye beklesin?

def rsi_hesapla(veri, pencere=14):
    """RSI İndikatörü Hesaplama Fonksiyonu"""
    fark = veri["Close"].diff()
    kazanc = fark.where(fark > 0, 0)
    kayip = -fark.where(fark < 0, 0)

    ortalama_kazanc = kazanc.ewm(com=pencere - 1, min_periods=pencere).mean()
    ortalama_kayip = kayip.ewm(com=pencere - 1, min_periods=pencere).mean()

    rs = ortalama_kazanc / ortalama_kayip
    rsi = 100 - (100 / (1 + rs))
    return rsi

print(f"🚀 Çoklu Borsa Botu v3.0 Başlatıldı...")
print(f"Takip Listesi: {HISSE_LISTESI}")
print("Durdurmak için: Ctrl + C")
print("=" * 60)

try:
    while True:
        zaman_damgasi = datetime.now().strftime("%H:%M:%S")
        print(f"\n🔄 Tarama Başlıyor... Saat: {zaman_damgasi}")
        
        # LİSTEDEKİ HER HİSSE İÇİN TEK TEK DÖN
        for sembol in HISSE_LISTESI:
            try:
                # 1. Veriyi Çek
                hisse = yf.Ticker(sembol)
                # Anlık analiz için saatlik veri (1h) kullanıyoruz
                veri = hisse.history(period="1mo", interval="1h")

                if veri.empty:
                    print(f" {sembol}: Veri alınamadı, geçiliyor.")
                    continue

                # 2. İndikatörleri Hesapla
                veri["SMA20"] = veri["Close"].rolling(window=20).mean()
                veri["RSI"] = rsi_hesapla(veri)

                # Son değerleri al
                son_fiyat = veri["Close"].iloc[-1]
                son_sma = veri["SMA20"].iloc[-1]
                son_rsi = veri["RSI"].iloc[-1]

                # 3. Analiz ve Ekrana Yazdırma
                print("-" * 40)
                print(f"📊 {sembol:<10} | Fiyat: {son_fiyat:.2f} TL")
                
                # Sinyal Mantığı
                sinyal = "BEKLE"
                detay = "Nötr"
                
                if son_fiyat > son_sma and son_rsi < 70:
                    sinyal = " AL"
                    detay = "Trend Yukarı, RSI Uygun"
                elif son_fiyat < son_sma:
                    sinyal = " SAT"
                    detay = "Trend Aşağı Kırıldı"
                elif son_rsi > 70:
                    sinyal = " RİSKLİ"
                    detay = "Aşırı Alım Bölgesi (Pahalı)"
                
                print(f"Sinyal: {sinyal:<10} | RSI: {son_rsi:.2f} | SMA20: {son_sma:.2f}")
                print(f"Durum: {detay}")

            except Exception as e:
                print(f"⚠️ {sembol} analiz edilirken hata oluştu: {e}")

        print("=" * 60)
        print(f"💤 Tarama bitti. {KONTROL_SURESI} saniye bekleniyor...")
        time.sleep(KONTROL_SURESI)

except KeyboardInterrupt:
    print("\n Bot durduruldu.")