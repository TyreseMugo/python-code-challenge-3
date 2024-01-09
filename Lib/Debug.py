from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Restaurant import Restaurant
from model.Review import Review
from model.Customer import Customer

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

def print_customer_reviews(session):
    print("\nCustomer list:")
    for review in session.query(Review).all():
        customer = review.customers
        print(f"Review by {customer.first_name} {customer.last_name}: {review.star_rating} stars")

def print_restaurant_reviews(session):
    print("\nRestaurant list:")
    for review in session.query(Review).all():
        restaurant = review.restaurants
        print(f"Review for {restaurant.name} - {review.star_rating} stars")

def retrieve_restaurant_and_reviews(session):
    restaurant = session.query(Restaurant).first()
    all_reviews = restaurant.display_reviews()
    return restaurant, all_reviews

def print_all_reviews_per_restaurant(restaurant, all_reviews):
    print("\nAll Reviews per restaurant:")
    for review in all_reviews:
        print(f"Review id: {review.id} Rating: {review.star_rating} Restaurant name: {restaurant.name}")

def print_customer_and_restaurant(session, restaurant):
    print("\nCustomer name and restaurant:")
    all_customers = restaurant.display_customers()
    for customer in all_customers:
        print(f"Review for {restaurant.name} by {customer.first_name} {customer.last_name}")

def print_customer_reviews_by_restaurant(session, customer):
    print("\nCustomer name, restaurant name, and restaurant star rating:")
    all_customers_reviews = customer.display_reviews()
    for review in all_customers_reviews:
        print(f"Review made by {customer.first_name} {customer.last_name} for restaurant id {review.restaurant_id} and gave a rating of {review.star_rating}")

def print_customer_and_reviewed_restaurants(session, customer):
    print("\nCustomer name, restaurant name, and restaurant price:")
    all_customers_reviewed_restaurants = customer.display_restaurants()
    for restaurant in all_customers_reviewed_restaurants:
        print(f"Review for {restaurant.name} by {customer.first_name} {customer.last_name} with a price of {restaurant.price}")

if __name__ == '__main__':
    engine = create_engine('sqlite:///Filedata.db')
    session = get_session(engine)

    print_customer_reviews(session)
    print_restaurant_reviews(session)

    restaurant, all_reviews = retrieve_restaurant_and_reviews(session)
    print_all_reviews_per_restaurant(restaurant, all_reviews)

    print_customer_and_restaurant(session, restaurant)

    customer = session.query(Customer).first()
    print_customer_reviews_by_restaurant(session, customer)
    print_customer_and_reviewed_restaurants(session, customer)