'''class amazon_s3():
    global s3
    s3 = boto.connect_s3()
    
    def create_bucket(self,bucket_name,key_name,file_name):
        try:
            bucket = s3.create_bucket(bucket_name)
            key = bucket.new_key(key_name)
            key.set_contents_from_filename(file_name)
            print "successfully created"
        except:
            print "Error in creating the bucket"
        
    #def get_buckets(self,bucket_name):
      #  conn = S3Connection('AKIAJDEEIWGQ2VYALI3Q','n+VfAgg4huFwScC/IisIBZTtP9dpV937YQn4iH54')
      #  mybucket = conn.get_bucket(bucket_name)
     #   mybucket.get_key( )'''
        
        
 #from boto.s3.connection import S3Connection
#from boto import rds       
        
#def connect_to_db(self):