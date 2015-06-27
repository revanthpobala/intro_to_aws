echo "Enter the file/folder name you want to upload"
read file_name
scp -v -i ~/.ssh/aws.pem -r  $file_name ubuntu@ec2-52-28-133-51.eu-central-1.compute.amazonaws.com:~





# ssh -i ~/.ssh/aws.pem ubuntu@ec2-52-28-133-51.eu-central-1.compute.amazonaws.com

