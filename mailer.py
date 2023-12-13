import smtplib

def automatic_email():
    user = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    message = (f"Dear {user},\n ")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("amitofficial341999@gmail.com", "dxug rqux izab gnkb")
try:
    # s.sendmail('&&&&&&&&&&&', email, message)
    s.sendmail('amitofficial341999@gmail.com', email, message)
    print("Email Sent!")
except Exception as e:
    print(f"An error occurred: {e}")

    
automatic_email()