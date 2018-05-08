# -*- coding: utf-8 -*-
import json
#from functools import wraps
import shutil

import arrow
import requests
from flask import g, request, make_response, jsonify, abort
#from flask_restful import reqparse, abort, Resource
#from passlib.hash import sha256_crypt
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import func

from . import db, app, cache, logger, access_logger
from models import *
#import helper
#import helper_kk


@app.route('/')
def index_get():
    result = {
	'maxid_url': '{0}cltx/maxid'.format(request.url_root),
        'cltx_url': '%scltx{/id}?q={}' % (request.url_root),
	'cltx_list_url': '%scltx?q={}' % (request.url_root)
    }
    header = {'Cache-Control': 'public, max-age=60, s-maxage=60'}
    return jsonify(result), 200, header


@app.route('/cltx/maxid', methods=['GET'])
@cache.memoize(1)
def maxid_get():
    try:
	q = db.session.query(func.max(Vehicle.record_id)).first()
	return jsonify({'maxid': q[0]}), 200
    except Exception as e:
	logger.exception(e)


@app.route('/cltx/<int:id>', methods=['GET'])
def cltx_get(id):
    try:
        i = Vehicle.query.filter_by(record_id=id).first()
        kkdd_id = app.config['KKBH2KKDD'].get(i.tollgate_code, None)
        item = {
	    'id': i.record_id,
	    'hphm': i.plate_code,
	    'jgsj': i.pass_time.strftime('%Y-%m-%d %H:%M:%S'),
            'hpys': app.config['HPYS_DICT'].get(int(i.plate_color), {'name': u'其他', 'code': 'QT'})['name'],
	    'hpys_id': int(i.plate_color),
            'hpys_code': app.config['HPYS_DICT'].get(int(i.plate_color), {'name': u'其他', 'code': 'QT'})['code'],
	    'kkdd': app.config['KKDD2NAME'].get(kkdd_id, ''),
            'kkdd_id': kkdd_id,
            'kkbh': i.tollgate_code,
            'fxbh': app.config['FXBH2NAME'].get(int(i.lane_dir), u'其他'),
	    'fxbh_id': int(i.lane_dir),
	    'cdbh': i.lane_index,
	    'clsd': i.vehicle_speed,
            'clxs': i.limit_speed,
	    'hpzl': i.plate_type,
            'csys': i.vehicle_color,
            'cllx_id': i.vehicle_type,
	    'imgurl': i.pic1_name
        }
	return jsonify(item), 200
    except Exception as e:
	logger.exception(e)


@app.route('/cltx', methods=['GET'])
def cltx_list_get():
    q = request.args.get('q', None)
    if q is None:
	abort(400)
    try:
	args = json.loads(q)
    except Exception as e:
	logger.error(e)
	abort(400)
    try:
	limit = int(args.get('per_page', 20))
	offset = (int(args.get('page', 1)) - 1) * limit
	query = db.session.query(Vehicle)
	if args.get('startid', None) is not None:
	    query = query.filter(Vehicle.record_id >= args['startid'])
	if args.get('endid', None) is not None:
	    query = query.filter(Vehicle.record_id <= args['endid'])
	if args.get('st', None) is not None:
	    query = query.filter(Vehicle.jgsj >= arrow.get(args['st']).datetime.replace(tzinfo=None))
	if args.get('et', None) is not None:
	    query = query.filter(Vehicle.jgsj <= arrow.get(args['et']).datetime.replace(tzinfo=None))
	if args.get('hphm', None) is not None:
	    query = query.filter(Vehicle.vehicle_code == args['hphm'])
	    if args.get('st', None) is None:
		query = query.filter(Vehicle.jgsj >= arrow.now('PRC').replace(days=-1).datetime.replace(tzinfo=None))
        result = query.limit(limit).offset(offset).all()

	# 结果集为空
        if len(result) == 0:
	    return jsonify({'total_count': 0, 'items': []}), 200
	# 总数
	total = query.count()
	items = []
	for i in result:
            kkdd_id = app.config['KKBH2KKDD'].get(i.tollgate_code, None)
	    item = {
	        'id': i.record_id,
	        'hphm': i.plate_code,
	        'jgsj': i.pass_time.strftime('%Y-%m-%d %H:%M:%S'),
                'hpys': app.config['HPYS_DICT'].get(int(i.plate_color), {'name': u'其他', 'code': 'QT'})['name'],
	        'hpys_id': int(i.plate_color),
                'hpys_code': app.config['HPYS_DICT'].get(int(i.plate_color), {'name': u'其他', 'code': 'QT'})['code'],
	        'kkdd': app.config['KKDD2NAME'].get(kkdd_id, ''),
                'kkdd_id': kkdd_id,
                'kkbh': i.tollgate_code,
                'fxbh': app.config['FXBH2NAME'].get(int(i.lane_dir), u'其他'),
	        'fxbh_id': int(i.lane_dir),
	        'cdbh': i.lane_index,
	        'clsd': i.vehicle_speed,
                'clxs': i.limit_speed,
	        'hpzl': i.plate_type,
                'csys': i.vehicle_color,
                'cllx_id': i.vehicle_type,
	        'imgurl': i.pic1_name
	    }
	    items.append(item)
	return jsonify({'total_count': total, 'items': items}), 200
    except Exception as e:
	logger.exception(e)

