import pywhatkit as pwk
from datetime import datetime
import time

# ==================== CONFIGURATION ====================
# Replace with your GitHub Pages URL
DASHBOARD_URL = ""

# Replace with recipient's phone number (with country code)
PHONE_NUMBER = "+918217696151"  # Example: Indian number

# ==================== MAIN FUNCTION ====================
def send_whatsapp_message():
    """Send WhatsApp message with dashboard link"""
    
    try:
        # Get current time
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute + 2  # Send after 2 minutes
        
        # Prepare message
        message = f"""
📊 *Hourly Data Dashboard Update*

⏰ Time: {current_time.strftime('%I:%M %p')}
📅 Date: {current_time.strftime('%d %B %Y')}

🔗 View Dashboard:
{DASHBOARD_URL}

💡 This dashboard shows real-time data from all users across all devices.

_This is an automated message_
"""
        
        print(f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] Preparing to send WhatsApp message...")
        print(f"Recipient: {PHONE_NUMBER}")
        print(f"Scheduled time: {hour}:{minute}")
        
        # Send WhatsApp message
        pwk.sendwhatmsg(PHONE_NUMBER, message, hour, minute)
        
        print("✅ WhatsApp message sent successfully!")
        print("⚠️ Note: WhatsApp Web will open automatically. Don't close it until message is sent.")
        
        # Wait for WhatsApp to send the message (20 seconds)
        time.sleep(20)
        
        print("✅ Process completed!")
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("Make sure:")
        print("1. You're logged into WhatsApp Web on your default browser")
        print("2. Phone number is correct with country code")
        print("3. Internet connection is stable")

# ==================== RUN THE SCRIPT ====================
if __name__ == "__main__":
    print("=" * 60)
    print("WhatsApp Dashboard Link Sender")
    print("=" * 60)
    send_whatsapp_message()
