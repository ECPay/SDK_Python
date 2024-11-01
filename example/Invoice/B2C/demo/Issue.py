#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票作業／開立發票／一般開立發票
* 適用於即時開立發票
'''

# 1.載入SDK程式與建立物件
import random
import time
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'ISSUE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/Issue'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
RelateNumber = 'ECPAY' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(
random.randint(1000000000, 2147483647))  # 產生測試用自訂訂單編號
ecpay_invoice.Send['RelateNumber'] = RelateNumber
ecpay_invoice.Send['CustomerID'] = ''
ecpay_invoice.Send['CustomerIdentifier'] = '97025978'
ecpay_invoice.Send['CustomerName'] = 'test'
ecpay_invoice.Send['CustomerAddr'] = 'test   zzz'
ecpay_invoice.Send['CustomerPhone'] = ''
ecpay_invoice.Send['CustomerEmail'] = 'test@local.com'
ecpay_invoice.Send['ClearanceMark'] = ''
ecpay_invoice.Send['Print'] = '1'
ecpay_invoice.Send['Donation'] = '0'
ecpay_invoice.Send['LoveCode'] = ''
ecpay_invoice.Send['CarrierType'] = ''
ecpay_invoice.Send['CarrierNum'] = ''
ecpay_invoice.Send['TaxType'] = '1'
ecpay_invoice.Send['SpecialTaxType'] = 0
ecpay_invoice.Send['SalesAmount'] = 3931
ecpay_invoice.Send['InvoiceRemark'] = 'SDK TEST Python V1.0.6'
ecpay_invoice.Send['Items'] = []
ecpay_invoice.Send['InvType'] = '07'
ecpay_invoice.Send['vat'] = '0'

# 商品資訊
ecpay_invoice.Send['Items'].append({
    'ItemSeq': 1,
    'ItemName': '商品名稱一',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 2052.0,
    'ItemTaxType': '',
    'ItemAmount': 2155,
    'ItemRemark': '商品備註一'
})
ecpay_invoice.Send['Items'].append({
    'ItemSeq': 2,
    'ItemName': '商品名稱二',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 1692.0,
    'ItemTaxType': '',
    'ItemAmount': 1777,
    'ItemRemark': '商品備註二'
})


# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print('RelateNumber：' + str(RelateNumber))
print(aReturn_Info)
print(aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'InvoiceNo' in aReturn_Info:
    print('發票號碼：' + aReturn_Info['InvoiceNo'])

