from pyscript import document, display

def create_order(e):
    document.getElementById("output1").innerHTML = ""  # Clear previous output
    document.getElementById("output3").innerHTML = ""  # Clear previous output
    document.getElementById("output2").innerHTML = ""  # Clear previous output

    subtotal = 0

    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    prod6 = document.getElementById("item6")
    if prod1.checked:
        subtotal = subtotal + float(prod1.value)
    if prod2.checked:
        subtotal = subtotal + float(prod2.value)
    if prod3.checked:
        subtotal = subtotal + float(prod3.value)
    if prod4.checked:
        subtotal = subtotal + float(prod4.value)
    if prod5.checked:
        subtotal = subtotal + float(prod5.value)
    if prod6.checked:
        subtotal = subtotal + float(prod6.value)

    pesos = "PhP"
        
    display(f"{pesos}" + f"{subtotal}", target="output1")

    tax = subtotal * 0.12

    display(f"{pesos}" + f"{tax}", target="output2")

    grandtotal = subtotal + tax

    display(f"{pesos}" + f"{grandtotal}", target="output3")

def generate(e):
    document.getElementById("sku").innerHTML = ""  # Clear previous output

    category = document.getElementById('categories').value #gets value of categories
    pname = document.getElementById('productname').value   #gets value of product name
    squantity = document.getElementById('quantity').value  #gets value of quantity

    Category = category.upper()[0:2]
    Pname = pname.upper()[0:2]
    Squantities = squantity.upper()[0:4]
    Squantity = str(Squantities)
    
    finalsku = Category + "-" + Pname + "-" + Squantity

    display(f"{finalsku}", target="sku")