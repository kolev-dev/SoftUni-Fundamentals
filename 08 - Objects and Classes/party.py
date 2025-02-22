class Party:
    def __init__(self):
        self.people = []


party_ins = Party()

while True:
    name = input()

    if name == "End":
        break

    party_ins.people.append(name)

print(f"Going: {', '.join(party_ins.people)}")
print(f"Total: {len(party_ins.people)}")