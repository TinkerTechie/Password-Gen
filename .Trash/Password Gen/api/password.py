import string, random

def handler(request):
    length = int(request.query.get("length", 12))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(chars, length))
    return {
        "statusCode": 200,
        "body": password
    }
