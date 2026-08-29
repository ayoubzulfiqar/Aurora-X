#!/usr/bin/env python3
"""Generate the Aurora X IntelliJ/Android Studio editor color scheme (.icls) — pure AMOLED.

IntelliJ .icls format: an <scheme> root with <option name="..." value="..."/> for
global colors and <attributes> blocks for text styles. Colors are 6-digit RGB or
8-digit RGBA (no leading #). We base it on Darcula and override with the aurora palette.
"""
import os

A = {
    "ice": "86A5FF", "nebula": "C792EA", "cyan": "89DDFF", "green": "C3E88D",
    "ember": "F78C6C", "gold": "FFCB6B", "rose": "F07178", "magenta": "DD5074",
    "text": "C7D5FF", "muted": "576DAF", "comment": "546E7A", "white": "EEFFFF",
    "surface": "15182B", "surface2": "0C0E19", "line": "262E47", "black": "000000",
    "blue": "82AAFF", "red": "DD5074", "green2": "63EB90", "yellow": "FFCB6B",
}

# Global <colors> options (name -> value). Based on Darcula, recolored to aurora/AMOLED.
global_colors = {
    "CARET_COLOR": A["ice"],
    "CARET_ROW_COLOR": "0C0E19",
    "GUTTER_BACKGROUND": A["black"],
    "LINE_NUMBERS_COLOR": "3A4B6B",
    "LINE_NUMBERS_ON_CARET_ROW_COLOR": A["ice"],
    "SELECTED_TEARLINE_COLOR": A["ice"],
    "TEARLINE_COLOR": A["line"],
    "RIGHT_MARGIN_COLOR": A["line"],
    "INDENT_GUIDE": A["surface"],
    "INDENT_GUIDE_SELECTED": A["line"],
    "SELECTED_INDENT_GUIDE": A["line"],
    "TARGET_TEARLINE_COLOR": A["ice"],
    "VCS_LINESTATUS_ADDED": A["green2"],
    "VCS_LINESTATUS_MODIFIED": "C778DB",
    "ERROR_STRIPE_COLOR": A["magenta"],
    "WARNING_STRIPE_COLOR": A["yellow"],
    "READ_ACCESS_MARK_COLOR": A["nebula"],
    "WRITE_ACCESS_MARK_COLOR": A["green"],
    "ADDED_LINES_COLOR": "14331F",
    "REMOVED_LINES_COLOR": "33141C",
    "MODIFIED_LINES_COLOR": "2E1B33",
    "WHITESPACES_COLOR": A["surface"],
    "INJECTED_LANGUAGE_FRAGMENT": "1C2138",
    "FOLDED_TEXT_BORDER_COLOR": A["line"],
    "FOLDED_TEXT_FOREGROUND": A["muted"],
    "SOFT_WRAP_SIGN_COLOR": A["muted"],
    "SCROLLBAR_HOVER_THUMB_COLOR": A["muted"],
    "SCROLLBAR_THUMB_COLOR": A["line"],
    "SCROLLBAR_TRANSPARENT_THUMB_COLOR": A["line"],
    "SCROLLBAR_FREE_THUMB_COLOR": A["line"],
    "SCROLLBAR_FREE_HOVER_THUMB_COLOR": A["muted"],
}

def attr(name, fg=None, bg=None, italic=False, bold=False, effect=None, effectcolor=None):
    """Build an <attributes> block. effect: 'LINE_UNDER' / 'WAVE_UNDERSCORE' / 'BOLD' etc."""
    parts = [f'  <attributes name="{name}">']
    if fg:
        parts.append(f'    <option name="FOREGROUND" value="{fg}" />')
    if bg:
        parts.append(f'    <option name="BACKGROUND" value="{bg}" />')
    if effect:
        parts.append(f'    <option name="EFFECT_TYPE" value="{effect}" />')
    if effectcolor:
        parts.append(f'    <option name="EFFECT_COLOR" value="{effectcolor}" />')
    if italic:
        parts.append('    <option name="FONT_TYPE" value="2" />')   # ITALIC = 2
    elif bold:
        parts.append('    <option name="FONT_TYPE" value="1" />')   # BOLD = 1
    parts.append('  </attributes>')
    return "\n".join(parts)

attributes = []

