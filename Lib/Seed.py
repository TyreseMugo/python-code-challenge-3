from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from model.Restaurant import Restaurant
from model.Customer import Customer
from model.Review import Review
from model.Base import Base

def create_session():
    engine = create_engine('sqlite:///Filedata.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()

def clear_existing_data(session):
    session.query(Customer).delete()
    session.query(Review).delete()
    session.query(Restaurant).delete()

def seed_data(session):
    # Add your data seeding logic here
    fake = Faker()
    for _ in range(5):
        restaurant = Restaurant(name=fake.company(), price=fake.random_int(1, 100))
        customer = Customer(first_name=fake.first_name(), last_name=fake.last_name())
        review = Review(star_rating=fake.random_int(1, 5), restaurant=restaurant, customer=customer)
        session.add_all([restaurant, customer, review])

def display_restaurants(session):
    print("\nRestaurants:")
    for restaurant in session.query(Restaurant).all():
        print(f"ID: {restaurant.id}, Name: {restaurant.name}, Price: {restaurant.price}")

def display_customers(session):
    print("\nCustomers:")
    for customer in session.query(Customer).all():
        print(f"ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")

def display_reviews(session):
    print("\nReviews:")
    for review in session.query(Review).all():
        print(f"ID: {review.id}, Rating: {review.star_rating}, Restaurant: {review.restaurant.name}, Customer: {review.customer.first_name} {review.customer.last_name}")

if __name__ == '__main__':
    with create_session() as session:
        clear_existing_data(session)
        seed_data(session)

        # Display information about the generated data
        display_restaurants(session)
        display_customers(session)
        display_reviews(session)

    print("Finished")