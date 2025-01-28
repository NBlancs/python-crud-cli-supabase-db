from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client
from datetime import datetime

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")


supabase = create_client(url, key)

## 1

# # Insert Data
# data = supabase.table("taskCollection").insert({
#     "taskDetail": "Create a CLI CRUD application with supabase as database",
#     "taskStatus": "Complete",
#     "created_at": datetime.now().isoformat()
# }).execute()

# # Assert we pulled real data.
# assert len(data.data) > 0

## 2

# # Select Data

# data = supabase.table("taskCollection").select("*").execute()

# # Assert we pulled real data.
# assert len(data.data) > 0
# print(data)

## 3

# # Update Data

# data = supabase.table("taskCollection").update({
#     "taskDetail": "Update the table in the supabase table with an ID of 2", 
#     "taskStatus": "Completed",
#     "created_at": datetime.now().isoformat()
# }).eq("id", 2).execute()

# print(data)

## 4 

# # Delete Data

# data = supabase.table("taskCollection").delete().eq("id", 2).execute()