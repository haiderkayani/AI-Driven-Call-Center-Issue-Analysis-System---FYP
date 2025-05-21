def extract_issue_and_urgency(english_text):
    text_lower = english_text.lower()

    if "login" in text_lower or "log in" in text_lower:
        category = "Login Issue"
    elif "payment" in text_lower or "card" in text_lower:
        category = "Payment Problem"
    elif "account" in text_lower and "block" in text_lower:
        category = "Account Suspension"
    elif "error" in text_lower or "not working" in text_lower:
        category = "App Bug"
    elif "network" or "network signals" or "WiFi" in text_lower and "not working" or "slow" in text_lower:
        category = "Network Connectivity"    
    elif "good" in text_lower or "satisfied" or "confident" in text_lower:
        category = "Feedback"
    else:
        category = "General Inquiry"

    if any(word in text_lower for word in ["urgent", "immediately", "can't access", "unable to use", "not working", "block"]):
        urgency = "High"
    elif any(word in text_lower for word in ["soon", "problem", "delay", "slow"]):
        urgency = "Medium"
    elif any(word in text_lower for word in ["good", "satisfied", "happy", "no problem", "confident"]):
        urgency = "None"
    else:
        urgency = "Low"

    return {
        "category": category,
        "description": english_text,
        "urgency": urgency
    }
