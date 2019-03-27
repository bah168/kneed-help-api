# # security/security_admin_views/utilities.py
# import datetime as dt
#
# def get_user_token(uid, minutes_to_expire):
#     payload = {
#         'identity': uid,
#         'iat': dt.datetime.utcnow(),
#         'exp': dt.datetime.utcnow() + dt.timedelta(minutes=minutes_to_expire),
#         'nbf': dt.datetime.utcnow(),
#     }
