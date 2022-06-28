import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

scaler = joblib.load(r"C:\Users\Cannonball\Downloads\Epsilon AI\Final Project\Mobile Price Classification app\Models\scaler.h5")
model = joblib.load(r'C:\Users\Cannonball\Downloads\Epsilon AI\Final Project\Mobile Price Classification app\Models\model.h5')


@app.route('/')
def index():
    # put application's code here
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def get_prediction():
    print("started")
    if request.method == 'POST':
        battery_power = int(request.form['battery_power'])
        # print(battery_power)

        blue = int(request.form['blue'])
        # print(blue)

        clock_speed = float(request.form['clock_speed'])
        # print(clock_speed)

        dual_sim = int(request.form['dual_sim'])
        # print(dual_sim)

        fc = int(request.form['fc'])
        # print(fc)

        four_g = int(request.form['four_g'])
        # print(four_g)

        int_memory = int(request.form['int_memory'])
        # print(int_memory)

        m_dep = float(request.form['m_dep'])
        # print(m_dep)

        mobile_wt = int(request.form['mobile_wt'])
        # print(mobile_wt)

        n_cores = int(request.form['n_cores'])
        # print(n_cores)

        pc = int(request.form['pc'])
        # print(pc)

        px_height = int(request.form['px_height'])
        # print(px_height)

        px_width = int(request.form['px_width'])
        # print(px_width)

        ram = int(request.form['ram'])
        # print(ram)

        sc_h = int(request.form['sc_h'])
        # print(sc_h)

        sc_w = int(request.form['sc_w'])
        # print(sc_w)

        talk_time = int(request.form['talk_time'])
        # print(talk_time)

        three_g = int(request.form['three_g'])
        # print(three_g)

        touch_screen = int(request.form['touch_screen'])
        # print(touch_screen)

        wifi = int(request.form['wifi'])
        # print(wifi)
    """
    This is the target variable with value of 0(low cost),
     1(medium cost), 
     2(high cost),
    3(very high cost).
    """
    data = [battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc,
            px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi]
    print("Data: ", data)
    prediction = model.predict([data])[0]
    print(prediction)
    result = ""
    if prediction == 0:
        result = "low cost"
    elif prediction == 1:
        result = "medium cost"
    elif prediction == 1:
        result = "high cost"
    else:
        result = "very high cost"
    return render_template('prediction.html', price_range=result)


if __name__ == '__main__':
    print("Main app started!")
    app.run(debug=True)
