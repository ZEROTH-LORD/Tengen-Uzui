from TengenUzui import ALLOW_EXCL

if ALLOW_EXCL:
    CMD_STARTERS = (
        "/",
        "!",
        ".",
        "-",
        "$",
        "*",
        "+",
    )
else:
    CMD_STARTERS = ("/",)
