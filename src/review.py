import hashlib
import re


def review(config):
    rules = config["rules"]
    changes = config["merge"]["changes"]

    comments = []

    for rule in rules:
        message = rule["message"]
        regex_path_list = rule["regexPath"]

        for change in changes:
            if not change["new_file"]:
                path = change["new_path"]

                for regex_path in regex_path_list:
                    if re.search(regex_path, path):
                        comments.append(__create_comment(message, path))
                        break

    return comments


def __create_comment(message, path):
    comment = {
        "id": __generate_md5(path),
        "comment": message,
        "position": {
            "path": path,
            "snipset": False
        }
    }

    return comment


def __generate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    return md5_hash.hexdigest()
