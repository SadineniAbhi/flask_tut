from flask import Flask ,render_template

app = Flask(__name__)

JOBS = [
  {'id':1,
  'title':"data analyst",
  'location':"bengalure",
  'salary': "10,00,000"
  },
  {'id':1,
  'title':"data scientist",
  'location':"dheli ",
  'salary': "19,00,000"
  },
  {'id':1,
  'title':"front end engineer",
  'location':"remote"
  },
  {'id':1,
  'title':"back end engineer",
  'location':"bengalure",
  'salary': "120,000"
  }
]
@app.route("/")
def hello_world():
  return render_template ('home.html',jobs = JOBS,companyname = "jovian")
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)