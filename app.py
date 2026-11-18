

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please enter a question."}), 400

    message = user_message.lower()

    # 1. Greetings
    if any(word in message.split() for word in ["hello", "hi", "hey"]):
        reply = (
            "Hello! Welcome to VoltWise! ⚡ "
            "I can help you understand electric vehicles, "
            "batteries, charging, range and EV recommendations. "
            "What would you like to know?"
        )

    # 2. Charging cost
    elif any(word in message for word in [
        "charging cost", "cost to charge", "charge cost",
        "electricity cost", "charging expense"
    ]):
        reply = (
            "EV charging cost depends on battery capacity and "
            "your electricity tariff. You can calculate it using: "
            "Energy used (kWh) × Electricity price per kWh. "
            "For example, 10 kWh at ₹8 per unit costs ₹80. "
            "Actual cost may vary due to charging losses."
        )

    # 3. Charging time
    elif any(word in message for word in [
    "charging time",
    "how long to charge",
    "how long does it take",
    "fast charging",
    "slow charging",
    "charge an ev",
    "charge an electric vehicle",
    "charging speed"
]):
        reply = (
            "EV charging time depends on battery size, charger power "
            "and the vehicle's charging capability. Home AC charging "
            "usually takes several hours, while compatible DC fast "
            "chargers can charge much faster. Check your vehicle's "
            "manual for its actual charging time."
        )

    # 4. Charging methods
    elif any(word in message for word in [
        "charging", "charger", "charging station",
        "charging point", "home charger"
    ]):
        reply = (
            "There are two common EV charging methods:\n\n"
            "1. AC Charging: Commonly used at homes and workplaces. "
            "It generally takes longer.\n"
            "2. DC Fast Charging: Available at compatible public "
            "charging stations and charges much faster.\n\n"
            "Always check charger compatibility with your EV."
        )

    # 5. Battery capacity
    elif any(word in message for word in [
        "battery capacity", "kwh", "battery size"
    ]):
        reply = (
            "Battery capacity is measured in kilowatt-hours (kWh). "
            "It indicates how much electrical energy the battery can "
            "store. Generally, a larger battery can provide more "
            "driving range, depending on vehicle efficiency."
        )
    # 6. Battery life    
    elif any(word in message for word in [
            "battery warranty", "warranty", "battery guarantee"
        ]):
                reply = (
                "EV battery warranties vary by manufacturer and model. "
                "Many manufacturers provide a separate battery warranty. "
                "Check the official warranty booklet for the exact "
                "coverage period, distance limit and conditions."
            )    
        

    # 6. Battery life and warranty
    elif any(word in message for word in [
        "battery life", "battery warranty", "battery replacement",
        "battery lifespan"
    ]):
        reply = (
            "EV battery life depends on usage, temperature, charging "
            "habits and battery management. Before buying an EV, "
            "check the manufacturer's battery warranty, coverage "
            "conditions and replacement terms."
        )

    # 7. Battery general information
    elif "battery" in message:
        reply = (
            "The battery is one of the most important parts of an EV. "
            "It stores electricity and supplies energy to the electric "
            "motor. Compare battery capacity, warranty, charging "
            "capability and driving range before buying."
        )

    # 8. EV range
    elif any(word in message for word in [
        "range", "distance", "how far", "driving range",
        "mileage", "km per charge"
    ]):
        reply = (
            "EV range is the distance an electric vehicle can travel "
            "on a fully charged battery. Range depends on battery "
            "capacity, speed, driving style, traffic, weather and "
            "air-conditioning usage. Always compare the claimed range "
            "with real-world reviews."
        )
        # 9. Advantages and disadvantages
    elif any(phrase in message for phrase in [
    "advantages and disadvantages",
    "pros and cons",
    "benefits and drawbacks"
]):
        reply = (
        "Advantages of electric vehicles:\n"
        "1. No tailpipe emissions.\n"
        "2. Lower routine maintenance.\n"
        "3. Quiet driving experience.\n"
        "4. Instant motor response.\n\n"
        "Disadvantages of electric vehicles:\n"
        "1. Charging may take longer than refuelling.\n"
        "2. Public charging availability varies by location.\n"
        "3. Initial purchase price may be higher.\n"
        "4. Driving range can vary with weather and driving style."
    )

    # 9. Advantages
    elif any(word in message for word in [
        "advantages", "benefits", "why buy", "good about ev",
        "benefit of electric"
    ]):
        reply = (
            "Advantages of electric vehicles:\n\n"
            "1. No tailpipe emissions.\n"
            "2. Lower routine maintenance requirements.\n"
            "3. Quiet driving experience.\n"
            "4. Instant electric motor response.\n"
            "5. Can have lower running costs depending on electricity "
            "and fuel prices."
        )

    # 10. Disadvantages
    elif any(word in message for word in [
        "disadvantages", "problems", "drawbacks",
        "limitations", "cons of ev"
    ]):
        reply = (
            "Some limitations of electric vehicles are:\n\n"
            "1. Public charging availability varies by location.\n"
            "2. Charging can take longer than refuelling petrol cars.\n"
            "3. Initial purchase price may be higher.\n"
            "4. Driving range can change with weather and driving style.\n"
            "5. Battery replacement can be expensive outside warranty."
        )

    # 11. Maintenance
    elif any(word in message for word in [
        "maintenance", "service", "servicing", "repair"
    ]):
        reply = (
            "EVs generally need less routine maintenance than petrol "
            "cars because they have fewer moving parts. However, "
            "tyres, brakes, suspension, coolant systems and battery "
            "health still need regular inspection."
        )

    # 12. EV vs petrol
    elif any(word in message for word in [
        "petrol", "diesel", "comparison", "difference",
        "electric vs", "ev vs"
    ]):
        reply = (
            "Electric vehicles use electric motors and rechargeable "
            "batteries. Petrol and diesel vehicles use internal "
            "combustion engines. EVs can offer lower running costs "
            "and quieter operation, while petrol vehicles generally "
            "refuel faster and may have more widely available fuel "
            "stations. The best choice depends on your travel needs."
        )
        # Budget recommendation for 10 lakh
    elif any(word in message for word in [
    "10 lakh", "₹10 lakh", "1000000"
]):
        reply = (
        "Your EV budget is ₹10 lakh! "
        "You can explore entry-level electric cars in this budget. "
        "Compare their on-road prices, driving range, battery "
        "warranty and charging facilities before buying. "
        "Use the Find Your Perfect EV section on VoltWise "
        "to explore suitable options."
    )

    # 13. Budget and price
    elif any(word in message for word in [
        "budget", "price", "cost of ev", 
        "affordable", "recommend", "suggest", "best ev"
    ]):
        reply = (
            "I can help you find a suitable electric vehicle! "
            "Please use the Find Your Perfect EV section on VoltWise. "
            "Enter your budget and preferred vehicle type to see "
            "matching EV options. You can also tell me your budget "
            "and requirements here."
        )

    # 14. Environmental benefits
    elif any(word in message for word in [
        "environment", "pollution", "eco friendly",
        "climate", "emissions"
    ]):
        reply = (
            "Electric vehicles produce no tailpipe emissions while "
            "driving. They can help reduce local air pollution. "
            "Their total environmental impact also depends on "
            "electricity generation, battery manufacturing and "
            "battery recycling."
        )
    # 15. Battery warranty
   
    # 15. Default response
    else:
        reply = (
            "I'm VoltWise, your Electric Vehicle Buyer's Assistant! ⚡\n\n"
            "I can help you with:\n"
            "• EV range and battery capacity\n"
            "• Charging methods and charging time\n"
            "• Charging cost\n"
            "• EV advantages and disadvantages\n"
            "• EV maintenance\n"
            "• EV vs petrol cars\n"
            "• Budget-based EV recommendations\n\n"
            "Please ask me an electric vehicle-related question!"
        )

    return jsonify({"reply": reply})
if __name__ == "__main__":
   app.run()
