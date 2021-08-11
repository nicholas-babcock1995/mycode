#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)
app.secret_key = "random string"


groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/", methods =["GET", "POST"])
def index():
    if"username" in session and session["username"] == "admin":
        if request.method == "POST":
            hostname = request.form.get("hostname")
            ip = request.form.get("ip")
            fqdn = request.form.get("fqdn")
            groups.append({"hostname" : hostname, "ip":ip, "fqdn": fqdn})
    return render_template("host_template.j2", groups = groups)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        session["username"] = request.form.get("username")
    if "username" in session and session["username"] == "admin":
        return render_template("add_data_template.html.j2")
    else:
        return """
        <form action ="" method = "post">
        <p> invalid login. </p>
        <p> <input type= text name = username></p>
        <p><input type = submit value = Login></p>
        </form>
        """
    
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2224)
