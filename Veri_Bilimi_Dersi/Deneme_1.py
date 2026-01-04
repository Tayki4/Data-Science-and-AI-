import yfinance as yf

# THY hissesini kontrol edelim
hisse = yf.Ticker("THYAO.IS")

# Sadece fiyatı alalım
fiyat = hisse.info.get("currentPrice")

print(f"THY Güncel Fiyatı: {fiyat} TL")