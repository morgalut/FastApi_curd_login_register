 
## command curl 

# for add :
 ```
curl -X POST ^
  "http://127.0.0.1:8000/tasks" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\": \"New Task\", \"description\": \"This is a new task.\", \"priority\": \"medium\"}"
```

# for Get :
curl -X GET "http://127.0.0.1:8000/tasks" -H "accept: application/json"

# for patch :
curl -X PATCH "http://127.0.0.1:8000/tasks/1/status?status=completed" -H "accept: application/json"


## to start all pogram :
uvicorn app.main:app --reload

# test register :
curl -X POST "http://127.0.0.1:8000/auth/register" -H "Content-Type: application/json" -d "{\"username\": \"mor\", \"email\": \"mor@example.com\", \"password\": \"password123\"}"

# test login:
curl -X POST "http://127.0.0.1:8000/auth/login" -H "Content-Type: application/json" -d "{\"username\": \"mor\", \"password\": \"password123\"}"
