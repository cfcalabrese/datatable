import json
from flask import Flask, jsonify, request, Response
from pandas import DataFrame, read_sql
from uuid import uuid4
import sqlite3

app = Flask(__name__)

query = "select * from audatex_approvals_list"
CONN = sqlite3.connect("names.db", check_same_thread=False)
cur = CONN.cursor()
df = read_sql(query, con=CONN)
df["UUID"] = None
df["UUID"] = df["UUID"].apply(lambda x: uuid4().hex)
data = df.to_dict(orient="records")

@app.route("/api/v1/data", methods=["GET", "POST"])
def all_approvals() -> Response:
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        data.append({
            "UUID": post_data.get("UUID"),
            "AUDATEX_SITE_ID": post_data.get("AUDATEX_SITE_ID"),
            "GARAGE_NAME": post_data.get("GARAGE_NAME"),
            "APPROVAL_TYPE": post_data.get("APPROVAL_TYPE"),
            "APPROVAL_SUBTYPE": post_data.get("APPROVAL_SUBTYPE"),
            "START_DATE": post_data.get("START_DATE"),
            "END_DATE": post_data.get("END_DATE")
        })
        response_object["message"] = "Record added!"
    else:
        response_object["approvals"] = data

    response = jsonify(response_object)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/api/v1/data/<uuid>", methods=["GET", "PUT", "DELETE"])
def single_approval(uuid: str) -> Response:
    if uuid_exists(uuid):
        response_object = {"status": "success"}
        if request.method == "PUT":
            put_data = request.get_json()
            remove_approval(uuid)
            data.append({
                "UUID": uuid,
                "AUDATEX_SITE_ID": put_data.get("AUDATEX_SITE_ID"),
                "GARAGE_NAME": put_data.get("GARAGE_NAME"),
                "APPROVAL_TYPE": put_data.get("APPROVAL_TYPE"),
                "APPROVAL_SUBTYPE": put_data.get("APPROVAL_SUBTYPE"),
                "START_DATE": put_data.get("START_DATE"),
                "END_DATE": put_data.get("END_DATE")            
            })
            response_object["message"] = "Approval updated!"
        if request.method == "DELETE":
            remove_approval(uuid)
            response_object["message"] = "Approval deleted!"
        if request.method == "GET":
            response_object["message"] = "Approval retrieved!"
            response_object["approval"] = retrieve_approval(uuid)
    else:
        response_object = {
            "status": "failure",
            "message": "uuid does not exist!"
        }

    response = jsonify(response_object)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/api/v1/submit", methods=["POST"])
def submit_changes() -> Response:
    to_write = DataFrame.from_dict(data)
    to_write = to_write.drop("UUID", axis=1)
    truncate = "delete from audatex_approvals_list"
    if request.method == "POST":
        try:
            response_object = {
                "status": "success",
                "message": "Data written to table!"
            }
            cur.execute(truncate)
            to_write.to_sql(
                name="audatex_approvals_list",
                con=CONN,
                if_exists="append",
                index=False,
                chunksize=10000
            )
            response = jsonify(response_object)
        except Exception as e:
            response_object = {
                "status": "failure",
                "message": f"failed writing to table: {e}"
            }
            response = jsonify(response_object)
    return response

def remove_approval(uuid: str) -> bool:
    """Helper function for `single_approval` function -
    removes approval corresponding to `uuid`. 

    Args:
        uuid (string): uuid for item being edited.

    Returns:
        Bool: False if uuid does not exist; True if exists.
    """

    for approval in data:
        if approval["UUID"] == uuid:
            data.remove(approval)
            return True

def retrieve_approval(uuid: str) -> dict:
    """Helper function for `single_approval` function -
    retrieves approval corresponding to `uuid`.

    Args:
        uuid (string): uuid for item being retrieved.

    Returns:
        approval (dict): J
    """

    for approval in data:
        if approval["UUID"] == uuid:
            return approval

def uuid_exists(uuid: str) -> bool:
    """Helper function - checks if approval with `uuid` exists in dataset.

    Args:
        uuid (string): `uuid` for given approval.

    Returns:
        Bool: True if exists, else False.
    """

    if any(approval["UUID"] == uuid for approval in data):
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)