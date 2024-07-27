def add_contact(contact_list, name, phone, email):
    contact_list.append({"name": name, "phone": phone, "email": email, "favorite": False})
    print(f"O contato {name} foi adicionado com sucesso.")
    return


def list_contacts(contact_list):
    print("\n ------------------------------------------")
    print("\n Lista de contatos:")
    for index, contact in enumerate(contact_list, start=1):
        favorite = "[♡]" if contact["favorite"] else "[ ]"
        print(f"{index}. {favorite} {contact['name']} | {contact['phone']} | {contact['email']}")
    print("\n ------------------------------------------")
    return


def update_contact(contact_list, contact_number, name, phone, email):
    if 0 <= contact_number - 1 < len(contact_list):
        contact_list[contact_number - 1 if contact_number > 0 else 0]["name"] = name
        contact_list[contact_number - 1 if contact_number > 0 else 0]["phone"] = phone
        contact_list[contact_number - 1 if contact_number > 0 else 0]["email"] = email
    return


def change_contact_status(contact_list, contact_number):
    if 0 <= contact_number - 1 < len(contact_list):
        if contact_list[contact_number - 1]["favorite"]:
            contact_list[contact_number - 1]["favorite"] = False
        else:
            contact_list[contact_number - 1]["favorite"] = True
    return


def list_favorite_contacts(contact_list):
    print("\n ------------------------------------------")
    print("\n Lista de contatos favoritos ♡:")
    for index, contact in enumerate(contact_list, start=1):
        if contact["favorite"]:
            favorite = "[♡]" if contact["favorite"] else "[ ]"
            print(f"{index}. {favorite} {contact['name']} | {contact['phone']} | {contact['email']}")
    print("\n ------------------------------------------")
    return


def delete_completed_tasks(contact_list, contact_number):
    if 0 <= contact_number - 1 < len(contact_list):
        contact_list.remove(contact_list[contact_number - 1])
    return


contact_list = []
while True:
    print("\n Menu do gerenciador da lista de contatos: ")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contatos")
    print("4. Marcar ou desmarcar um contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    choice = input("Digite a sua escolha: ")

    if choice == "1":
        name = input("Digite o nome do contato: ")
        phone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        add_contact(contact_list, name, phone, email)

    elif choice == "2":
        list_contacts(contact_list)

    elif choice == "3":
        list_contacts(contact_list)
        number = int(input("Digite o número do contato: "))
        name = input("Digite o nome do contato: ")
        phone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        update_contact(contact_list, number, name, phone, email)

    elif choice == "4":
        list_contacts(contact_list)
        number = int(input("Digite o número do contato: "))
        change_contact_status(contact_list, number)

    elif choice == "5":
        list_favorite_contacts(contact_list)

    elif choice == "6":
        list_contacts(contact_list)
        number = int(input("Digite o número do contato: "))
        delete_completed_tasks(contact_list, number)

    else:
        break
