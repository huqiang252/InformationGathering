#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/30



from scripts.share.enums import (
    EnvCode,
    MarketCode
)
from hst_users import HstongUsers



market_code = MarketCode.vbkr.name
env_code = EnvCode.pro.name
pro_hstong_users= HstongUsers(market_code=market_code,env_code=env_code)

print( pro_hstong_users.tourists.sid )
print( pro_hstong_users.vbkr_bmp_delay.sid )
print( pro_hstong_users.vbkr_lv1_basic.sid )
print( pro_hstong_users.vbkr_lv2_allus.sid )


market_code1 = MarketCode.vbkr.name
env_code1 = EnvCode.pro_sg.name
pro_sg_hstong_users= HstongUsers(market_code=market_code1,env_code=env_code1)
print( pro_sg_hstong_users.tourists.sid )
print( pro_sg_hstong_users.vbkr_bmp_delay.sid )
print( pro_sg_hstong_users.vbkr_lv1_basic.sid )
print( pro_sg_hstong_users.vbkr_lv2_allus.sid )



# market_code2 = MarketCode.vbkr.name
# env_code2 = EnvCode.uat.name
# uat_hstong_users= HstongUsers( market_code=market_code2, env_code=env_code2 )
# print( uat_hstong_users.tourists.sid )
# print( uat_hstong_users.vbkr_bmp_delay.sid )
# print( uat_hstong_users.vbkr_lv1_basic.sid )
# print( uat_hstong_users.vbkr_lv2_allus.sid )