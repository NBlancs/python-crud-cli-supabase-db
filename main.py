from dotenv import load_dotenv
load_dotenv()
import os
from os import name, system
from supabase import create_client
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
import time

console = Console()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")


supabase = create_client(url, key)

def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('çlear')

def auth_menu():
    console.print("======== SUPABASE - AUTH MENU ========\n", style="bold green", justify="center")
    console.print("Note: When creating a new account verify it first in your email and then try signing-in\n", style="bold green", justify="center")

    console.print("1. Sign In\n", style="bold blue")
    console.print("2. Sign Up\n", style="bold cyan")
    console.print("3. Exit\n", style="bold red")

    choice = console.input("[bold green]Please input the number here: [/bold green]")

    if choice == "1":
        clear_terminal()
        sign_in()
    elif choice == "2":
        clear_terminal()
        sign_up()
    elif choice == "3":
        console.print("Goodbye!", style="bold red")
        exit()
    else:
        console.print("Invalid Input", style="bold red")
        clear_terminal()
        auth_menu()

def sign_in():
    console.print("======== SIGN IN ========\n", style="bold blue", justify="center")
    email = console.input("[bold cyan]Email: [/bold cyan]")
    print()
    password = console.input("[bold cyan]Password: [/bold cyan]")
    print()

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Signing in..."),
            transient=True,
        ) as progress:
            progress.add_task("", total=None)
            session = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            time.sleep(1)  # Add small delay for better UX
        console.print("✅ Login successful!", style="bold green", justify="center")
        clear_terminal()
        menu()
    except Exception as e:
        console.print(f"❌ Login failed: {str(e)}", style="bold red", justify="center")
        auth_menu()

def sign_up():
    console.print("======== SIGN UP ========\n", style="bold cyan", justify="center")
    email = console.input("[bold cyan]Email: [/bold cyan]")
    print()
    password = console.input("[bold cyan]Password: [/bold cyan]")
    print()


    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold cyan]Creating your account..."),
            transient=True,
        ) as progress:
            progress.add_task("", total=None)
            user = supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            time.sleep(1)  # Add small delay for better UX
        console.print("✅ Sign up successful! Please check your email to verify your account.", style="bold green", justify="center")
        auth_menu()
    except Exception as e:
        console.print(f"❌ Sign up failed: {str(e)}", style="bold red", justify="center")
        auth_menu()

def check_auth():
    try:
        session = supabase.auth.get_session()
        return session is not None
    except:
        return False

def menu():
    if not check_auth():
        console.print("❌ Please sign in first!", style="bold red", justify="center")
        auth_menu()
        return

    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========", style="bold green", justify="center")
    current_year = datetime.now().year
    console.print(f"======== {current_year} Nblancs - All Rights Reserved ™ ========\n", style="bold green",justify="center")

    console.print("1. Create\n", style="bold blue")
    console.print("2. Read\n", style ="bold cyan")
    console.print("3. Update\n", style="bold yellow")
    console.print("4. Delete\n", style = "red")
    console.print("5. Log out\n", style = "bold red")

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

    elif choice == "5":
        print( "Logout Option Chosen")
        clear_terminal()
        auth_menu()

    else:
        print("Invalid Input")
        clear_terminal()
        menu()




## 1
def insertData():
# Insert Data
    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green", justify="center")
    dataInputTaskDetail = console.input("[bold green]Task Detail: [/bold green]")
    dataInputTaskStatus = console.input("[bold green]Task Status (Complete or To-do): [/bold green]")

    try:
        data = supabase.table("taskCollection").insert({
            "taskDetail": dataInputTaskDetail,
            "taskStatus": dataInputTaskStatus,
            "created_at": datetime.now().isoformat()
        }).execute()
        
        if len(data.data) > 0:
            console.print("✅ Task successfully created!", style="bold green", justify="center")
        else:
            console.print("❌ No data was inserted", style="bold red", justify="center")
            
    except Exception as e:
        console.print(f"❌ Error inserting data: {str(e)}", style="bold red", justify="center")
    
    menu()

## 2
def selectData():
    # Select Data / View Data
    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green", justify="center")
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold cyan]Fetching tasks..."),
            transient=True,
        ) as progress:
            progress.add_task("", total=None)
            data = supabase.table("taskCollection").select("*").execute()
            time.sleep(1)  # Add small delay for better UX

        if len(data.data) == 0:
            console.print("❌ No tasks found!", style="bold red", justify="center")
            menu()
            return

        # Create a table
        table = Table(show_header=True, header_style="bold magenta")
        headers = data.data[0].keys()
        for header in headers:
            table.add_column(header)

        for item in data.data:
            table.add_row(*[str(value) for value in item.values()])

        console.print(table, justify="center")

    except Exception as e:
        console.print(f"❌ Error fetching data: {str(e)}", style="bold red", justify="center")
        menu()
        return

    # go back to menu
    while True:
        userInput = console.input('\n [bold green]Type "0" to go back to menu:  [/bold green]')
        if userInput == "0":  
            clear_terminal()
            menu()
            break
        else:
            console.print("Invalid Input. Please type '0' to return to menu.", style="bold red", justify="center")

    

## 3
def updateData():
    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green", justify="center")

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
            console.print("✅ Task successfully updated!", style="bold green", justify="center")
        else:
            console.print("❌ No data was updated", style="bold red", justify="center")
        
    except Exception as e:
        console.print(f"❌ Error updating data: {str(e)}", style="bold red", justify="center")

    menu()

## 4 
def deleteData():
    # Delete Data
    console.print("======== SUPABASE - BASIC CRUD APPLICATION EXAMPLE ========\n", style="bold green", justify="center")
    idInputDelete = console.input("[bold green]Input the ID of the task you want to delete: [/bold green]")
    
    try:
        response = supabase.table("taskCollection").delete().eq("id", idInputDelete).execute()
        if response.data:
            console.print("✅Task deleted successfully.", style="bold green", justify="center")
        else:
            console.print("❌Task with that ID does not exist.", style="bold red", justify="center")
    except Exception as e:
        console.print(f"❌An error occurred: {e}", style="bold red", justify="center")
    menu()


if __name__ == '__main__':
    auth_menu()