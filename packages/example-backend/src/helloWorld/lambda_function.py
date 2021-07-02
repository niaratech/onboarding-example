import os
STAGE = os.getenv("STAGE", "UNDEFINED")
def lambda_handler(event, context):
    message = f"Hello {event.get('first_name')} {event.get('last_name')}!"
    print(f"STAGE={STAGE}")
    print("EVENT:===")
    print(event)
    return {
        "message": message
    }
