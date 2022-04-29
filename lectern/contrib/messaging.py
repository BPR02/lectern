"""Plugin for handling markdown coming from messaging apps."""


__all__ = [
    "MessagingOptions",
    "messaging",
]


from typing import Literal

from beet import Context, Function, ListOption, configurable
from pydantic import BaseModel

from lectern import Document, LinkFragmentLoader


class MessagingOptions(BaseModel):
    links: Literal["enable", "ignore", "disable"] = "enable"
    input: ListOption[str] = ListOption()


def beet_default(ctx: Context):
    ctx.require(messaging)


@configurable(validator=MessagingOptions)
def messaging(ctx: Context, opts: MessagingOptions):
    """Plugin for handling markdown coming from messaging apps.

    The extractor cache is disabled to prevent remote files from being
    written to disk. If the message doesn't produce any files we try to
    form a default function by concatenating all code blocks.
    """
    document = ctx.inject(Document)
    document.loaders.append(LinkFragmentLoader(status=opts.links))
    document.markdown_extractor.cache = None

    for message in opts.input.entries():
        if not document.add(message):
            code_blocks = [
                token.content
                for token in document.markdown_extractor.parser.parse(message)  # type: ignore
                if token.type in ["fence", "code_block"]
            ]
            ctx.generate("{short_hash}", Function("\n".join(code_blocks)))
