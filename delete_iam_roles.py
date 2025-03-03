import boto3
import datetime
import time

# AWS Credentials (ensure these are set up in your environment or environment variables)
session = boto3.Session()
iam = session.client('iam')

#List of IAM roles to delete
roles_to_delete = ['AWSAmplifyCodeCommitExecutionRole-d32rytyz2bnr67 ',
                    'AWSCodePipelineServiceRole-us-east-1-pipeline-secondDevopsGetti ',
                      'AWSCodePipelineServiceRole-us-west-2-meme-draft-pipeline'] # Replace with your actual role names

#Define the scheduled deletion time (24-hour format: HH:MM)
scheduled_deletion_time = "15:50"  # Replace with your desired time

# Function for deleting roles

def delete_iam_roles(role):
    try:
        iam.delete_role(RoleName=role)
        print(f"Role '{role}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting role '{role}': {e}")
    except iam.exceptions.NoSuchEntityException:
        print(f"Role '{role}' does not exist.")


def wait_until_scheduled_time():
    """Waits until scheduled time to delete roles. """

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == scheduled_deletion_time:
            print("Scheduled time reached. Deleting roles...")
            for role in roles_to_delete:
                delete_iam_roles(role)
            break
        time.sleep(20)  # Check every 20 seconds

if __name__ == "__main__":
    wait_until_scheduled_time()

