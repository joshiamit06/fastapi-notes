'''
You can define background tasks to be run after returning a response.

This is useful for operations that need to happen after a request, 
but that the client doesn't really have to be waiting for the operation 
to complete before receiving the response.

'''

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_email(email: str, message: str):
    print(f"Sending email to {email}...")
    # Simulate email sending delay
    import time
    time.sleep(3)
    print(f"Email sent to {email}!")

@app.post("/register/")
async def register_user(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Welcome to FastAPI!") # The request does NOT wait for send_email() to finish.
    return {"message": "User registered successfully. Email will be sent shortly!"}

'''
User sends a request to /register/ with an email.

FastAPI immediately returns a response ("User registered successfully.").

Meanwhile, the send_email function runs in the background (without blocking the request).

After 3 seconds, the email gets "sent".
'''