from flask import Flask, request, render_template



app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route('/')
def home():
    return render_template("coffee.html")

@app.route("/Coffee_Make",methods=['POST'])
def coffee_making():
    if request.method == 'POST':
        milk = int(request.form['milk'])
        sugar = int(request.form['sugar'])
        coffee_amount = int(request.form['coffee_amount'])
        hotwater = int(request.form['hotwater'])
        cream = int(request.form['cream'])

        print(milk)
        print(sugar)
        print(coffee_amount)
        print(hotwater)
        print(cream)

        if milk == 1 and sugar==1 and coffee_amount==1 and hotwater ==1 and cream ==1:
            Your_Coffee = "Your Regular Coffee is here ☕! Enjoy😊"
        elif milk == 3 and sugar==2 and coffee_amount ==2 and hotwater ==2 and cream ==2:
            Your_Coffee = "Your Cappuccino is here 🥤! Enjoy😊"
        elif milk == 3 and sugar ==3 and coffee_amount ==1 and hotwater ==3 and cream ==1:
            Your_Coffee = "Your Latte is here 🧋! Enjoy😊"
        elif milk ==3 and sugar ==3 and coffee_amount == 3 and hotwater ==3 and cream ==3:
            Your_Coffee = "Your Espresso is here 🍵! Enjoy😊"
        else:
            Your_Coffee = "Your Americano is here 🧉! Enjoy😊"



        return render_template("coffee.html" ,Your_Coffee = Your_Coffee,milk=milk, sugar=sugar, coffee_amount = coffee_amount, hotwater = hotwater, cream=cream)



if __name__ == '__main__':
     app.run(debug=True)
