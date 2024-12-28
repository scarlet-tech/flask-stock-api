from flask import Flask, request, jsonify
import yfinance as yf
import os

app = Flask(__name__)

def get_stock_data(ticker):
    """
    指定されたティッカーの現在値を取得する
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            latest_price = data['Close'].iloc[-1]
            return {"ticker": ticker, "price": latest_price}
        else:
            return {"error": f"No data found for {ticker}"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/get_stock_price', methods=['GET'])
def get_stock_price():
    """
    APIエンドポイント: ティッカーの現在値を返す
    """
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "No ticker provided"}), 400
    data = get_stock_data(ticker)
    return jsonify(data)

@app.route("/")
def home():
    """
    ルートエンドポイント
    """
    return "Flaskアプリが正常に動作しています！"

if __name__ == "__main__":
    # Render環境用にポートを環境変数から取得
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
