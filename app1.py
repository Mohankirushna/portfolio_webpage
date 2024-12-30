from flask import Flask, request
import cx_Oracle

app = Flask(__name__)

# Set up the Oracle connection
conn = cx_Oracle.connect("HR/Mo@070805@Mac.lan:1521/ORCL")
cursor = conn.cursor()

@app.route('/submit-message', methods=['POST'])
def submit_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Insert into the messages table
    cursor.execute("""
        INSERT INTO messages (name, email, message)
        VALUES (:name, :email, :message)
    """, {'name': name, 'email': email, 'message': message})
    
    conn.commit()
    return "Message Submitted Successfully!", 200

if __name__ == '__main__':
    app.run(debug=True)
