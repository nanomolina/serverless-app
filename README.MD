# Install serverless
`npm install -g serverless`

# Get access_keys and secrets on aws: https://www.youtube.com/watch?v=D5_FHbdsjRc&list=PLmexTtcbIn_gP8bpsUsHfv-58KsKPsGEo&index=1

# Configure serverless credentials
`serverless config credentials --provider aws --key <AWS_ACCESS_KEY> --secret <AWS_SECRET_KEY> --profile <AWS_USER>`

# Deploy changes on aws
`sls deploy`


# after update telegram.py we need to add it to telegram.zip
zip -g telegram.zip telegram.py 