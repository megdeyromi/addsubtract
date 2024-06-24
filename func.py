import io
import json

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    print("Entering Python Hello World handler", flush=True)
    result = {"addition": None, "subtraction": None}
    try:
        body = json.loads(data.getvalue())
        A = body.get("A")
        B = body.get("B")

        if A is not None and B is not None:
            result["addition"] = A + B
            result["subtraction"] = A - B
        else:
            result["message"] = "Please provide both A and B"
    except (Exception, ValueError) as ex:
        print(str(ex), flush=True)
        result["message"] = "Error processing input"

    print("Values: A = {}, B = {}".format(body.get("A"), body.get("B")), flush=True)
    print("Exiting Python Hello World handler", flush=True)
    return response.Response(
        ctx, response_data=json.dumps(result),
        headers={"Content-Type": "application/json"}
    )
