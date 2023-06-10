import os
import sys

# Access GitHub repository secrets
env = os.environ.get('env')
env_n = os.environ.get('ENV.ENV')
env_oth = os.environ.get('GITHUB_ENV')

e = argv[1]
print(e)

print('hello')
print(f'this is {env} branch {env_n}')
