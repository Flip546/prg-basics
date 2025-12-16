
import re

def email_sender(text):
    """
    Pobiera adres email nadawcy (to co jest w nawiasach < > w polu From).
    """
    # Szukamy linii zaczynającej się od From, potem dowolne znaki, aż do <
    # Następnie pobieramy to co jest w środku <>
    match = re.search(r"From:.*<(.+?)>", text)
    if match:
        return match.group(1)
    return None

def email_recipient(text):
    """
    Pobiera adres email odbiorcy (to co jest w nawiasach < > w polu To).
    """
    # Analogicznie jak wyżej, tylko dla pola To
    match = re.search(r"To:.*<(.+?)>", text)
    if match:
        return match.group(1)
    return None

def email_subject(text):
    """
    Pobiera temat wiadomości.
    """
    # Szukamy linii Subject: i pobieramy wszystko do końca tej linii
    match = re.search(r"Subject: (.+)", text)
    if match:
        return match.group(1)
    return None

def email_body(text):
    """
    Pobiera treść wiadomości.
    """
    # Treść w raw emailu zaczyna się po pierwszej pustej linii (\n\n).
    # Używamy re.DOTALL, aby kropka (.) łapała też znaki nowej linii.
    match = re.search(r"\n\n(.*)", text, re.DOTALL)
    if match:
        return match.group(1).strip() # .strip() usuwa zbędne spacje na początku/końcu
    return None