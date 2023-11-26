class ShinyFilter(Filter):
    '''Этот фильтр подсвечивает все тусклые оттенки на картинке'''

    def apply_to_pixel(self, pixel: tuple, k) -> tuple:
        return tuple([min(round(i * k), 255) for i in pixel])

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        count = img.size[0] * img.size[1]
        summ = sum([sum([sum(img.getpixel((i, j))) for j in range(img.height)]) for i in range(img.width)])
        mid = summ // count
        for i in range(img.width):
            for j in range(img.height):
                pixel = img.getpixel((i, j))
                k = mid / sum(pixel) if sum(pixel) < mid and sum(pixel) != 0 else False
                if k:
                    new_pixel = self.apply_to_pixel(pixel, k)
                    img.putpixel((i, j), new_pixel)
        return img


class ChaoticFilter(Filter):
    def apply_to_image(self, img: Image.Image) -> Image.Image:
        r, g, b = randint(-100, 100), randint(-100, 100), randint(-100, 100)
        print(r, g, b)
        for i in range(img.width):
            for j in range(img.height):
                pixel = img.getpixel((i, j))
                new_pixel = tuple(pixel[i] + [r, g, b][i] if (0 <= i <= 255) else pixel[i] for i in range(3))
                img.putpixel((i, j), new_pixel)
        return img