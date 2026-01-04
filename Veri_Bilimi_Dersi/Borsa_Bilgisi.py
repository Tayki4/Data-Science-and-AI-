import yfinance as yf

# BIST hisselerinin sonuna ".IS" eklenir
hisse = yf.Ticker("THYAO.IS")

detaylar = hisse.info
guncel_fiyat = detaylar.get("currentPrice") 

print(f"THY Güncel Fiyat: {guncel_fiyat} TL")

gecmis_veri = hisse.history(period="1mo")

print("\n Son 5 Günlük Veri ")
print(gecmis_veri.tail(5))