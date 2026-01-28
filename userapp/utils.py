import threading

def send_email_async(email_message):
    """Send email in background to avoid blocking Render workers."""
    threading.Thread(
        target=email_message.send,
        kwargs={'fail_silently': False}
    ).start()