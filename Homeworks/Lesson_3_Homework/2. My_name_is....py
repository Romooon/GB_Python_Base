def person(name, surname, year, city, email, phone_number):
    result = f'Имя, фамилия: {name}, {surname}. Год рождения: {year}, город проживания: {city}, email: {email}, номер телефона: {phone_number}'

    return result

print(person('Роман', 'Марфин', 2000, 'Шахты', 'marfutin.00@mail.ru', '+79381557575'))