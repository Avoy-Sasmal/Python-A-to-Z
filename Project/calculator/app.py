from flask import Flask, render_template, request

app = Flask(__name__)

def add(x,y) :
  return x+ y

def subtract(x,y) :
  return x - y

def multiply(x,y) :
  return x * y

def divide(x,y) :
  if(y==0):
    return "Cannot divide by zero"
  else:
    return x / y 
  

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        x = int(request.form['first_number'])
        y = int(request.form['second_number'])
        operation = request.form['operation']
      
        if operation == 'add':
            result = add(x, y)
        elif operation == 'subtract':
            result = subtract(x, y)
        elif operation == 'multiply':
            result = multiply(x, y)
        elif operation == 'divide':
            result = divide(x, y)
    
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)