def find_password_in_file(file_path, password_to_check):
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == password_to_check:
                return True
    return False

def main():
    file_path = 'passwords.txt'  # Можно при желании добавить свою базу паролей
    password_to_check = input("Введите пароль для проверки: ")

    if find_password_in_file(file_path, password_to_check):
        print("Пароль найден в списке.")
    else:
        print("Пароль не найден в списке.")

if __name__ == "__main__":
    main()
