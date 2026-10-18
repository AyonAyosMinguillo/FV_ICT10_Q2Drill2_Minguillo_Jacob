from pyscript import document  # type: ignore[reportMissingImports]

# list of cadet officers over the rank of 2nd LT
CO10 = {"Julian Anaque", "Carlos Borromeo", "Jan Cabading", "Francis Fernandez", "Jacob Minguillo", "Darvine Mitchell"}
CO9 = {"Erich Garaza", "Georgina Gamponia", "Kevin Goda", "Kaitlyn Mediarito", "Venice Magdayao", "Ondrea Torres"}

COC = CO10 | CO9 # combine officer sets

def check_cos(e): # checks the officer function
    global COC  # access the global set

    f_name = document.getElementById("Fname").value.strip().title() # grab first name
    l_name = document.getElementById("Lname").value.strip().title() # grab second name

    if f_name and l_name: # check if both names are okay
        cocc = f"{f_name} {l_name}" # = user input
        plebs = {cocc} # create name set
        
        COC = COC | plebs # adds to roster

        document.getElementById("Fname").value = ""
        document.getElementById("Lname").value = ""

    # final sort of inputs and values
    cadetofficers = "<br>".join(sorted(COC)) # sorts and joins the officers
    total_count = len(COC) # counts total officers after sort
            
    output_text = f"ALL MEMBERS:<br>{cadetofficers}<br><br>TOTAL MEMBERS: {total_count}" # Format output
            
    document.getElementById("output1").innerHTML = output_text # Display final output
