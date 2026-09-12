from pyscript import document, display

def adding_numbers(e):
    document.getElementById("output1").innerHTML = ""     # clears previous output
    num1 = float(document.getElementById('input1').value) # get 1st output
    num2 = float(document.getElementById('input2').value) # get 2nd output
    result = num1 + num2                                  # use operator to compute
    display(result, target = "output1")                   # display output in div

def create_order(e):
    document.getElementById("output2").innerHTML = "" # clears previous output
    prod1= document.getElementById("item1")
    # Calculate
    subtotal = float(prod1.value) * prod1.checked
    size = document.querySelector('input[name="size"]:checked')
    size_price = float(size.value)
    grandtotal = subtotal + size_price
    display(grandtotal, target="output2")

def place_order(e):
    document.getElementById("output3").innerHTML = "" # clears previous output
    coffee = document.getElementById("coffee")
    coffee_price = float(coffee.value)
    display(f'Pay{coffee_price}', target="output3")