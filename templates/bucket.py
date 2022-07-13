# Copyright 2020 Dell Boomi. All rights reserved.




""" This template creates a Bucket"""


def generate_config(context):

    """ Entry point for the deployment resources. """

    deployment = context.env['deployment']
    bucketname = deployment + '-bucket'
    reg = context.properties['location']  
    

    
    resources = []
    resources.append(
       {
            'name': 'CreateBucket',
            'type': 'gcp-types/storage-v1:buckets',
            'properties':
                {
                  "name" : bucketname,
                  "locationtype" : "Region",
                  "location" : reg,                  
                  "storageClass" : "Standard"                                                          
                                                                    
                }
        }

    )   
    resources.append(
            {
                'name': 'Cloudbuild',
                'type': 'cloudbuild.jinja',
                'properties': 
                  {
                    'bucketname' : bucketname

                  },
                'metadata': {      'dependsOn': ['CreateBucket']
                     }
            }
        )          

    return{
        'resources': resources        

    }
    
