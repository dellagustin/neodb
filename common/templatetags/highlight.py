from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from opencc import OpenCC
import re

cc = OpenCC("t2s")
register = template.Library()


@register.filter
@stringfilter
def highlight(text, search):
    otext = cc.convert(text.lower())
    l = len(text)
    if l != len(otext):
        return text  # in rare cases, the lowered&converted text has a different length
    rtext = ""
    words = list(set([w for w in cc.convert(search.strip().lower()).split(" ") if w]))
    words.sort(key=len, reverse=True)
    i = 0
    while i < l:
        m = None
        for w in words:
            if otext[i : i + len(w)] == w:
                m = f"<mark>{text[i:i+len(w)]}</mark>"
                i += len(w)
                break
        if not m:
            m = text[i]
            i += 1
        rtext += m
    return mark_safe(rtext)


@register.filter
@stringfilter
def strip_season(text):
    return re.sub(r"\s*第\s*\d+\s*季$", "", text)
