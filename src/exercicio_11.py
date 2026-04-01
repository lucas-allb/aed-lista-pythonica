def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
  valor = guests.index(unavailable)
  guests[valor] = new_guest
  return guests
