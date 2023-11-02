from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """ Show froyo form page"""
    return render_template('froyo_form.html')
    

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    # I used context to store my variables and values as key value pairs.
    context = {
        'user_froyo_flavor': request.args.get('flavor'),
        'user_froyo_toppings': request.args.get('toppings')
    }
    
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What's your favorite color?<br/>
        <input type="text" name="color"><br/>
        What's your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What's your favorite city?<br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit Favorites">  
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    user_favorite_color = request.args.get('color')
    user_favorite_animal = request.args.get('animal')
    user_favorite_city = request.args.get('city')
    return f'Wow, I didn\'t know {user_favorite_color} {user_favorite_animal} lived in {user_favorite_city}!'


@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Hey! Enter your secret message here.<br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit Message">  
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    user_secret_message = request.form.get('message')
    sorted_message = ''.join(sorted(user_secret_message))
    return f'Here is your secret message! {sorted_message}'

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    context = {
    'operand1':int(request.args.get('operand1', 0)),
    'operand2': int(request.args.get('operand2', 0)),
    'operation':request.args.get('operation')

    }
    
    return render_template('calculator_results.html', **context)



HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    # Get the user's name from the form
    user_name = request.args.get('users_name')
    # Get the selected hosocope sign from the form.
    horoscope_sign = request.args.get('horoscope_sign')

    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign, "Invalid")
    # Generate a random lucky number
    lucky_number = random.randint(1, 99)

    context = {
        'user_name': user_name,
        'horoscope_sign': horoscope_sign,
        'users_personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
