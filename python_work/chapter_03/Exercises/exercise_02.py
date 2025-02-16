invitations_list = ["Victoria", "Ruby", "ELea"]
for invitation in invitations_list:
    print(f"Invite {invitation} to my party")

print(f"{invitations_list[2]} cannot come")
del invitations_list[2]
invitations_list.append("Sam")

for invitation in invitations_list:
    print(f"Invite {invitation} to my party")

print("We have a bigger table")
invitations_list.insert(0, "Carole")
invitations_list.insert(2, "John")
invitations_list.append("Adam")

for invitation in invitations_list:
    print(f"Invite {invitation} to my party")

print("We can only have 2 people, sorry")

print(f"{invitations_list.pop()} sorry you cannot come")
print(f"{invitations_list.pop()} sorry you cannot come")
print(f"{invitations_list.pop()} sorry you cannot come")
print(f"{invitations_list.pop()} sorry you cannot come")

for invitation in invitations_list:
    print(f"{invitation} you are still invited to my party")

del invitations_list[0]
del invitations_list[1]

print(invitations_list)