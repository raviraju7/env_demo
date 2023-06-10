import os

# Access GitHub repository secrets
env = os.environ.get('env.env')
env_n = os.environ.get('ENV.ENV')
env_oth = os.environ.get('GITHUB_ENV')

print('hello')
print(f'this is {env} branch {env_n}')
