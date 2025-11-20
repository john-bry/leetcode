# Basic API endpoints

from typing import Any, Dict

from fastapi import Body, FastAPI, HTTPException

app = FastAPI()

@app.get('/')
def home():
    return "Hello, World!"

@app.get('/api/v1/users')
def get_users():
    return {'users': ['user1', 'user2', 'user3']}

@app.get('/api/v1/users/{user_id}')
def get_user(user_id: int):
    return {'user': {'id': user_id, 'name': 'user1', 'email': 'user1@example.com'}}

# Create new user with name, id, email, and birthdate
@app.post('/api/v1/users')
def create_user(body: Dict[str, Any] = Body(...)):
    # Extract fields from request body
    name = body.get('name')
    id = body.get('id')
    email = body.get('email')
    birthdate = body.get('birthdate')
    
    # Validate required fields
    if not name or not id or not email or not birthdate:
        raise HTTPException(status_code=400, detail='Missing required fields')
    
    # Create user in database
    # create_user(name, id, email, birthdate)
    
    return {
        'message': 'User created successfully',
        'user': {
            'id': id,
            'name': name,
            'email': email,
            'birthdate': birthdate
        }
    }

@app.put('/api/v1/users/{user_id}')
def update_user(user_id: int):
    return {'message': 'User updated successfully'}

@app.delete('/api/v1/users/{user_id}')
def delete_user(user_id: int):
    return {'message': 'User deleted successfully'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

