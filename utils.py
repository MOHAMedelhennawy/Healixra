from models.doctor import Doctor

def search_doctors(name, location=None):
    name = name.title()
    first_name, last_name = name.split() if ' ' in name else (name, None)
    if name and location == None:
        if last_name:
            return Doctor.query.filter(
                Doctor.first_name.ilike(f'%{first_name}%'),
                Doctor.last_name.ilike(f'%{last_name}%')
            ).all()
        else:
            return Doctor.query.filter(
                Doctor.first_name.ilike(f'%{first_name}%')
            ).all()
    elif name and location:
        if last_name:
            matched_doctors = Doctor.query.filter(
                Doctor.location_id == location.id,
                Doctor.first_name.ilike(f'%{first_name}%'),
                Doctor.last_name.ilike(f'%{last_name}%')
                ).all()
        else:
            matched_doctors = Doctor.query.filter(
                Doctor.location_id == location.id,
                Doctor.first_name.ilike(f'%{first_name}%')
                ).all()
    else:
        return Doctor.query.all()
