import boto3

# Replace with your own AWS access key and secret access key
ACCESS_KEY = 'AKIAWUPP4KA4KIV2CAHA'
SECRET_KEY = 'pG9OUgvpL4BW16TlsAwlM+cO3zEm3gYE+W/q1EPU'

def list_s3_buckets():
    try:
        # Create an S3 client using the provided credentials
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

        # List all S3 buckets
        response = s3.list_buckets()

        # Print the names of the buckets
        print("List of S3 buckets:")
        for bucket in response['Buckets']:
            print(bucket['Name'])

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    list_s3_buckets()