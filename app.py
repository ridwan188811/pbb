from flask import Flask, request, render_template

app = Flask(__name__)

# Fungsi untuk menghitung PBB dan langkah-langkahnya
def gcd_with_steps(a, b):
    steps = []
    original_a, original_b = a, b
    while b:
        quotient = a // b
        remainder = a % b
        steps.append(f"{a} / {b} = {quotient} sisa {remainder}")
        a, b = b, remainder
    steps.append(f"{original_a} = {original_b} * ({original_a // original_b}) + {original_a % original_b}")
    steps.append(f"PBB({original_a}, {original_b}) adalah {a}")
    return a, steps

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    process = []
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            result, process = gcd_with_steps(num1, num2)
            print("Result:", result)  # Output hasil PBB di konsol
            print("Process:", process)  # Output langkah-langkah di konsol
        except ValueError:
            result = "Error: Input tidak valid"
    
    # Mengirimkan data ke template
    print(f"Sending result: {result} and process: {process} to template.")
    return render_template('index.html', result=result, process=process)

if __name__ == '__main__':
    app.run(debug =True,port=5500)
