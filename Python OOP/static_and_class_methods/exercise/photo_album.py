from math import ceil


class PhotoAlbum:
    PAGES_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.PAGES_PER_PAGE))

    def add_photo(self, label: str):
        try:
            page_available = next(filter(lambda p: len(p) < 4, self.photos))
            idx = self.photos.index(page_available) + 1
        except StopIteration:
            return "No more free slots"
        page_available.append(label)
        return f"{label} photo added successfully on page {idx} slot {len(page_available)}"

    def display(self):
        sep = '-' * 11
        pages = f'\n{sep}\n'.join([('[] ' * len(p)).rstrip() for p in self.photos])
        return f'{sep}\n{pages}\n{sep}'
