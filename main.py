from pyscript import document  # type: ignore[reportMissingImports]

# list of cadet officers over the rank of 2nd LT
CO10 = {"Julian Anaque", "Carlos Borromeo", "Jan Cabading", "Francis Fernandez", "Jacob Minguillo", "Darvine Mitchell"}
CO9 = {"Erich Garaza", "Georgina Gamponia", "Kevin Goda", "Kaitlyn Mediarito", "Venice Magdayao", "Ondrea Torres"}

COC = CO10 | CO9 # intersect

def check_cos(e):
    global COC  

    f_name = document.getElementById("Fname").value.strip().title() # grab first name
    l_name = document.getElementById("Lname").value.strip().title() # grab second name

    if f_name and l_name:
        cocc = f"{f_name} {l_name}" # = user input
        plebs = {cocc}
        
        COC = COC | plebs

        document.getElementById("Fname").value = ""
        document.getElementById("Lname").value = ""

    cadetofficers = "<br>".join(sorted(COC))
    total_count = len(COC)
            
    output_text = f"ALL MEMBERS:<br>{cadetofficers}<br><br>TOTAL MEMBERS: {total_count}"
            
    document.getElementById("output1").innerHTML = output_text