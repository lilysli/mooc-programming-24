name = input("Whom should I sign this to:")
document = input("Where shall I save it:")

with open(document, "w") as f:
    f.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
