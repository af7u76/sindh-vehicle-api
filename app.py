# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/vehicle", methods=["POST"])
def vehicle_report():
    data = request.get_json()
    reg_no = data.get("reg_no", "NULL")
    cnic = data.get("cnic", "NULL")
    vehicle_type = data.get("vehicle_type", "4W")
    
    url = "https://taxportal.excise.gos.pk:443/TaxPortalAppServices/RoutVehicleSearching"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic V2ViUG9ydGFsOlNhcHBoaXJlQDEyMw=="
    }
    payload = {
        "_USER_ID_": "WebPortal",
        "_PASSWORD_": "Sapphire@123",
        "_VEHICLE_CATEGORY_": vehicle_type,
        "_REGISTRATION_NO_": reg_no,
        "_CNIC_NO_": cnic,
        "_CHASSIS_NO_": "NULL",
        "_ENGINE_NO_": "NULL"
    }

    try:
        response = requests.post(url, headers=headers, json=payload, verify=True, timeout=60)
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
