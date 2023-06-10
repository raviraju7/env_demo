import os

# Access GitHub repository secrets
env = os.environ.get('env')
#database_url = os.environ.get('DATABASE_URL')

print('hello')
print(f'this is {env} branch')
