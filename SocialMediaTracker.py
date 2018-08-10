import os

from flask import Flask, render_template, request, redirect

web = Flask(__name__)


@web.route("/")
def main():
    return render_template("index.html")


@web.route("/config", methods=['POST'])
def get_config():
    waweb = request.files['whatsapp']
    waweb.save('data/whatsapp.web')
    return redirect("/")


@web.route("/track", methods=['POST'])
def get_track():
    name = request.form["name"]
    twitter = request.form["twitter"]
    whatsapp = request.form["whatsapp"]
    facebook = request.form["facebook"]
    instagram = request.form["instagram"]
    online_time = request.form.get("time")
    sleep = request.form.get("sleep")
    prediction = request.form.get("onlineprediction")
    words = request.form["words"]
    information = request.form.get("collector")
    if online_time == 'on':
        online_time = 1
    else:
        online_time = 0
    if sleep == 'on':
        sleep = 1
    else:
        sleep = 0
    if prediction == 'on':
        prediction = 1
    else:
        prediction = 0
    if information == 'on':
        information = 1
    else:
        information = 0
    checkboxes = [str(online_time), str(sleep), str(prediction), str(information)]
    os.mkdir("data/" + name)
    with open("data/" + name + "/config.cfg", "w") as cfg:
        cfg.writelines("name: " + name + "\n")
        cfg.writelines("twitter: " + twitter + "\n")
        cfg.writelines("whatsapp: " + whatsapp + "\n")
        cfg.writelines("facebook: " + facebook + "\n")
        cfg.writelines("instagram: " + instagram + "\n")
        cfg.writelines("words: " + words + "\n")
        cfg.writelines("online_time: " + checkboxes[0] + "\n")
        cfg.writelines("sleep: " + checkboxes[1] + "\n")
        cfg.writelines("prediction: " + checkboxes[2] + "\n")
        cfg.writelines("information: " + checkboxes[3] + "\n")
    return redirect("/")


if __name__ == "__main__":
    web.run(debug=True, host="0.0.0.0", port=80)
