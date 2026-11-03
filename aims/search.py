def search_by_title(cart, title):
    return [dvd for dvd in cart.items if title.strip().lower() in dvd.title.lower()]
