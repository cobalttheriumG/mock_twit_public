import re
import textwrap
from PIL import Image, ImageDraw, ImageFont


def write_last_seen_id(id, txt):
    with open(txt, 'w') as txt:
        txt.write(id)
    print('Write last seen id are done!')


def get_last_seen_id(txt):
    with open(txt, 'r') as txt:
        readfile = txt.read()
    return readfile


def mock_tweet(twt, type):
    splitted = twt.split(' ')
    fix_str = ' '.join(splitted)
    if type == 'pliisi':
        return khalesi_mock(fix_str)
    elif type == 'please':
        return spongebob_mock(fix_str)


def khalesi_mock(twt):
    vowels_pattern = r"[aiueoAIUEO]"
    result = re.sub(vowels_pattern, 'i', twt)
    img_file = 'khalesi_mock.jpg'
    draw_txt(result, img_file)
    return result


def spongebob_mock(twt):
    result = ''
    img_file = 'spongebob_mock.jpg'
    for x in range(len(twt)):
        if x % 2 == 0:
            result += twt[x].upper()
        else:
            result += twt[x].lower()
    draw_txt(result, img_file)
    return result


def draw_txt(txt, img_file):
    img = Image.open(f'./assets/{img_file}')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./assets/impact.ttf', size=30)
    img_height = img.size[1]
    wrapped_txt = textwrap.wrap(txt, width=50)
    print(len(txt))
    current_h, padding = img_height - 100, 20
    if len(txt) > 250:
        current_h = img_height - 200
    elif len(txt) > 200:
        current_h = img_height - 180
    elif len(txt) > 150:
        current_h = img_height - 140

    stroke_color = (0, 0, 0)

    for line in wrapped_txt:
        fixed_line = line.replace('’', ' ')
        txt_w, txt_h = draw.textsize(fixed_line)
        img_w = img.size[0]
        draw.text(((img_w / 2) - (txt_w), current_h), line,
                  font=font, stroke_width=1, stroke_fill=stroke_color)
        current_h += txt_h + padding

    img.save('upload.jpg')
    print('image saved!')
