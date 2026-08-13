with open("client_notes.txt", "w") as file:
    file.write("Client: ABC Manufacturing\n")
    file.write("Needs quotation automation\n")
    file.write("follow up on friday")

with open("client_notes.txt", "a") as file:
    file.write("\nStatus: Interested")

with open("client_notes.txt", "r") as file:
          notes = file.read()

print(notes)

with open("client_notes.txt", "r") as file:
      for line in file:
            print(line, end="")

print()

with open("client_log", "w") as file:
      file.write("Client: Rahul Packaging")

with open("client_log", "a") as file:
      file.write("\nmeeting booked")

with open("client_log", "a") as file:
      file.write("\nProposal pending")

with open("client_log", "r") as file:
      notes = file.read()

with open("client_log", "r") as file:
      for line in file:
            print(line, end="")
print()