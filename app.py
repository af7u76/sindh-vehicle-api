from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fetch_vehicle_data(reg_no="NULL", cnic="NULL"):
    url = "https://taxportal.excise.gos.pk:443/TaxPortalAppServices/RoutVehicleSearching"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic V2ViUG9ydGFsOlNhcHBoaXJlQDEyMw=="
    }
    payload = {
        "_USER_ID_": "WebPortal",
        "_PASSWORD_": "Sapphire@123",
        "_VEHICLE_CATEGORY_": "4W",
        "_REGISTRATION_NO_": reg_no,
        "_CNIC_NO_": cnic,
        "_CHASSIS_NO_": "NULL",
        "_ENGINE_NO_": "NULL"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

# API Route
@app.route("/vehicle", methods=["POST"])
def vehicle():
    body = request.get_json()
    reg_no = body.get("reg_no", "NULL")
    cnic = body.get("cnic", "NULL")
    result = fetch_vehicle_data(reg_no, cnic)
    return jsonify(result)

# Optional: Root route for testing
@app.route("/")
def index():
    return "Sindh Vehicle API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
