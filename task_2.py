"""
Складання розкладу занять за допомогою жадібного алгоритму

Реалізуйте програму для складання розкладу занять в університеті,
 використовуючи жадібний алгоритм для задачі покриття множини.
 Мета полягає в призначенні викладачів на предмети таким чином,
 щоб мінімізувати кількість викладачів та покрити всі предмети.

Технічні умови:
Дано множину предметів: {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
Список викладачів:
1. Олександр Іваненко, 45 років, o.ivanenko@example.com, предмети: {'Математика', 'Фізика'}
2. Марія Петренко, 38 років, m.petrenko@example.com, предмети: {'Хімія'}
3. Сергій Коваленко, 50 років, s.kovalenko@example.com, предмети: {'Інформатика', 'Математика'}
4. Наталія Шевченко, 29 років, n.shevchenko@example.com, предмети: {'Біологія', 'Хімія'}
5. Дмитро Бондаренко, 35 років, d.bondarenko@example.com, предмети: {'Фізика', 'Інформатика'}
6. Олена Гриценко, 42 роки, o.grytsenko@example.com, предмети: {'Біологія'}
"""


class Teacher:
    """Teacher class"""

    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = []

    def get_info(self):
        """Get teacher info."""
        return (
            f"{self.first_name} {self.last_name}, {self.age} років, email: {self.email}"
        )

    def __str__(self):
        return self.get_info()

    def __repr__(self):
        return self.get_info()

    def assign_subject(self, subjects):
        """Assign subject to teacher."""
        self.assigned_subjects.extend(subjects)


def get_best_teacher(teachers, subjects):
    """Get best teacher."""
    return max(
        teachers,
        key=lambda teacher: (len(teacher.can_teach_subjects & subjects), teacher.age),
    )


def create_schedule(subjects, teachers):
    """Create schedule."""
    schedule = []
    unassigned_subjects = subjects.copy()
    all_teachers_subjects = [teacher.can_teach_subjects for teacher in teachers]
    if not subjects.issubset(set.union(*all_teachers_subjects)):
        return None
    while unassigned_subjects:
        best_teacher = get_best_teacher(teachers, unassigned_subjects)
        subjects = best_teacher.can_teach_subjects & unassigned_subjects
        best_teacher.assign_subject(subjects)
        schedule.append(best_teacher)
        unassigned_subjects -= subjects

    return schedule


def main():
    """Main function."""
    subjects_ = {
        "Математика",
        "Фізика",
        "Хімія",
        "Інформатика",
        "Біологія",
    }
    # Створення списку викладачів
    teachers_ = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Микола",
            "Коваленко",
            51,
            "m.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule_ = create_schedule(subjects_, teachers_)

    # Виведення розкладу
    if schedule_:
        print("Розклад занять:")
        for teacher in schedule_:
            print(teacher)
            print(f"\tВикладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")


if __name__ == "__main__":
    main()
