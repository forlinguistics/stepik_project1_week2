from flask import Flask, abort
from flask import render_template
from data import tours, departures

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html', data=list(tours.items())[0:6])


@app.route('/departures/<departure>/')
def show_deps(departure):
    new_data = {i: tours[i] for i in tours.keys() if tours[i]['departure'] == departure}
    if new_data == {}:
        return abort(404)
    rus_departure = departures[departure]
    rus_departure = 'и' + rus_departure[1:]
    return render_template('departure.html', departure=rus_departure, data=new_data)


@app.route('/tours/<int:id>/')
def show_tour(id):
    if not id in tours.keys():
        abort(404)
    night_str = str(tours[id]['nights'])
    if int(night_str) % 100 in range(5, 21):
        night_str = night_str + ' ночей'
    elif (int(night_str) % 10 == 1):
        night_str = night_str + ' ночь'
    else:
        night_str = night_str + ' ночи'
    rus_departure = departures[tours[id]["departure"]]
    rus_departure = 'и' + rus_departure[1:]
    return render_template('tour.html', tour=tours[id], nights=night_str, dep=rus_departure)


if __name__ == '__main__':
    app.run()
