import yfinance as yf
import pandas as pd

def sinyal_uret(hisse_kodu):
    print(f"\n--- {hisse_kodu} Analiz Ediliyor ---")
    
    # Veriyi Çek
    hisse = yf.Ticker(hisse_kodu)
    veri = hisse.history(period="6mo")
    
    if veri.empty:
        print("Veri çekilemedi!")
        return

    # Güncel Fiyat
    guncel_fiyat = veri["Close"].iloc[-1]
    
    #  (SMA20) 
    veri["SMA20"] = veri["Close"].rolling(window=20).mean()
    
    sma20_degeri = veri["SMA20"].iloc[-1]
    
    print(f"Güncel Fiyat: {guncel_fiyat:.2f} TL")
    print(f"20 Günlük Ortalama: {sma20_degeri:.2f} TL")
    
    print("-" * 30)
    
    if guncel_fiyat > sma20_degeri:
        print(f" KARAR: AL (Trend Yükselişte)")
        print("Fiyat, ortalamanın üzerinde seyrediyor.")
    else:
        print(f" KARAR: SAT veya BEKLE (Trend Düşüşte)")
        print("Fiyat, ortalamanın altında kaldı.")

# İstediğin hisseleri buraya yazıp deneyebilirsin
sinyal_uret("THYAO.IS") 
sinyal_uret("GARAN.IS")
sinyal_uret("ASELS.IS")
sinyal_uret("DIRIT.IS")
sinyal_uret("EUYO.IS")
sinyal_uret("ATLAS.IS")
sinyal_uret("MTRYO.IS")
sinyal_uret("A1YEN.IS")
sinyal_uret("MANAS.IS")
sinyal_uret("AKSUE.IS")