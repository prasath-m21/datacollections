import pywhatkit as pwk
from datetime import datetime
import time

DASHBOARD_URL = "https://prasath-m21.github.io/datacollections/dashboard.html"
PHONE_NUMBER = "+918217696151" 

def send_whatsapp_message():
    
    try:
        current_time = datetime.now()

       
        message = f"""
📊 *Hourly Data Dashboard Update*

⏰ Time: {current_time.strftime('%I:%M %p')}
📅 Date: {current_time.strftime('%d %B %Y')}

🔗 View Dashboard:
{DASHBOARD_URL}



_This is an automated message_
"""

        print(f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] Sending WhatsApp message instantly...")
        print(f"Recipient: {PHONE_NUMBER}")

        # Send instantly
        pwk.sendwhatmsg_instantly(PHONE_NUMBER, message, wait_time=15, tab_close=True)

        print("✅ WhatsApp message sent successfully!")
        print("⚠️ Note: WhatsApp Web will open automatically. Don't close it until message is sent.")

        time.sleep(10)
        print("✅ Process completed!")

    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("Make sure:")
        print("1. You're logged into WhatsApp Web on your default browser")
        print("2. Phone number is correct with country code")
        print("3. Internet connection is stable")

if __name__ == "__main__":
    print("=" * 60)
    print("WhatsApp Dashboard Link Sender")
    print("=" * 60)
    send_whatsapp_message()
