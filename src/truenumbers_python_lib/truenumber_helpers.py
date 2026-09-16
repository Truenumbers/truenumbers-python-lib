import re

def get_truenumber_type(truenumber: dict) -> str:
    return truenumber.get("value").get("type")

def is_artifact_truenumber(truenumber: dict) -> bool:
    return get_truenumber_type(truenumber) == "artifact"

def is_numeric_truenumber(truenumber: dict) -> bool:
    return get_truenumber_type(truenumber) == "numeric"

def is_string_truenumber(truenumber: dict) -> bool:
    return get_truenumber_type(truenumber) == "string"

def is_date_truenumber(truenumber: dict) -> bool:
    return get_truenumber_type(truenumber) == "date"

def is_path_truenumber(truenumber: dict) -> bool:
    return get_truenumber_type(truenumber) == "srd"

def is_json_truenumber(truenumber: dict) -> bool:
    return get_truenumber_type(truenumber) == "json"


SRD_PARTITION_REGEXP = re.compile(r'(:|/)')


def split_path_parts(srd: str, include_srd_breaks: bool = False) -> list[str]:
    parts = SRD_PARTITION_REGEXP.split(srd)

    if include_srd_breaks:
        return parts

    return [part for part in parts if not SRD_PARTITION_REGEXP.fullmatch(part)]


def format_path_to_phrase(srd_to_transform: str) -> str:
    srd_partition_to_phrase = {
        ':': '',
        '/': 'of',
    }

    srd_term_parts = split_path_parts(srd_to_transform, True)
    srd_term_parts.reverse()

    result = [
        srd_partition_to_phrase.get(part, part)
        if SRD_PARTITION_REGEXP.fullmatch(part)
        else part
        for part in srd_term_parts
    ]

    return re.sub(r'\s{2,}', ' ', ' '.join(result)).strip()



def sanitize_path_phrase(path_phrase: str) -> str:
    return re.sub(r'[^a-zA-Z_\-0-9:\/]', '', path_phrase.strip()).strip()


def format_path_phrase_to_path(srd_to_format: str) -> str:

    def remove_filler_srd_terms(srd: str) -> str:
        replacements = [
            (r'(:|/)a:', ':'),
            (r'(:|/)a/', '/'),
            (r'(:|/)a$', ''),
            (r'(:|/)an/', '/'),
            (r'(:|/)an:', ':'),
            (r'(:|/)an$', ''),
            (r'(:|/)the$', ''),
            (r'(:|/)the/', '/'),
            (r'(:|/)the:', ':'),
        ]

        for pattern, replacement in replacements:
            srd = re.sub(pattern, replacement, srd)

        return srd

    def join_phrase_to_srd(phrase: str) -> str:
        return ':'.join(
            reversed([v for v in phrase.split(' ') if v])
        ).strip()

    def join_of_a_relationship_phrase(of_a_relationship_phrase: str) -> str:
        return ':'.join(
            map(join_phrase_to_srd, of_a_relationship_phrase.split(','))
        )

    transformed = (
        srd_to_format.strip()
        .replace(' of ', '@@')
        .replace(' in ', '@@')
        .replace(' at ', '@@')
        .replace(' for ', '@@')
    )

    transformed = re.split(r'@@', transformed, flags=re.IGNORECASE)

    transformed = [
        join_of_a_relationship_phrase(part)
        for part in transformed
    ]

    transformed.reverse()

    result = '/'.join(transformed)

    return sanitize_path_phrase(remove_filler_srd_terms(result))