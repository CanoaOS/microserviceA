import json
import yaml
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['POST'])
def result():
    month_table = {1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August',
                   9:'September', 10:'October', 11:'November', 12:'December'}

    data = request.get_json()
    user_day = data['day']
    user_month = data['month']
    user_date_tuple = (user_month, user_day)
    print(user_date_tuple)
    # parsed = json.loads(data)
    with open("zodiac.json", errors="ignore") as stream:
        try:
            zodiac_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    western_data = None
    for sign in zodiac_data:
        if sign == "western_zodiac":
            western_data = zodiac_data[sign]
        print(sign)

    for item in western_data:
        # print(item)
        print(western_data[item]['approximate_start_date'])

    day = data['day']
    month_num = data['month']

    for month in month_table:
        if month_num == month:
            month_num = month_table[month]

    string = f'{day} {month_num}'
    print(string)

    for sign in western_data:

        start = western_data[sign]['approximate_start_date']
        start_day = start[0:2]
        start_day = int(start_day)
        start_month = start[3:]

        end = western_data[sign]['approximate_end_date']
        end_day = end[0:2]
        end_day = int(end_day)
        end_month = end[3:]

        for x in range(1, len(month_table)+1):
            if start_month == month_table[x]:
                start_month = x
            if end_month == month_table[x]:
                end_month = x

        start_sign_tuple = (start_month, start_day)
        end_sign_tuple = (end_month, end_day)
        print(start_sign_tuple)
        print(end_sign_tuple)
        print(f'num: {start_day}-{type(start_day)}, month: {start_month}-{type(start_month)}')
        if start_sign_tuple <= user_date_tuple <= end_sign_tuple:
            print("between")
            return sign

    return jsonify({"zodiac_sign": sign})


if __name__ == '__main__':
    app.run(debug=True)


