from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL 連接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '9056Xo6319',  # 修改為您的 MySQL 密碼
    'database': 'schedule_db'
}

# API: 獲取某月的班表數據
@app.route('/api/schedule/<month>', methods=['GET'])
def get_schedule(month):
    try:
        # 連接數據庫
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # 執行查詢語句
        query = "SELECT * FROM schedule WHERE month = %s"
        cursor.execute(query, (month,))
        schedule = cursor.fetchall()

        # 返回 JSON 格式的結果
        return jsonify(schedule)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
