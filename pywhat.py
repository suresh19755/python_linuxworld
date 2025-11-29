import pywhatkit
import schedule
import time

booking_link = "https://,forms.gle/your-google-form-link" 
target_number = "+45454654665" 

def send_marketing_message():
    message = f"""Health Management System

Book here: {booking_link}
"""
    
    try:
        pywhatkit.sendwhatmsg_instantly(target_number, message, 15, True, 3)
        print(f"Marketing message sent successfully to {target_number}!")
    except Exception as e:
        print(f"An error occurred: {e}")

schedule.every().day.at("09:00").do(send_marketing_message)

print("Auto-scheduler started... Keep this script running.")
print("Ensure you are logged into WhatsApp Web in your default browser.")

while True:
    schedule.run_pending()
    time.sleep(1)