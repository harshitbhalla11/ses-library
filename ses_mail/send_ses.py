import boto3

class SESMailer:
    # default region set to 'eu-north-1 (Stockholm)'
    def __init__(self, access_key, secret_key, region_name='eu-north-1'):
        self.client = boto3.client('ses', 
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key,
                                   region_name=region_name)
    
    def send_email(self, sender_email, recipient_email, subject, body):
        try:
            response = self.client.send_email(
                Source=sender_email,
                Destination={'ToAddresses': [recipient_email]},
                Message={
                    'Subject': {'Data': subject},
                    'Body': {'Text': {'Data': body}}
                }
            )
            print("Email sent! Message ID:", response['MessageId'])
            return True
        except Exception as e:
            print("Email sending failed:", str(e))
            return False
        

    # user needs to verify the email address before sending/ recieving email so this will verify the user.
        
    def verify_email_identity(self, identify_email_address):
        try:
            self.client.verify_email_identity(
                EmailAddress = identify_email_address
            )
            print(f"Verification email sent to {identify_email_address}.")
            return True
        except Exception as e:
            print(f"Failed to send verification email to {identify_email_address}: {str(e)}")
            return False




