email = input("Enter Your Email: ").strip()
username=email[:email.index('@')]
domain=email[email.index('@')+1:]
print(f"your username is {username}& domain is{domain}")