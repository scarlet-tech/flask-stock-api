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
                return f"{data['ticker']} の最新株価は {data['price']:.2f} です。"
            else:
                return f"エラー: {data.get('error', '不明なエラー')}"
        else:
            return f"HTTPエラー: {response.status_code}"
    except Exception as e:
        return f"リクエストエラー: {str(e)}"

# テスト
if __name__ == "__main__":
    ticker = input("ティッカーを入力してください: ")  # 例: AAPL, 7203.T
    print(get_stock_price_from_api(ticker))
