from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[list] = [[] for page in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(pages=(photos_count + 4 - 1) // 4)

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            for slot in range(0, 4):
                if len(self.photos[page]) != 4:
                    self.photos[page].append(label)
                    return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        result = ''
        for page in self.photos:
            result += f'-----------\n'
            for slot, label in enumerate(page, 1):
                if label:
                    if len(page) != slot:
                        result += '[] '
                    else:
                        result += '[]'
            result += '\n'
        result += '-----------'
        return result


# Test code:
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

