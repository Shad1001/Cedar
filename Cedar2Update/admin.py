from app import db, User

user_to_update = User.query.filter_by(username='admin').first()
if user_to_update:
    user_to_update.is_admin = True
    db.session.commit()