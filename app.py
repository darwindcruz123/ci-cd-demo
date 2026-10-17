
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Calculator</title>
    </head>
    <body>
        <h1>Python Calculator</h1>

            <form method="POST">
                    <input type="number" step="any" name="a"
                                   placeholder="First number" required>

                                           <select name="operation">
                                                       <option value="+">Addition (+)</option>
                                                                   <option value="-">Subtraction (-)</option>
                                                                               <option value="*">Multiplication (*)</option>
                                                                                           <option value="/">Division (/)</option>
                                                                                                   </select>

                                                                                                           <input type="number" step="any" name="b"
                                                                                                                          placeholder="Second number" required>

                                                                                                                                  <button type="submit">Calculate</button>
                                                                                                                                      </form>

                                                                                                                                          <h2>Result: {{ result }}</h2>
                                                                                                                                          </body>
                                                                                                                                          </html>
                                                                                                                                          """

                                                                                                                                          @app.route("/", methods=["GET", "POST"])
                                                                                                                                          def calculator():
                                                                                                                                                  result = ""

                                                                                                                                                      if request.method == "POST":
                                                                                                                                                                  try:
                                                                                                                                                                                  a = float(request.form["a"])
                                                                                                                                                                                              b = float(request.form["b"])
                                                                                                                                                                                                          operation = request.form["operation"]

                                                                                                                                                                                                                      if operation == "+":
                                                                                                                                                                                                                                          result = a + b
                                                                                                                                                                                                                                                      elif operation == "-":
                                                                                                                                                                                                                                                                          result = a - b
                                                                                                                                                                                                                                                                                      elif operation == "*":
                                                                                                                                                                                                                                                                                                      result = a * b
                                                                                                                                                                                                                                                                                                                  elif operation == "/":
                                                                                                                                                                                                                                                                                                                                  result = a / b if b != 0 else "Cannot divide by zero"

                                                                                                                                                                                                                                                                                                                                          except ValueError:
                                                                                                                                                                                                                                                                                                                                                      result = "Invalid input"

                                                                                                                                                                                                                                                                                                                                                          return render_template_string(HTML, result=result)

                                                                                                                                                                                                                                                                                                                                                      if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                              app.run(host="0.0.0.0", port=5000)

