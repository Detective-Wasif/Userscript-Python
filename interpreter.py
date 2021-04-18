import math
from flask import Flask, request, render_template 
  
app = Flask(__name__)   
k = "\n"

def interpret(scrip):
  n=""
  if scrip == "":
    n=""
    for fizzbuzz in range(1,101):
      if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        n+="fizzbuzz"+k
        continue
      elif fizzbuzz % 3 == 0:
        n+="fizz"+k
        continue
      elif fizzbuzz % 5 == 0:
        n+="buzz"+k
        continue
      else:
        n+=str(fizzbuzz)+k
    return n
  else:
    a=[]
    numbers = {str(x):x for x in range(10)}
    numbers.update({'π':math.pi,'S':640,'F':256,'K':1000})
    for x in scrip:
      if x in numbers:
        a.append(numbers[x])
    return a

  
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        script = request.form.get('code')
        return render_template('interpreter.html', output=interpret(script))        
    else:
      return render_template("interpreter.html")
  
if __name__=='__main__':
   app.run(debug=True)
