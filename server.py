from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep this secret"


@app.get("/")
def counting():
    session['counter'] +=1
    if session['counter'] ==0:
        count_x = (f'You have visisted {session['counter']} times!!')
        print(count_x)
    else:
        count_x = (f'You have visited {session['counter']} time!!')
        print(count_x)
        return render_template("index.html", count_x=count_x)

@app.post('/increment_by')
def increment_x():
    session['counter'] += 1
    return redirect('/')

@app.post('/clear')
def clear_count():
    session.clear()
    session['counter'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)