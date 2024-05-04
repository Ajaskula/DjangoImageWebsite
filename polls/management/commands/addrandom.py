from django.core.management.base import BaseCommand
from polls.models import SVGImage, Rectangle, Tag
import random
from django.core.management.base import BaseCommand
import string

class Command(BaseCommand):
    help = 'Adds a random SVGImage object with a rectangle to the database'

    def handle(self, *args, **options):
        image_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        width = random.randint(100, 500)
        height = random.randint(100, 500)
        viewbox = f"0 0 {width} {height}"
        version = '1.1'
        xmlns = 'http://www.w3.org/2000/svg'
        description = 'Randomly generated SVGImage'
        svg_image = SVGImage.objects.create(image_name=image_name, width=width, height=height, viewbox=viewbox, version=version, xmlns=xmlns, description=description)

        # Dodajemy losowy prostokąt
        rect_x = random.randint(0, width)
        rect_y = random.randint(0, height)
        rect_width = random.randint(0, width - rect_x)
        rect_height = random.randint(0, height - rect_y)
        rect_fill = random.choice(['red', 'green', 'blue', 'yellow', 'purple'])
        svg_image.add_rectangle(rect_x, rect_y, rect_width, rect_height, rect_fill)
        rect_x = random.randint(0, width)
        rect_y = random.randint(0, height)
        rect_width = random.randint(0, width - rect_x)
        rect_height = random.randint(0, height - rect_y)
        rect_fill = random.choice(['red', 'green', 'blue', 'yellow', 'purple'])
        svg_image.add_rectangle(rect_x, rect_y, rect_width, rect_height, rect_fill)

        self.stdout.write(self.style.SUCCESS('Successfully added random SVGImage object with a rectangle'))
