import ollama

def explain_forecast(product_id, warehouse_id, model_used, forecast):
    """
    Generate a business-friendly explanation of the forecast.
    """

    forecast_text = "\n".join(
        [f"Day {item['day']}: {item['forecast_units']} units"
         for item in forecast]
    )

    prompt = f"""
You are an ERP Demand Forecasting Assistant.

Product ID: {product_id}
Warehouse ID: {warehouse_id}
Forecast Model: {model_used}

Forecast:
{forecast_text}

Explain:
1. Overall demand trend.
2. Any increase or decrease.
3. Inventory recommendation.
4. Keep it under 150 words.
Use simple business language.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]