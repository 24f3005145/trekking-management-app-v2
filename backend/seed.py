
from datetime import date, timedelta
from app import create_app
from app.extensions import db
from app.models.role import Role
from app.models.user import User
from app.models.staff_profile import StaffProfile
from app.models.trek import Trek
from app.models.booking import Booking

app = create_app()

def get_role(name):
    return Role.query.filter_by(name=name).first()

with app.app_context():
    roles=["Admin","Trek Staff","Trekker"]
    for r in roles:
        if not Role.query.filter_by(name=r).first():
            db.session.add(Role(name=r))
    db.session.commit()

    admin_role=get_role("Admin")
    staff_role=get_role("Trek Staff")
    trekker_role=get_role("Trekker")

    if not User.query.filter_by(email="admin@tma.com").first():
        u=User(name="Admin",email="admin@tma.com",phone="9999999999",role_id=admin_role.id)
        u.set_password("admin123")
        db.session.add(u)
        db.session.commit()

    staff_data=[
        ("Rahul Sharma","rahul@tma.com"),
        ("Priya Singh","priya@tma.com"),
        ("Aman Verma","aman@tma.com"),
        ("Neha Kapoor","neha@tma.com"),
        ("Vikram Joshi","vikram@tma.com"),
    ]
    staff_users=[]
    for i,(n,e) in enumerate(staff_data,1):
        u=User.query.filter_by(email=e).first()
        if not u:
            u=User(name=n,email=e,phone=f"900000000{i}",role_id=staff_role.id)
            u.set_password("staff123")
            db.session.add(u); db.session.commit()
        if not StaffProfile.query.filter_by(user_id=u.id).first():
            db.session.add(StaffProfile(user_id=u.id,contact_details=u.phone,status="Active"))
            db.session.commit()
        staff_users.append(u)

    trekkers=[]
    trekker_data=[
        ("Arjun Mehta","arjun@tma.com"),
        ("Riya Patel","riya@tma.com"),
        ("Kunal Shah","kunal@tma.com"),
        ("Sneha Roy","sneha@tma.com"),
        ("Aditya Rao","aditya@tma.com"),
        ("Pooja Nair","pooja@tma.com"),
    ]
    for i,(n,e) in enumerate(trekker_data,1):
        u=User.query.filter_by(email=e).first()
        if not u:
            u=User(name=n,email=e,phone=f"800000000{i}",role_id=trekker_role.id)
            u.set_password("trekker123")
            db.session.add(u); db.session.commit()
        trekkers.append(u)

    trek_data=[
      ("Valley of Flowers","Uttarakhand","Easy",5,"A UNESCO heritage alpine valley with colorful flowers."),
      ("Kedarkantha","Uttarakhand","Easy",6,"Popular winter summit trek with snow-covered trails."),
      ("Hampta Pass","Himachal Pradesh","Moderate",5,"Dramatic crossover from lush valleys to barren landscapes."),
      ("Triund","Himachal Pradesh","Easy",2,"Weekend trek with panoramic Dhauladhar views."),
      ("Brahmatal","Uttarakhand","Moderate",6,"Beautiful frozen lakes and Himalayan vistas."),
      ("Kashmir Great Lakes","Jammu & Kashmir","Hard",8,"One of India's most scenic multi-lake treks.")
    ]
    treks=[]
    today=date.today()
    for idx,t in enumerate(trek_data):
        name,loc,diff,dur,desc=t
        tr=Trek.query.filter_by(name=name).first()
        if not tr:
            start=today+timedelta(days=(idx+1)*10)
            tr=Trek(
                name=name,location=loc,difficulty=diff,duration=dur,
                description=desc,
                available_slots=20-idx,
                status="Open",
                start_date=start,
                end_date=start+timedelta(days=dur),
                assigned_staff_id=staff_users[idx%len(staff_users)].id
            )
            db.session.add(tr); db.session.commit()
        treks.append(tr)

    statuses=["Booked","Booked","Booked","Completed","Booked","Cancelled","Completed","Booked","Booked","Booked"]
    payments=["Paid","Pending","Paid","Paid","Pending","Refunded","Paid","Pending","Paid","Pending"]
    pairs=[(0,0),(0,1),(1,2),(1,3),(2,4),(2,5),(3,0),(4,1),(4,4),(5,2)]
    for i,(tu,tr) in enumerate(pairs):
        if not Booking.query.filter_by(user_id=trekkers[tu].id,trek_id=treks[tr].id).first():
            db.session.add(Booking(
                user_id=trekkers[tu].id,
                trek_id=treks[tr].id,
                status=statuses[i],
                payment_status=payments[i]
            ))
    db.session.commit()
    print("Database seeded successfully.")
