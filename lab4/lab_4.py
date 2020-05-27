from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox,SHConfig,DataSource,AwsProductRequest,AwsTile,AwsTileRequest
import datetime
import numpy as np

import matplotlib.pyplot as plt

INSTANCE_ID = '91755d3d-ff3c-44a4-a161-67bc55524b9c'  # In case you put instance ID into configuration file you can leave this unchanged

if INSTANCE_ID:
    config = SHConfig()
    config.instance_id = INSTANCE_ID
else:
    config = None

product_id = 'S2A_MSIL2A_20190821T085601_N0213_R007_T36UUA_20190821T115206'
data_folder = 'A:\\lab4'

product_request = AwsProductRequest(product_id=product_id,
                                    data_folder=data_folder, safe_format=True)
product_request.save_data()
