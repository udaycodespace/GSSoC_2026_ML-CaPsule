import pathlib
import re


ROOT_PATH = pathlib.Path(__file__).parent.resolve()


EXCLUDED_FILES = {
    ".github",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING_GUIDELINES.md",
    "build_readme.py",
    "requirements.txt",
    "README.md",
    "download statistics.jpg",
    "img",
    "ml img.jpg",
    ".git",
    "__pycache__",
}


def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} start \-\->.*<!\-\- {} end \-\->".format(marker, marker),
        re.DOTALL,
    )

    if not inline:
        chunk = "\n{}\n".format(chunk)

    chunk = "<!-- {} start -->{}<!-- {} end -->".format(
        marker,
        chunk,
        marker,
    )

    return r.sub(chunk, content)


def extract_file_names():
    temp = []

    for item in ROOT_PATH.iterdir():

        if item.name in EXCLUDED_FILES:
            continue

        temp.append({
            "fname": item.name,
            "furl": item.name
        })

    return sorted(temp, key=lambda x: x["fname"].lower())


if __name__ == "__main__":

    readme = ROOT_PATH / "README.md"

    readme_contents = readme.read_text(encoding="utf-8")

    file_names = extract_file_names()

    file_md = "\n".join(
        ["| [{fname}]({furl}) |".format(**i) for i in file_names]
    )

    updated_content = replace_chunk(
        readme_contents,
        "Projects",
        "| Content List |\n| --------------- |\n" + file_md
    )

    readme.write_text(updated_content, encoding="utf-8")

    print("README.md updated successfully.")