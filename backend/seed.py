from app import create_app
from app.extensions import db
from app.models.role import Role
from app.models.user import User

app = create_app()

with app.app_context():

    # Create roles
    roles = ["Admin", "Trek Staff", "Trekker"]

    for role_name in roles:
        role = Role.query.filter_by(name=role_name).first()

        if not role:
            db.session.add(Role(name=role_name))

    db.session.commit()

    # Create admin user
    admin_role = Role.query.filter_by(name="Admin").first()

    admin = User.query.filter_by(
        email="admin@tma.com"
    ).first()

    if not admin:
        admin = User(
            name="Admin",
            email="admin@tma.com",
            role_id=admin_role.id
        )
        admin.set_password("admin123")

        db.session.add(admin)
        db.session.commit()

        print("Admin user created.")

    else:
        print("Admin user already exists.")