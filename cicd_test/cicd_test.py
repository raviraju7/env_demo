import os
import sys

# Access GitHub repository secrets
# correct way to receive the parameter



env = os.environ.get('env')
env_var = os.environ.get('env_var')

#incoorect way to get the parameter - env_n wont get the value
env_n = os.environ.get('ENV.ENV')

#ways to get the github env variables
#env_oth = os.environ.get('GITHUB_ENV')

#below method of receiving the parameter works
#e = sys.argv[1]
#print(e)
print('cicd test')
print('hello test')
print(f'this is {env} branch {env_n} and {env_var}')
