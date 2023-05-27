import streamlit as st
import csv
from datetime import datetime
import os



# プロフィール保存をする
def save_profile(name, age, gender, height):
    with open('profile.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age', 'gender', 'height'])
        writer.writerow([name, age, gender, height])

# プロフィールを表示する
def show_profile():
    with open('profile.csv', 'r') as f:
        reader = csv.reader(f)
        profile = []
        for row in reader:
            profile.append(row)
        st.write(f"名前: {profile[1][0]}")
        st.write(f"年齢: {profile[1][1]}")
        st.write(f"性別: {profile[1][2]}")
        st.write(f"身長: {profile[1][3]} cm")
        return profile[1][3]

# 体重を保存する
def save_weight(date, weight):
    csv_path = os.path.join(os.getcwd(), 'weight.csv')
    
    # weight.csvを読み込む
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # 新しいデータを追加する
    rows.append([date, weight])
    
    # weight.csvを上書き保存する
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

# 体重を表示する
def show_weight():
    with open('weight.csv', 'r') as f:
        reader = csv.reader(f)
        weights = []
        for row in reader:
            weights.append(row)
        for weight in weights:
            st.write(f"日付: {weight[0]}, 体重: {weight[1]} kg")
        return weight[0]

# BMIを計算する
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

# BMIを保存する
def save_bmi(date, bmi):
    with open('bmi.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'bmi'])
        writer.writerow([date, bmi])

# BMIを表示する
def show_bmi():
    with open('bmi.csv', 'r') as f:
        reader = csv.reader(f)
        bmis = []
        for row in reader:
            bmis.append(row)
        for bmi in bmis:
            st.write(f"日付: {bmi[0]}, BMI: {bmi[1]}")

# 食事内容を保存する
def save_meal(date, meal):
    with open('meal.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'meal'])
        writer.writerow([date, meal])

# 食事内容を表示する
def show_meal():
    with open('meal.csv', 'r') as f:
        reader = csv.reader(f)
        meals = []
        for row in reader:
            meals.append(row)
        for meal in meals:
            st.write(f"日付: {meal[0]}, 食事内容: {meal[1]}")

# 歩数を保存する
def save_steps(date, steps):
    with open('steps.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'steps'])
        writer.writerow([date, steps])

# 歩数を表示する
def show_steps():
    with open('steps.csv', 'r') as f:
        reader = csv.reader(f)
        steps_list = []
    for row in reader:
        steps_list.append(row)
        for steps in steps_list:
            st.write(f"日付: {steps[0]}, 歩数: {steps[1]} 歩")

# 筋トレ系運種類と時間を保存する
def save_exercise(date, exercise, time):
    with open('exercise.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'exercise', 'time'])
        writer.writerow([date, exercise, time])

# 筋トレ系運動種類と時間を表示する
def show_exercise():
    with open('exercise.csv','r') as f:
        reader = csv.reader(f)
        exercises = []
        for row in reader:
            exercises.append(row)
        for exercise in exercises:
            st.write(f"日付: {exercise[0]}, 種目: {exercise[1]}, 時間: {exercise[2]} 分")

# 今日の良かったことと反省を保存する
def save_journal(date, good, bad):
    with open('journal.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'good', 'bad'])
        writer.writerow([date, good, bad])

# 今日の良かったことと反省を表示する
def show_journal():
    with open('journal.csv', 'r') as f:
        reader = csv.reader(f)
        journals = []
        for row in reader:
            journals.append(row)
        for journal in journals:
            st.write(f"日付: {journal[0]}, 良かったこと: {journal[1]}, 反省: {journal[2]}")

# 健康管理アプリのタイトルを表示する
st.title("ダイエット記録アプリ")

# ページを切り替えるためのサイドバーを作成する
menu = ['プロフィール', '体重記録', 'BMI計算', '食事内容', '歩数', '筋トレ系運動種類時間', '今日の良かったことと反省']
choice = st.sidebar.selectbox('メニュ', menu)

# 選択たメニューに応じて、対応する関数を呼び出す
if choice == 'プロフィール':
    st.title('プロフィール')
    name = st.text_input('名前')
    age = st.number_input('年齢', min_value=0, max_value=120, step=1)
    gender = st.radio('性別', ['男性', '女性'])
    height = st.number_input('身長(cm)', min_value=0, max_value=300, step=1)
    if st.button('保存', key='profile_save_button'):
        save_profile(name, age, gender, height)
        st.success('プロフィールを保存しました。')
    height_2 = show_profile()

elif choice == '体重記録':
    st.title('体重記録')
    date = st.date_input('日付')
    weight = st.number_input('体重g)', min_value=0.0, max_value=500.0, step=0.1)
    if st.button('保存', key='weight_save_button'):
        save_weight(date, weight)
        st.success('体重を保存しました。')
    weight_2 = show_weight()

elif choice == 'BMI計算':
    st.title('BMI計算')
    weight = None
    height = None
    if 'weight_2' in locals():
        weight = weight_2
    else:
        weight = st.number_input('体重(kg)', min_value=0.0, max_value=500.0, step=0.1)
    if 'height_2' in locals():
        height = height_2
    else:
        height = st.number_input('身長(cm)', min_value=0, max_value=300, step=1)
    if st.button('計算', key='bmi_calculate_button'):
        bmi = calculate_bmi(weight, height)
        st.write(f"BMI: {bmi:.2f}")
        if st.button('保存', key='bmi_save_button'):
            today = datetime.today().strftime('%Y-%m-%d')
            save_bmi(today, bmi)
            st.success('BMIを保存しました。')
    show_bmi()



elif choice == '食事内容':
    st.title('食事内容')
    date = st.date_input('日付')
    meal = st.text_input('食事')
    if st.button('保存', key='meal_save_button'):
        save_meal(date, meal)
        st.success('食事内容を保存しました。')
    show_meal()

elif choice == '歩数':
    st.title('歩数')
    date = st.date_input('日付')
    steps = st.number_input('歩数(歩)', min_value=0, max_value=100000, step=1)
    if st.button('保存', key='steps_save_button'):
        save_steps(date, steps)
        st.success('歩数を保存しました')
    show_steps()

elif choice == '筋トレ系運動種類と時間':
    st.title('筋トレ系運動種類と時間')
    date = st.date_input('日付')
    exercise = st.text_input('種目')
    time = st.number_input('時間(分)', min_value=0, max_value=1440, step=1)
    if st.button('保存', key='exercise_save_button'):
        save_exercise(date, exercise, time)
        st.success('筋トレ系運動種類と時間を保存しました。')
    show_exercise()

elif choice == '今日の良かったことと反省':
    st.title('今日の良かったことと反省')
    date = st.date_input('日付')
    good = st.text_input('良かったこと')
    bad = st.text_input('反省')
    if st.button('保存', key='journal_save_button'):
        save_journal(date, good, bad)
        st.success('今日の良かったことと反省を保存しました。')
    show_journal()
