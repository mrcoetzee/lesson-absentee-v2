import csv
import os
import django

# Set the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lessonabsentees.settings")
django.setup()

# Import your Django models
from base.models import Learner

def add_data_from_csv(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        print(reader.fieldnames)
        for row in reader:
           
                name = row['name']
                grade_id = row['grade_id']
                reg_class = row['reg_class']

                print(f"Row values: {name}, {grade_id}, {reg_class}")
                Learner.objects.create(
                    name=name,
                    grade_id=grade_id,
                    reg_class=reg_class
                    # Add other fields as needed
                )


if __name__ == "__main__":
    csv_file_path = 'C:/Users/AKL/Desktop/Learners.csv'
    add_data_from_csv(csv_file_path)
