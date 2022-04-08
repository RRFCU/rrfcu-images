"""
"""

from base64 import b64encode

RESOLUTIONS = (
    '16',
    '24',
    '32',
    '64',
    '128',
    '256',
    '512',
)

RESOLUTION = RESOLUTIONS[0]


if __name__ == '__main__':
    for _type in ('gold', 'silver', 'bronze'):
        with open(f'./{_type}/{RESOLUTION}px.png', 'rb') as file:
            encoded = b64encode(file.read())

        with open(f'./{_type}_encoded.txt', 'w') as file:
            file.truncate()
            file.write(str(encoded))
