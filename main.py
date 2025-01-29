from dotenv import load_dotenv
load_dotenv()
import os
from os import name, system
from supabase import create_client
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")


supabase = create_client(url, key)

def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('çlear')

def menu():

    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green")

    console.print("1. Create\n", style="bold blue")
    console.print("2. Read\n", style ="bold cyan")
    console.print("3. Update\n", style="bold yellow")
    console.print("4. Delete\n", style = "bold red")

    choice = console.input("[bold green]Please input the number here: [/bold green]")

    if choice == "1":
        print( "Create Option Chosen")
        clear_terminal()
        insertData()

    elif choice == "2":
        print( "Read Option Chosen")
        clear_terminal()
        selectData()
       
    elif choice == "3":
        print( "Update Option Chosen")
        clear_terminal()
        updateData()

    elif choice == "4":
        print( "Delete Option Chosen")
        clear_terminal()
        deleteData()

    else:
        print("Invalid Input")
        clear_terminal()
        menu()


## 1
def insertData():
# Insert Data
    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green")
    dataInputTaskDetail = console.input("[bold green]Task Detail: [/bold green]")
    dataInputTaskStatus = console.input("[bold green]Task Status (Complete or To-do): [/bold green]")

    try:
        data = supabase.table("taskCollection").insert({
            "taskDetail": dataInputTaskDetail,
            "taskStatus": dataInputTaskStatus,
            "created_at": datetime.now().isoformat()
        }).execute()
        
        if len(data.data) > 0:
            print("✅ Task successfully created!")
        else:
            print("❌ No data was inserted")
            
    except Exception as e:
        print(f"❌ Error inserting data: {str(e)}")
    
    menu()

## 2
def selectData():
    # Select Data / View Data
    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green")
    data = supabase.table("taskCollection").select("*").execute()

    # Assert we pulled real data.
    assert len(data.data) > 0

    # Create a table
    table = Table(show_header=True, header_style="bold magenta")
    headers = data.data[0].keys()
    for header in headers:
        table.add_column(header)

    for item in data.data:
        table.add_row(*[str(value) for value in item.values()])

    console.print(table)



    # go back to menu
    while True:
        userInput = console.input('\n [bold green]Type "0" to go back to menu:  [/bold green]')
        if userInput == "0":  
            clear_terminal()
            menu()
            break
        else:
            console.print("Invalid Input. Please type '0' to return to menu.", style="bold red")

    

## 3
def updateData():
    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green")

    # Update Data
    idInputUpdate = console.input("[bold green]Input the ID of the task you wish to update: [/bold green]")
    updateDataInputTaskDetail = console.input("[bold green]Task Detail: [bold green]")
    updateDataInputTaskStatus = console.input("[bold green]Task Status (Complete or To-do): [/bold green]")

    try:
        data = supabase.table("taskCollection").update({
            "taskDetail":  updateDataInputTaskDetail, 
            "taskStatus": updateDataInputTaskStatus,
            "created_at": datetime.now().isoformat()
        }).eq("id", idInputUpdate).execute()
        if len(data.data) > 0:
            print("✅ Task successfully updated!")
        else:
            print("❌ No data was updated")
        
    except Exception as e:
        print(f"❌ Error updating data: {str(e)}")

    menu()

## 4 
def deleteData():
    # Delete Data
    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green")
    idInputDelete = console.input("[bold green]Input the ID of the task you want to delete: [/bold green]")
    
    try:
        response = supabase.table("taskCollection").delete().eq("id", idInputDelete).execute()
        if response.data:
            print("✅Task deleted successfully.")
        else:
            print("❌Task with that ID does not exist.")
    except Exception as e:
        print(f"❌An error occurred: {e}")
    menu()


if __name__ == '__main__':
    menu()