# ---- Language Defaults (apply to all languages) ----
attributes.append(attr("DEFAULT_TEXT", fg=A["text"]))
attributes.append(attr("DEFAULT_KEYWORD", fg=A["nebula"], bold=True))
attributes.append(attr("DEFAULT_NUMBER", fg=A["ember"]))
attributes.append(attr("DEFAULT_STRING", fg=A["green"]))
attributes.append(attr("DEFAULT_STRING_ESCAPED_CHARACTER", fg=A["cyan"]))
attributes.append(attr("DEFAULT_VALID_STRING_ESCAPE", fg=A["cyan"]))
attributes.append(attr("DEFAULT_LINE_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("DEFAULT_BLOCK_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("DEFAULT_DOC_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("DEFAULT_DOC_MARKUP", fg=A["muted"]))
attributes.append(attr("DEFAULT_OPERATION_SIGN", fg=A["cyan"]))
attributes.append(attr("DEFAULT_PARENTHS", fg=A["cyan"]))
attributes.append(attr("DEFAULT_BRACKETS", fg=A["cyan"]))
attributes.append(attr("DEFAULT_BRACES", fg=A["cyan"]))
attributes.append(attr("DEFAULT_COMMA", fg=A["cyan"]))
attributes.append(attr("DEFAULT_DOT", fg=A["cyan"]))
attributes.append(attr("DEFAULT_SEMICOLON", fg=A["cyan"]))
attributes.append(attr("DEFAULT_IDENTIFIER", fg=A["text"]))
attributes.append(attr("DEFAULT_FUNCTION_DECLARATION", fg=A["blue"], bold=True))
attributes.append(attr("DEFAULT_FUNCTION_CALL", fg=A["blue"]))
attributes.append(attr("DEFAULT_METHOD_DECLARATION", fg=A["blue"], bold=True))
attributes.append(attr("DEFAULT_METHOD_CALL", fg=A["blue"]))
attributes.append(attr("DEFAULT_CLASS", fg=A["gold"]))
attributes.append(attr("DEFAULT_CLASS_NAME", fg=A["gold"]))
attributes.append(attr("DEFAULT_INTERFACE_NAME", fg=A["gold"]))
attributes.append(attr("DEFAULT_ENUM_NAME", fg=A["gold"]))
attributes.append(attr("DEFAULT_TYPE_PARAMETER_NAME", fg=A["gold"]))
attributes.append(attr("DEFAULT_INSTANCE_FIELD", fg=A["white"]))
attributes.append(attr("DEFAULT_INSTANCE_METHOD", fg=A["blue"]))
attributes.append(attr("DEFAULT_STATIC_FIELD", fg=A["white"]))
attributes.append(attr("DEFAULT_STATIC_METHOD", fg=A["blue"]))
attributes.append(attr("DEFAULT_PARAMETER", fg=A["white"]))
attributes.append(attr("DEFAULT_LABEL", fg=A["gold"]))
attributes.append(attr("DEFAULT_CONSTANT", fg=A["ember"]))
attributes.append(attr("DEFAULT_LOCAL_VARIABLE", fg=A["white"]))
attributes.append(attr("DEFAULT_LOCAL_VARIABLE_DECLARATION", fg=A["white"]))
attributes.append(attr("DEFAULT_GLOBAL_VARIABLE", fg=A["white"]))
attributes.append(attr("DEFAULT_PREDEFINED_SYMBOL", fg=A["nebula"]))
attributes.append(attr("DEFAULT_PROPERTY", fg=A["gold"]))
attributes.append(attr("DEFAULT_TAG", fg=A["rose"]))
attributes.append(attr("DEFAULT_TAG_NAME", fg=A["rose"]))
attributes.append(attr("DEFAULT_ATTRIBUTE", fg=A["nebula"]))
attributes.append(attr("DEFAULT_ATTRIBUTE_NAME", fg=A["nebula"]))
attributes.append(attr("DEFAULT_NAMESPACE", fg=A["gold"]))
attributes.append(attr("DEFAULT_ANNOTATION", fg=A["nebula"]))
attributes.append(attr("DEFAULT_METADATA", fg=A["nebula"]))
attributes.append(attr("DEFAULT_INVALID_STRING_ESCAPE", fg=A["magenta"]))
attributes.append(attr("DEFAULT_MARKUP_ENTITY", fg=A["rose"]))
attributes.append(attr("DEFAULT_MARKUP_TAG", fg=A["rose"]))
attributes.append(attr("DEFAULT_MARKUP_ATTRIBUTE", fg=A["nebula"]))
attributes.append(attr("DEFAULT_MARKUP_ATTRIBUTE_VALUE", fg=A["green"]))
attributes.append(attr("DEFAULT_ENTITY", fg=A["gold"]))

# ---- Errors / Warnings / Infos ----
attributes.append(attr("ERRORS_ATTRIBUTES", fg=A["magenta"], effect="WAVE_UNDERSCORE", effectcolor=A["magenta"]))
attributes.append(attr("WARNING_ATTRIBUTES", fg=A["yellow"], effect="WAVE_UNDERSCORE", effectcolor=A["yellow"]))
attributes.append(attr("TYPO_ATTRIBUTES", fg=A["muted"], effect="WAVE_UNDERSCORE", effectcolor=A["muted"]))
attributes.append(attr("HINT_ATTRIBUTES", fg=A["nebula"]))
attributes.append(attr("INFO_ATTRIBUTES", fg=A["blue"]))
attributes.append(attr("NOT_USED_ELEMENT_ATTRIBUTES", fg=A["muted"]))
attributes.append(attr("DUPLICATE_FROM_SERVER", fg=A["muted"]))
attributes.append(attr("HYPERLINK_ATTRIBUTES", fg=A["blue"], effect="LINE_UNDER", effectcolor=A["blue"]))
attributes.append(attr("FOLDED_TEXT_ATTRIBUTES", fg=A["muted"]))

# ---- Search / selection ----
attributes.append(attr("SEARCH_RESULT_ATTRIBUTES", fg=A["white"], bg="262E47"))
attributes.append(attr("SEARCH_RESULT_WRITE", fg=A["white"], bg="33405F"))
attributes.append(attr("WRITE_SEARCH_RESULT_ATTRIBUTES", fg=A["white"], bg="33405F"))
attributes.append(attr("TEXT_SEARCH_RESULT_ATTRIBUTES", fg=A["white"], bg="262E47"))
attributes.append(attr("IDENTIFIER_UNDER_CARET_ATTRIBUTES", fg=A["white"], bg="262E47"))
attributes.append(attr("IDENTIFIER_UNDER_CARET_WRITE_ATTRIBUTES", fg=A["white"], bg="33405F"))
attributes.append(attr("WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES", fg=A["white"], bg="33405F"))

# ---- Code / refs ----
attributes.append(attr("CLASS_NAME_ATTRIBUTES", fg=A["gold"]))
attributes.append(attr("INTERFACE_NAME_ATTRIBUTES", fg=A["gold"]))
attributes.append(attr("ENUM_NAME_ATTRIBUTES", fg=A["gold"]))
attributes.append(attr("CONSTANT_ATTRIBUTES", fg=A["ember"]))
attributes.append(attr("STATIC_FINAL_FIELD_ATTRIBUTES", fg=A["ember"]))
attributes.append(attr("STATIC_FIELD_ATTRIBUTES", fg=A["white"]))
attributes.append(attr("STATIC_METHOD_ATTRIBUTES", fg=A["blue"]))
attributes.append(attr("PARAMETER_ATTRIBUTES", fg=A["white"]))
attributes.append(attr("LOCAL_VARIABLE_ATTRIBUTES", fg=A["white"]))
attributes.append(attr("LOCAL_VARIABLE_DECLARATION_ATTRIBUTES", fg=A["white"]))
attributes.append(attr("INSTANCE_FIELD_ATTRIBUTES", fg=A["white"]))
attributes.append(attr("INSTANCE_METHOD_ATTRIBUTES", fg=A["blue"]))
attributes.append(attr("METHOD_CALL_ATTRIBUTES", fg=A["blue"]))
attributes.append(attr("FUNCTION_CALL_ATTRIBUTES", fg=A["blue"]))
attributes.append(attr("KEYWORD_ATTRIBUTES", fg=A["nebula"], bold=True))
attributes.append(attr("SEMICOLON_ATTRIBUTES", fg=A["cyan"]))
attributes.append(attr("DOT_ATTRIBUTES", fg=A["cyan"]))
attributes.append(attr("COMMA_ATTRIBUTES", fg=A["cyan"]))
attributes.append(attr("PARENTHS_ATTRIBUTES", fg=A["cyan"]))
attributes.append(attr("BRACES_ATTRIBUTES", fg=A["cyan"]))
attributes.append(attr("BRACKETS_ATTRIBUTES", fg=A["cyan"]))
attributes.append(attr("OPERATION_SIGN_ATTRIBUTES", fg=A["cyan"]))
attributes.append(attr("BAD_CHARACTER_ATTRIBUTES", fg=A["magenta"], effect="WAVE_UNDERSCORE", effectcolor=A["magenta"]))
attributes.append(attr("NUMBER_ATTRIBUTES", fg=A["ember"]))
attributes.append(attr("STRING_ATTRIBUTES", fg=A["green"]))
attributes.append(attr("LINE_COMMENT_ATTRIBUTES", fg=A["comment"], italic=True))
attributes.append(attr("BLOCK_COMMENT_ATTRIBUTES", fg=A["comment"], italic=True))
attributes.append(attr("DOC_COMMENT_ATTRIBUTES", fg=A["comment"], italic=True))
attributes.append(attr("DOC_COMMENT_TAG", fg=A["muted"]))
attributes.append(attr("DOC_COMMENT_MARKUP", fg=A["muted"]))

# ---- Python ----
attributes.append(attr("PY.KEYWORD", fg=A["nebula"], bold=True))
attributes.append(attr("PY.NUMBER", fg=A["ember"]))
attributes.append(attr("PY.STRING", fg=A["green"]))
attributes.append(attr("PY.COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("PY.FUNC_DEFINITION", fg=A["blue"], bold=True))
attributes.append(attr("PY.CLASS_DEFINITION", fg=A["gold"], bold=True))
attributes.append(attr("PY.DECORATOR", fg=A["nebula"], italic=True))
attributes.append(attr("PY.PREDEFINED_DEFINITION", fg=A["blue"]))
attributes.append(attr("PY.SELF", fg=A["rose"], italic=True))
attributes.append(attr("PY.PARAMETER", fg=A["white"]))
attributes.append(attr("PY.BUILTIN_NAME", fg=A["blue"]))
attributes.append(attr("PY.OPERATOR", fg=A["cyan"]))

# ---- Kotlin / Java ----
attributes.append(attr("KOTLIN_KEYWORD", fg=A["nebula"], bold=True))
attributes.append(attr("KOTLIN_FUNCTION", fg=A["blue"], bold=True))
attributes.append(attr("KOTLIN_CLASS", fg=A["gold"], bold=True))
attributes.append(attr("KOTLIN_PROPERTY", fg=A["gold"]))
attributes.append(attr("KOTLIN_ANNOTATION", fg=A["nebula"]))
attributes.append(attr("KOTLIN_STRING", fg=A["green"]))
attributes.append(attr("KOTLIN_NUMBER", fg=A["ember"]))
attributes.append(attr("KOTLIN_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("JAVA_KEYWORD", fg=A["nebula"], bold=True))
attributes.append(attr("JAVA_STRING", fg=A["green"]))
attributes.append(attr("JAVA_NUMBER", fg=A["ember"]))
attributes.append(attr("JAVA_LINE_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("JAVA_BLOCK_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("JAVA_DOC_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("JAVA_CLASS", fg=A["gold"]))
attributes.append(attr("JAVA_METHOD", fg=A["blue"]))
attributes.append(attr("JAVA_ANNOTATION", fg=A["nebula"]))
attributes.append(attr("JAVA_STATIC_FIELD", fg=A["white"]))
attributes.append(attr("JAVA_PARAMETER", fg=A["white"]))
attributes.append(attr("JAVA_LOCAL_VARIABLE", fg=A["white"]))

# ---- JS / TS ----
attributes.append(attr("JS.KEYWORD", fg=A["nebula"], bold=True))
attributes.append(attr("JS.STRING", fg=A["green"]))
attributes.append(attr("JS.NUMBER", fg=A["ember"]))
attributes.append(attr("JS.FUNCTION", fg=A["blue"], bold=True))
attributes.append(attr("JS.CLASS_NAME", fg=A["gold"]))
attributes.append(attr("JS.LOCAL_VARIABLE", fg=A["white"]))
attributes.append(attr("JS.PARAMETER", fg=A["white"]))
attributes.append(attr("JS.REGEXP", fg=A["cyan"]))
attributes.append(attr("JS.COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("TS.KEYWORD", fg=A["nebula"], bold=True))
attributes.append(attr("TS.STRING", fg=A["green"]))
attributes.append(attr("TS.NUMBER", fg=A["ember"]))
attributes.append(attr("TS.FUNCTION", fg=A["blue"], bold=True))
attributes.append(attr("TS.CLASS", fg=A["gold"]))
attributes.append(attr("TS.INTERFACE", fg=A["gold"]))
attributes.append(attr("TS.TYPE", fg=A["gold"]))
attributes.append(attr("TS.ENUM", fg=A["gold"]))
attributes.append(attr("TS.PARAMETER", fg=A["white"]))
attributes.append(attr("TS.COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("TS.REGEXP", fg=A["cyan"]))

# ---- SQL ----
attributes.append(attr("SQL.KEYWORD", fg=A["nebula"], bold=True))
attributes.append(attr("SQL.FUNCTION", fg=A["nebula"]))
attributes.append(attr("SQL.TABLE", fg=A["gold"]))
attributes.append(attr("SQL.COLUMN", fg=A["gold"]))
attributes.append(attr("SQL.STRING", fg=A["green"]))
attributes.append(attr("SQL.NUMBER", fg=A["ember"]))
attributes.append(attr("SQL.COMMENT", fg=A["comment"], italic=True))

# ---- Shell ----
attributes.append(attr("SHELL_KEYWORD", fg=A["nebula"], bold=True))
attributes.append(attr("SHELL_FUNCTION", fg=A["blue"], bold=True))
attributes.append(attr("SHELL_VARIABLE", fg=A["white"]))
attributes.append(attr("SHELL_STRING", fg=A["green"]))
attributes.append(attr("SHELL_NUMBER", fg=A["ember"]))
attributes.append(attr("SHELL_COMMENT", fg=A["comment"], italic=True))

# ---- YAML / TOML / JSON ----
attributes.append(attr("YAML_KEY", fg=A["gold"]))
attributes.append(attr("YAML_SCALAR_KEY", fg=A["gold"]))
attributes.append(attr("YAML_SCALAR_VALUE", fg=A["white"]))
attributes.append(attr("YAML_STRING", fg=A["white"]))
attributes.append(attr("YAML_NUMBER", fg=A["ember"]))
attributes.append(attr("YAML_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("TOML_KEY", fg=A["gold"]))
attributes.append(attr("TOML_SEPARATOR", fg=A["cyan"]))
attributes.append(attr("TOML_STRING", fg=A["white"]))
attributes.append(attr("TOML_NUMBER", fg=A["ember"]))
attributes.append(attr("TOML_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("JSON_PROPERTY_KEY", fg=A["nebula"]))
attributes.append(attr("JSON_STRING", fg=A["green"]))
attributes.append(attr("JSON_NUMBER", fg=A["ember"]))
attributes.append(attr("JSON_KEYWORD", fg=A["cyan"]))
attributes.append(attr("JSON_BRACES", fg=A["cyan"]))
attributes.append(attr("JSON_COMMA", fg=A["cyan"]))
attributes.append(attr("JSON_COLON", fg=A["cyan"]))
attributes.append(attr("JSON_ERROR_KEY", fg=A["magenta"]))

# ---- HTML / CSS ----
attributes.append(attr("HTML_TAG", fg=A["rose"]))
attributes.append(attr("HTML_TAG_NAME", fg=A["rose"]))
attributes.append(attr("HTML_ATTRIBUTE_NAME", fg=A["nebula"]))
attributes.append(attr("HTML_ATTRIBUTE_VALUE", fg=A["green"]))
attributes.append(attr("HTML_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("CSS_PROPERTY_NAME", fg=A["blue"]))
attributes.append(attr("CSS_PROPERTY_VALUE", fg=A["ember"]))
attributes.append(attr("CSS_CLASS", fg=A["gold"]))
attributes.append(attr("CSS_ID", fg=A["blue"]))
attributes.append(attr("CSS_FUNCTION", fg=A["blue"]))
attributes.append(attr("CSS_TAG_NAME", fg=A["rose"]))
attributes.append(attr("CSS_COMMENT", fg=A["comment"], italic=True))
attributes.append(attr("CSS_COLOR", fg=A["white"]))

# ---- XML ----
attributes.append(attr("XML_TAG", fg=A["rose"]))
attributes.append(attr("XML_TAG_NAME", fg=A["rose"]))
attributes.append(attr("XML_ATTRIBUTE_NAME", fg=A["nebula"]))
attributes.append(attr("XML_ATTRIBUTE_VALUE", fg=A["green"]))
attributes.append(attr("XML_COMMENT", fg=A["comment"], italic=True))

# ---- Markdown ----
attributes.append(attr("MARKDOWN_HEADING", fg=A["green"], bold=True))
attributes.append(attr("MARKDOWN_BOLD", fg=A["rose"], bold=True))
attributes.append(attr("MARKDOWN_ITALIC", fg=A["rose"], italic=True))
attributes.append(attr("MARKDOWN_LINK", fg=A["blue"], effect="LINE_UNDER", effectcolor=A["blue"]))
attributes.append(attr("MARKDOWN_URL", fg=A["blue"], effect="LINE_UNDER", effectcolor=A["blue"]))
attributes.append(attr("MARKDOWN_QUOTE", fg=A["muted"], italic=True))
attributes.append(attr("MARKDOWN_LIST", fg=A["cyan"]))
attributes.append(attr("MARKDOWN_CODE", fg=A["nebula"]))
attributes.append(attr("MARKDOWN_INLINE_CODE", fg=A["nebula"]))

# ---- Diff / VCS ----
attributes.append(attr("DIFF_ADDITION", fg=A["green2"], bg="15331F"))
attributes.append(attr("DIFF_DELETION", fg=A["magenta"], bg="33141C"))
attributes.append(attr("DIFF_MODIFIED", fg=A["nebula"], bg="2E1B33"))
attributes.append(attr("ADDED_LINES", fg=A["green2"], bg="14331F"))
attributes.append(attr("REMOVED_LINES", fg=A["magenta"], bg="33141C"))
attributes.append(attr("MODIFIED_LINES", fg=A["nebula"], bg="2E1B33"))

# ---- Console ----
attributes.append(attr("CONSOLE_NORMAL_OUTPUT", fg=A["text"]))
attributes.append(attr("CONSOLE_ERROR_OUTPUT", fg=A["magenta"]))
attributes.append(attr("CONSOLE_USER_INPUT", fg=A["blue"]))
attributes.append(attr("CONSOLE_WARNING_OUTPUT", fg=A["yellow"]))
attributes.append(attr("CONSOLE_SYSTEM_OUTPUT", fg=A["muted"]))

# ---- Misc editor ----
attributes.append(attr("MATCHED_BRACE_ATTRIBUTES", fg=A["white"], bg=A["line"]))
attributes.append(attr("UNMATCHED_BRACE_ATTRIBUTES", fg=A["magenta"]))
attributes.append(attr("TODO_ATTRIBUTES", fg=A["gold"], bold=True))
attributes.append(attr("FIXME_ATTRIBUTES", fg=A["magenta"], bold=True))
attributes.append(attr("INLINE_PARAMETER_HINT", fg=A["muted"], bg="15182B"))
attributes.append(attr("INLINE_PARAMETER_HINT_HIGHLIGHTED", fg=A["muted"], bg="1C2138"))
attributes.append(attr("INLINE_REFACTORING_SETTINGS", fg=A["muted"]))
attributes.append(attr("TEMPLATE_VARIABLE_ATTRIBUTES", fg=A["nebula"], bg="1C2138"))
attributes.append(attr("LIVE_TEMPLATE_ATTRIBUTES", fg=A["nebula"], bg="1C2138"))
attributes.append(attr("POSTFIX_TEMPLATE", fg=A["nebula"]))
attributes.append(attr("SMART_TAG", fg=A["muted"]))
attributes.append(attr("CODE_VISION_USAGES", fg=A["muted"]))
attributes.append(attr("SECONDARY_LANGUAGE_TOKEN", fg=A["muted"]))
attributes.append(attr("GENERIC_SERVER_ERROR_OR_WARNING", fg=A["yellow"]))
attributes.append(attr("MERGE_CONFLICT", fg=A["gold"]))
attributes.append(attr("DUPLICATE_FROM_SERVER", fg=A["muted"]))
attributes.append(attr("NULLABILITY_PROBLEM", fg=A["yellow"]))
attributes.append(attr("WEAK_WARNING_ATTRIBUTES", fg=A["yellow"]))

color_opts = "\n".join(f'    <option name="{k}" value="{v}" />' for k, v in global_colors.items())

xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE scheme SYSTEM "https://www.jetbrains.com/DTD/2023.1/color-scheme.dtd">
<scheme name="Aurora X" version="142" parent_scheme="Darcula">
  <colors>
{color_opts}
  </colors>
{os.linesep.join(attributes)}
</scheme>
"""

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Aurora X.icls")
with open(out, "w", encoding="utf-8") as f:
    f.write(xml)
print("WROTE", out, "global colors:", len(global_colors), "attribute blocks:", len(attributes))
