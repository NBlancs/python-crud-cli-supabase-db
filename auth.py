from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client
from supabase.lib.client_options import ClientOptions

# try catch
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

# Sign-up

users_email = "noelblanco369@gmail.com"
users_password = "meowmeow"

# user = supabase.auth.sign_up({ "email": users_email, "password": users_password })

# Sign-in
session = None
try:
    session = supabase.auth.sign_in_with_password({
        "email": users_email,
        "password": users_password
    })
    print("Login successful!")
    print(f"User session: {session}")
except Exception as e:
    if "Invalid login credentials" in str(e):
        print("Error: Invalid password or email")
    elif "User not found" in str(e):
        print("Error: User does not exist")
    else:
        print(f"Error: {str(e)}")

## sign out

supabase.auth.sign_out()