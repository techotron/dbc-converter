cd /Users/eddys/git/dbc-converter/package
zip -r9 ../dbc-converter.zip .
cd /Users/eddys/git/dbc-converter
zip -g dbc-converter.zip lambda_function.py
aws lambda update-function-code --function-name dbc-converter --zip-file fileb://dbc-converter.zip --profile intapp-devopssbx_eddy.snow@intapp.com --region eu-west-1
