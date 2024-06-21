# refred https://github.com/Roshan-Here/Python-Stuff/blob/64d97dd58ee38412ffaea5841de4ed451842cf0b/Adv/Spam-Email.py#L27

import asyncio
import os 
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
load_dotenv()


async def sendEmailAsAleart(email_content,subject="Render Acc Expired !!!!!"):
    CONTENT = f"""
    Your Render Account Status
    {email_content}
    """
    # print(os.environ.get('EMAIL_PASS'))
    email_msg = EmailMessage()
    email_msg['subject'] = subject
    email_msg['From'] = os.environ.get('FROM_EMAIL_ID')
    email_msg.set_content(CONTENT)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(os.environ.get('FROM_EMAIL_ID'),os.environ.get('EMAIL_PASS'))
    s.sendmail(os.environ.get('FROM_EMAIL_ID'),os.environ.get('TO_EMAIL_ID'),email_msg.as_string())
    s.quit()
    return "Email Sent Sucessfully!"


# async def wow():
#     email_content = "hety"
#     await sendEmailAsAleart(email_content)
    
# asyncio.run(wow())
