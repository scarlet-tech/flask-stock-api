import yfinance as yf

def get_stock_data(tickers):
    """
    指定したティッカーの株価データを取得する関数
    """
    results = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")
            if not data.empty:
                latest_price = data['Close'].iloc[-1]
                results.append(f"{ticker} の最新株価: {latest_price:.2f}")
            else:
                results.append(f"{ticker} のデータが見つかりません。")
        except Exception as e:
            results.append(f"{ticker} の取得中にエラー: {str(e)}")
    return results

if __name__ == "__main__":
    # 日本株 (例: トヨタ自動車、三菱UFJ)
    japanese_stocks = ["7203.T", "8035.T"]
    for result in get_stock_data(japanese_stocks):
        print(result)
   
    # アメリカ株 (例: Apple, Astera Labs)
    us_stocks = ["AAPL", "ALAB"]
    for result in get_stock_data(us_stocks):
        print(result)
    
    # 日経225先物 (例: 日経先物連動ETF)
    futures = ["^N225"]
    for result in get_stock_data(futures):
        print(result)
