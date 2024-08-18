from flask import Flask, request, jsonify, render_template_string

# Create an instance of the Flask class
app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Currency Converter</title>
</head>
<body>
    <h1>Currency Converter</h1>
    <form id="convertForm">
        <label for="base_currency">Base Currency:</label>
        <input type="text" id="base_currency" name="base_currency"><br><br>
        <label for="target_currency">Target Currency:</label>
        <input type="text" id="target_currency" name="target_currency"><br><br>
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount" step="0.01"><br><br>
        <input type="submit" value="Convert">
    </form>
    <p id="result"></p>
    <script>
        document.getElementById('convertForm').onsubmit = function(event) {
            event.preventDefault();
            var formData = new FormData(event.target);
            var data = {
                base_currency: formData.get('base_currency'),
                target_currency: formData.get('target_currency'),
                amount: formData.get('amount')
            };
            fetch('/convert', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                document.getElementById('result').textContent = 'Converted Amount: ' + result.converted_amount;
            })
            .catch(error => {
                document.getElementById('result').textContent = 'Error: ' + error;
            });
        };
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """
    Brief: Handle the root URL of the application and render a simple HTML page.

    Return: A rendered HTML page with the content from the `render_template_string` function.
    """
    return render_template_string(HTML_TEMPLATE)

@app.route('/convert', methods=['POST'])
def convert():
    """
    Brief: Simulate a currency conversion without external API calls.

    Return: A JSON object containing the simulated converted amount.
    """
    data = request.json
    base_currency = data['base_currency']
    target_currency = data['target_currency']
    amount = float(data['amount'])

    # Simulate a currency conversion rate (for example purposes)
    simulated_rates = {
        'USD': {'EUR': 0.85, 'JPY': 110.0},
        'EUR': {'USD': 1.18, 'JPY': 129.0}
    }

    rate = simulated_rates.get(base_currency, {}).get(target_currency, None)

    if rate:
        converted_amount = round(amount * rate, 2)
        return jsonify({'converted_amount': converted_amount})
    else:
        return jsonify({'error': 'Invalid currency code'}), 400

if __name__ == '__main__':
    app.run(debug=True)


