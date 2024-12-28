import requests

def get_stock_price_from_api(ticker):
    """
    Flask APIを呼び出して株価を取得する関数
    """
    url = f"http://127.0.0.1:5000/get_stock_price?ticker={ticker}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "price" in data:
                return f"{data['ticker']} の現在値は {data['price']:.2f}"
            else:
                return f"エラー: {data.get('error', '詳細不明')}"
        else:
            return f"HTTPエラー: {response.status_code}"
    except Exception as e:
        return f"リクエストエラー: {str(e)}"

if __name__ == "__main__":
    tickers = input("ティッカーをカンマ区切りで入力してください（例: AAPL, 7203.T）: ")
    tickers_list = tickers.split(",")  # カンマで分割してリスト化
    for ticker in tickers_list:
        ticker = ticker.strip()  # 前後の空白を削除
        print(get_stock_price_from_api(ticker))
