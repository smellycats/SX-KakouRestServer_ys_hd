# -*- coding: utf-8 -*-
import arrow

from . import db


class Vehicle(db.Model):
    """Vehicle过车表"""
    __tablename__ = 'tbl_vehicle_record_2015_04_25'
    record_id = db.Column(db.Integer, primary_key=True)    #车辆信息编号
    tollgate_code = db.Column(db.String(16))               #卡口编号
    lane_index = db.Column(db.Integer)                     #车道编号
    lane_dir = db.Column(db.Integer)                       #车道方向
    pass_time = db.Column(db.DateTime)                     #通过时间
    plate_number = db.Column(db.Integer)                   #号牌数量
    plate_code = db.Column(db.String(32))                  #号牌号码
    plate_color = db.Column(db.String(32))                 #号牌颜色
    plate_type = db.Column(db.String(32))                  #号牌种类
    backend_plate_type = db.Column(db.String(32))
    plate_coincide = db.Column(db.Integer)
    vehicle_brand = db.Column(db.String(32))
    vehicle_colordepth = db.Column(db.Integer)
    vehicle_color = db.Column(db.String(32))
    vehicle_figure = db.Column(db.String(32))
    vehicle_type = db.Column(db.String(32))
    vehicle_speed = db.Column(db.Integer)
    limit_speed = db.Column(db.Integer)
    drive_status = db.Column(db.String(32))
    pic_number = db.Column(db.Integer)
    pic1_name = db.Column(db.String(255))
    pic2_name = db.Column(db.String(255))
    pic3_name = db.Column(db.String(255))          #图像3
    pic4_name = db.Column(db.String(255))          #图像4
    plate_pic = db.Column(db.String(255))          #车牌图像
    relate_video_addr = db.Column(db.String(255))  #关联录像地址
    identity_time = db.Column(db.Integer)          #识别时间
    identify_status = db.Column(db.Integer)        #识别状态
    deal_tag = db.Column(db.Integer)               #处理标记
    record_type = db.Column(db.Integer)            #记录类型
    section_code = db.Column(db.String(32))        #区间编号
    tollgate_code2 = db.Column(db.String(32))      #卡口编号2
    lane_index2 = db.Column(db.Integer)            #车道编号2
    lane_dir2 = db.Column(db.String(32))           #车道方向2
    pass_time2 = db.Column(db.DateTime)            #通过时间2
    place_code = db.Column(db.String(32))          #地点编码
    equipment_type = db.Column(db.String(32))      #采集类型
    dept_code = db.Column(db.String(32))           #采集机关编码
    update_time = db.Column(db.DateTime)           #更新时间
    
    def __init__(self, record_id, tollgate_code, lane_index, lane_dir,
		 pass_time, plate_number, plate_code, plate_color, plate_type,
		 backend_plate_type, plate_coincide, vehicle_brand,
                 vehicle_colordepth, vehicle_color, vehicle_figure,
                 vehicle_type, vehicle_speed, limit_speed, drive_status,
                 pic_number, pic1_name, pic2_name, pic3_name, pic4_name,
                 plate_pic, relate_video_addr, identity_time, identify_status,
                 deal_tag, record_type, section_code, tollgate_code2,
                 lane_index2, lane_dir2, pass_time2, place_code, equipment_type,
                 dept_code, update_time):
        self.record_id = record_id
        self.tollgate_code = tollgate_code
        self.lane_index = lane_index
        self.lane_dir = lane_dir
        self.pass_time = pass_time
        self.plate_number = plate_number
        self.plate_code = dplate_code
        self.plate_color = plate_color
        self.plate_type = plate_type
        self.backend_plate_type = backend_plate_type
        self.plate_coincide = plate_coincide
        self.vehicle_brand = vehicle_brand
        self.vehicle_colordepth = vehicle_colordepth
        self.vehicle_color = vehicle_color
        self.vehicle_figure = vehicle_figure
        self.vehicle_type = vehicle_type
        self.vehicle_speed = vehicle_speed
        self.limit_speed = limit_speed
        self.drive_status = drive_status
        self.pic_number = pic_number
        self.pic1_name = pic1_name
        self.pic2_name = pic2_name
        self.pic3_name = pic3_name
        self.pic4_name = pic4_name
        self.plate_pic = plate_pic
        self.relate_video_addr = relate_video_addr
        self.identity_time = identity_time
        self.identify_status = identify_status
        self.deal_tag = deal_tag
        self.record_type = record_type
        self.section_code = section_code
        self.tollgate_code2 = tollgate_code2    #卡口编号2
        self.lane_index2 = lane_index2          #车道编号2
        self.lane_dir2 = lane_dir2              #车道方向2
        self.pass_time2 = pass_time2            #通过时间2
        self.place_code = place_code            #地点编码
        self.equipment_type = equipment_type    #采集类型
        self.dept_code = dept_code              #采集机关编码
        self.update_time = update_time          #更新时间

    def __repr__(self):
        return '<Vehicle %r>' % self.record_id

