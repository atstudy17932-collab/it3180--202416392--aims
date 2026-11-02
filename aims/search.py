def search_by_category(cart, category):
    return [dvd for dvd in cart.items if category.lower() == dvd.category.lower()]


def search_by_title(cart, title):
    return [dvd for dvd in cart.items if title.lower() in dvd.title.lower()]
