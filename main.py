from pyscript import document, display

def create_order(e):
    document.getElementById("output2").innerHTML = "" # clears previous output
    prod1= document.getElementById("item1")
    # Calculate
    subtotal = float(prod1.value) * prod1.checked
    size = document.querySelector('input[name="size"]:checked')
    size_price = float(size.value)
    grandtotal = subtotal + size_price
    display(grandtotal, target="output2")
