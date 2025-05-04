def extract_issue_and_urgency(english_text):
    text_lower = english_text.lower()

    # Simple rule-based categorization
    if "login" in text_lower or "log in" in text_lower:
        category = "Login Issue"
    elif "payment" in text_lower or "card" in text_lower:
        category = "Payment Problem"
    elif "account" in text_lower and "block" in text_lower:
        category = "Account Suspension"
    elif "error" in text_lower or "not working" in text_lower:
        category = "App Bug"
    elif "network" in text_lower and "not working" or "slow" in text_lower:
        category = "Network Connectivity"    
    else:
        category = "General Inquiry"

    # Simple rule-based urgency tagging
    if any(word in text_lower for word in ["urgent", "immediately", "can't access", "unable to use"]):
        urgency = "High"
    elif any(word in text_lower for word in ["soon", "problem", "delay"]):
        urgency = "Medium"
    else:
        urgency = "Low"

    return {
        "category": category,
        "description": english_text,
        "urgency": urgency
    }
