import json
import os
import logging
import boto3
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    logger.info("Request recibido: %s %s", event.get("httpMethod"), event.get("path"))

    try:
        visit_id = datetime.now().isoformat()

        table.put_item(
            Item={
                "id": visit_id,
                "timestamp": visit_id,
                "path": event.get("path", "/unknown"),
            }
        )

        response = table.scan()
        total_visits = response["Count"]

        logger.info("Visita registrada: %s | Total: %d", visit_id, total_visits)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello world",
                "visit_id": visit_id,
                "total_visits": total_visits
            })
        }

    except Exception as e:
        logger.error("Error procesando request: %s", str(e), exc_info=True)

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Internal server error"
            })
        }