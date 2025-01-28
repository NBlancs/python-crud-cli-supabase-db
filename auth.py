from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client


# try catch
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")


supabase = create_client(url, key)

# Sign-up

users_email = "noelblanco369@gmail.com"
users_password = "meowmeow"

# user = supabase.auth.sign_up({ "email": users_email, "password": users_password })

# Sign-in

session = supabase.auth.sign_in_with_password({ "email": users_email, "password": users_password })

print(session)

## sign out

supabase.auth.sign_out()