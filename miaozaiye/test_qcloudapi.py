from QcloudApi.qcloudapi import QcloudApi

'''
module: 设置需要加载的模块
已有的模块列表：
cvm      对应   cvm.api.qcloud.com
cdb      对应   cdb.api.qcloud.com
lb       对应   lb.api.qcloud.com
trade    对应   trade.api.qcloud.com
sec      对应   csec.api.qcloud.com
image    对应   image.api.qcloud.com
monitor  对应   monitor.api.qcloud.com
cdn      对应   cdn.api.qcloud.com
'''
module = 'cvm'

'''
action: 对应接口的接口名，请参考wiki文档上对应接口的接口名
'''
action = 'DescribeInstances'

'''
config: 云API的公共参数
'''
config = {
    'Region': 'ap-guangzhou',
    'secretId': 'AKIDoV5UmtmzowviJhEv55ua7XmsqcBavbOz',
    'secretKey': 'bFj3Rq7D9ze6QZVFsPnEg2DD3139JUZS',
    #'method': 'GET',
    #'SignatureMethod': 'HmacSHA1'
}

# 接口参数
action_params = {
    'content':'李亚鹏挺王菲：加油！孩儿她娘。',
}

try:
    service = QcloudApi(module, config)

    # 请求前可以通过下面四个方法重新设置请求的secretId/secretKey/region/method/SignatureMethod参数
    # 重新设置请求的secretId
    secretId = 'AKIDoV5UmtmzowviJhEv55ua7XmsqcBavbOz'
    service.setSecretId(secretId)
    # 重新设置请求的secretKey
    secretKey = 'bFj3Rq7D9ze6QZVFsPnEg2DD3139JUZS'
    service.setSecretKey(secretKey)
    # 重新设置请求的region
    region = 'ap-shanghai'
    service.setRegion(region)
    # 重新设置请求的method
    method = 'POST'
    service.setRequestMethod(method)
    # 重新设置请求的SignatureMethod
    SignatureMethod = 'HmacSHA256'
    service.setRequestMethod(SignatureMethod)

    # 生成请求的URL，不发起请求
    print(service.generateUrl(action, action_params))
    # 调用接口，发起请求
    print(service.call(action, action_params))
except Exception as e:
    import traceback
    print('traceback.format_exc():\n%s' % traceback.format_exc())