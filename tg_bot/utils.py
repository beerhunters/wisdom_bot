import re


async def escape_markdown(text: str) -> str:
    """Экранирует спецсимволы для MarkdownV2."""
    return re.sub(
        r"([*_`$begin:math:display$$end:math:display$()~>#+\-=|{}.!])", r"\\\1", text
    )
