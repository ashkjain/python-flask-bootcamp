from app import db, Puppy, app

with app.app_context():
    # This is Creating
    my_puppy = Puppy('Rufus',5)
    db.session.add(my_puppy)
    db.session.commit()

    # This is Reading
    all_puppies = Puppy.query.all() # Will return all the puppy objects in the table.
    print(all_puppies)

    # Select by ID
    puppy_one = Puppy.query.get(1)
    print(puppy_one)

    # Filters
    puppy_frankie = Puppy.query.filter_by(name='Frankie')
    print(puppy_frankie.all()) # Prints the list

    # This is updating
    first_puppy = Puppy.query.get(1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    # This is deleting
    second_pup = Puppy.query.get(2)
    db.session.delete(second_pup)
    db.session.commit()

    all_puppies = Puppy.query.all()
    print(all_puppies)