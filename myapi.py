from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        'name': 'John',
        'age': 17,
        'class': 'Year 12'
    }
}

@app.get('/')
def index():
    return {'name': 'First Data'}

@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(None, description=f'ID of the student you want to view.', gt=0)):
    """Path parameter"""
    return students[student_id]


# @app.get('/get-by-name/')
# def get_student(name: Optional[str] = None):
#     """Query parameter"""
#     for student_id in students:
#         if students[student_id]['name'] == name:
#             return students[student_id]
#     return {'Data': 'Not Found'}

@app.get('/get-by-name/{student_id}')
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    """Path parameters and query parameters"""
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {'Data': 'Not Found'}
