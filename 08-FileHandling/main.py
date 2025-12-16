import emails  # Importujemy Twój moduł

def main():
    # 1. Wczytujemy zawartość pliku do zmiennej
    try:
        with open('email.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            
        # 2. Wywołujemy funkcje z modułu emails
        sender = emails.email_sender(content)
        recipient = emails.email_recipient(content)
        subject = emails.email_subject(content)
        body = emails.email_body(content)

        # 3. Wyświetlamy wyniki
        print(f"Sender: {sender}")
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print("-" * 20)
        print(f"Body:\n{body}")

    except FileNotFoundError:
        print("Nie znaleziono pliku email.txt!")

if __name__ == "__main__":
    main()