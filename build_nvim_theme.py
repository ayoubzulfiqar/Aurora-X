#!/usr/bin/env python3
"""Generate the Aurora X Neovim colorscheme (pure-AMOLED) as a Lua plugin.

Structure (standard Neovim plugin layout):
  colors/aurora-x.lua        -> runtime entry point (:colorscheme aurora-x)
  lua/aurora-x/palette.lua   -> palette
  lua/aurora-x/groups.lua    -> highlight groups (editor, treesitter, lsp, plugins)
  lua/aurora-x/init.lua      -> M.setup(opts)/M.load()

All colors are pure-AMOLED black + aurora accents, matching the other ports.
"""
import os

C = {
    "none":      "NONE",
    "black":     "#000000",
    "bg":        "#000000",
    "bg_alt":    "#0C0E19",
    "bg_ui":     "#15182B",
    "bg_ui2":    "#1C2138",
    "fg":        "#C7D5FF",
    "fg_dim":    "#9AA8D6",
    "muted":     "#576DAF",
    "comment":   "#546E7A",
    "ice":       "#86A5FF",
    "nebula":    "#C792EA",
    "cyan":      "#89DDFF",
    "green":     "#C3E88D",
    "ember":     "#F78C6C",
    "gold":      "#FFCB6B",
    "rose":      "#F07178",
    "magenta":   "#DD5074",
    "red":       "#DD5074",
    "green2":    "#63EB90",
    "blue":      "#82AAFF",
    "white":     "#EEFFFF",
    "yellow":    "#FFCB6B",
    "line":      "#262E47",
    "sel":       "#262E47",
    "line_nr":   "#3A4B6B",
    "border":    "#15182B",
}

# ---- editor (base) groups ----
editor = {
    "Normal":            {"fg": C["fg"], "bg": C["bg"]},
    "NormalFloat":       {"fg": C["fg"], "bg": C["bg_ui"]},
    "NormalNC":          {"fg": C["fg_dim"], "bg": C["bg"]},
    "SignColumn":        {"fg": C["muted"], "bg": C["bg"]},
    "SignColumnNC":      {"fg": C["muted"], "bg": C["bg"]},
    "Cursor":            {"fg": C["bg"], "bg": C["ice"]},
    "CursorLine":        {"bg": C["bg_alt"]},
    "CursorLineNr":      {"fg": C["ice"], "bg": C["bg_alt"]},
    "CursorColumn":      {"bg": C["bg_alt"]},
    "ColorColumn":       {"bg": C["bg_alt"]},
    "LineNr":            {"fg": C["line_nr"], "bg": C["bg"]},
    "VertSplit":         {"fg": C["border"], "bg": C["bg"]},
    "WinSeparator":      {"fg": C["border"], "bg": C["bg"]},
    "Folded":            {"fg": C["muted"], "bg": C["bg_alt"]},
    "FoldColumn":        {"fg": C["muted"], "bg": C["bg"]},
    "IncSearch":         {"fg": C["bg"], "bg": C["ice"]},
    "Search":            {"fg": C["bg"], "bg": C["muted"]},
    "CurSearch":         {"fg": C["bg"], "bg": C["ice"]},
    "Visual":            {"bg": C["sel"]},
    "VisualNOS":         {"bg": C["sel"]},
    "VisualNC":          {"bg": C["sel"]},
    "Substitute":        {"fg": C["bg"], "bg": C["nebula"]},
    "MatchParen":        {"fg": C["white"], "bg": C["line"], "bold": True},
    "Conceal":           {"fg": C["muted"], "bg": C["bg"]},
    "Whitespace":        {"fg": C["border"]},
    "NonText":           {"fg": C["border"]},
    "SpecialKey":        {"fg": C["muted"]},
    "EndOfBuffer":       {"fg": C["bg"]},
    "Directory":         {"fg": C["blue"]},
    "Title":             {"fg": C["green"], "bold": True},
    "Question":          {"fg": C["green"]},
    "MoreMsg":           {"fg": C["green"]},
    "ModeMsg":           {"fg": C["ice"]},
    "ErrorMsg":          {"fg": C["red"], "bold": True},
    "WarningMsg":        {"fg": C["yellow"], "bold": True},
    "MsgArea":           {"fg": C["fg_dim"]},
    "MsgSeparator":      {"fg": C["border"]},
    "WildMenu":          {"fg": C["ice"], "bg": C["bg_ui"]},
    "StatusLine":        {"fg": C["ice"], "bg": C["bg"], "bold": True},
    "StatusLineNC":      {"fg": C["muted"], "bg": C["bg"]},
    "StatusLineTerm":    {"fg": C["ice"], "bg": C["bg"]},
    "StatusLineTermNC":  {"fg": C["muted"], "bg": C["bg"]},
    "TabLine":           {"fg": C["muted"], "bg": C["bg"]},
    "TabLineFill":       {"fg": C["muted"], "bg": C["bg"]},
    "TabLineSel":        {"fg": C["white"], "bg": C["bg_alt"], "bold": True},
    "Pmenu":             {"fg": C["fg"], "bg": C["bg_ui"]},
    "PmenuSel":          {"fg": C["ice"], "bg": C["sel"]},
    "PmenuSelBold":      {"bold": True},
    "PmenuSbar":         {"bg": C["bg_ui2"]},
    "PmenuThumb":        {"bg": C["muted"]},
    "QuickFixLine":      {"fg": C["ice"], "bg": C["sel"]},
    "SpellBad":          {"undercurl": True, "sp": C["red"]},
    "SpellCap":          {"undercurl": True, "sp": C["yellow"]},
    "SpellRare":         {"undercurl": True, "sp": C["nebula"]},
    "SpellLocal":        {"undercurl": True, "sp": C["cyan"]},
    "Terminal":          {"fg": C["fg"], "bg": C["bg"]},
    "TerminalCursor":    {"fg": C["bg"], "bg": C["ice"]},
    "TermCursor":        {"fg": C["bg"], "bg": C["ice"]},
    "TermCursorNC":      {"fg": C["bg"], "bg": C["ice"]},
    "ToolbarLine":       {"fg": C["fg"], "bg": C["bg_ui"]},
    "ToolbarButton":     {"fg": C["ice"], "bg": C["bg_ui2"]},
    "FloatBorder":       {"fg": C["ice"], "bg": C["bg_ui"]},
    "FloatTitle":        {"fg": C["ice"], "bg": C["bg_ui"]},
    "WinBar":            {"fg": C["fg"], "bg": C["bg"]},
    "WinBarNC":          {"fg": C["muted"], "bg": C["bg"]},
    "Menubar":           {"fg": C["fg"], "bg": C["bg_ui"]},
    "Scrollbar":         {"fg": C["muted"], "bg": C["bg"]},
    "Substitute":        {"fg": C["bg"], "bg": C["nebula"]},
}

# ---- syntax (legacy) groups ----
syntax = {
    "Comment":        {"fg": C["comment"], "italic": True},
    "Constant":       {"fg": C["ember"]},
    "String":         {"fg": C["green"]},
    "Character":      {"fg": C["green"]},
    "Number":         {"fg": C["ember"]},
    "Boolean":        {"fg": C["ember"]},
    "Float":          {"fg": C["ember"]},
    "Identifier":     {"fg": C["white"]},
    "Function":       {"fg": C["blue"], "bold": True},
    "Statement":      {"fg": C["nebula"], "bold": True},
    "Conditional":    {"fg": C["nebula"]},
    "Repeat":         {"fg": C["nebula"]},
    "Label":          {"fg": C["gold"]},
    "Operator":       {"fg": C["cyan"]},
    "Keyword":        {"fg": C["nebula"], "bold": True},
    "Exception":      {"fg": C["nebula"]},
    "PreProc":        {"fg": C["nebula"]},
    "Include":        {"fg": C["nebula"]},
    "Define":         {"fg": C["nebula"]},
    "Macro":          {"fg": C["nebula"]},
    "PreCondit":      {"fg": C["nebula"]},
    "Type":           {"fg": C["gold"]},
    "StorageClass":   {"fg": C["nebula"]},
    "Structure":      {"fg": C["gold"]},
    "Typedef":        {"fg": C["gold"]},
    "Special":        {"fg": C["cyan"]},
    "SpecialChar":    {"fg": C["cyan"]},
    "Tag":            {"fg": C["rose"]},
    "Delimiter":      {"fg": C["cyan"]},
    "SpecialComment": {"fg": C["comment"], "italic": True},
    "Debug":          {"fg": C["muted"]},
    "Underlined":     {"fg": C["blue"], "underline": True},
    "Ignore":         {"fg": C["muted"]},
    "Error":          {"fg": C["red"], "bold": True},
    "Todo":           {"fg": C["gold"], "bold": True},
    "htmlTag":        {"fg": C["rose"]},
    "htmlEndTag":     {"fg": C["rose"]},
    "htmlTagName":    {"fg": C["rose"]},
    "htmlArg":        {"fg": C["nebula"]},
    "xmlTag":         {"fg": C["rose"]},
    "xmlEndTag":      {"fg": C["rose"]},
    "xmlTagName":     {"fg": C["rose"]},
    "cssPropertyName": {"fg": C["blue"]},
    "cssValueNumber": {"fg": C["ember"]},
}

# ---- treesitter / semantic (@) groups ----
treesitter = {
    "@comment":          {"fg": C["comment"], "italic": True},
    "@comment.documentation": {"fg": C["comment"], "italic": True},
    "@none":             {},
    "@text":             {"fg": C["fg"]},
    "@text.strong":      {"fg": C["rose"], "bold": True},
    "@text.emphasis":    {"fg": C["rose"], "italic": True},
    "@text.underline":   {"fg": C["ember"], "underline": True},
    "@text.strike":      {"fg": C["muted"], "strikethrough": True},
    "@text.title":       {"fg": C["green"], "bold": True},
    "@text.title.1":     {"fg": C["green"], "bold": True},
    "@text.title.2":     {"fg": C["blue"], "bold": True},
    "@text.title.3":     {"fg": C["nebula"], "bold": True},
    "@text.title.4":     {"fg": C["green"], "bold": True},
    "@text.title.5":     {"fg": C["blue"], "bold": True},
    "@text.title.6":     {"fg": C["nebula"], "bold": True},
    "@text.literal":     {"fg": C["nebula"]},
    "@text.uri":         {"fg": C["blue"], "underline": True},
    "@text.link":        {"fg": C["blue"], "underline": True},
    "@text.reference":   {"fg": C["blue"]},
    "@text.note":        {"fg": C["cyan"]},
    "@text.warning":     {"fg": C["yellow"]},
    "@text.danger":      {"fg": C["red"]},
    "@text.diff.add":    {"fg": C["green2"]},
    "@text.diff.delete": {"fg": C["red"]},
    "@text.environment": {"fg": C["nebula"]},
    "@text.environment.name": {"fg": C["gold"]},
    "@text.math":        {"fg": C["nebula"]},
    "@text.quote":       {"fg": C["muted"], "italic": True},
    "@text.punctuation": {"fg": C["cyan"]},
    "@text.todo":        {"fg": C["gold"], "bold": True},
    "@keyword":          {"fg": C["nebula"], "bold": True},
    "@keyword.coroutine": {"fg": C["nebula"]},
    "@keyword.function": {"fg": C["nebula"], "bold": True},
    "@keyword.operator": {"fg": C["cyan"]},
    "@keyword.import":   {"fg": C["nebula"]},
    "@keyword.storage":  {"fg": C["nebula"]},
    "@keyword.repeat":    {"fg": C["nebula"]},
    "@keyword.return":    {"fg": C["nebula"]},
    "@keyword.conditional": {"fg": C["nebula"]},
    "@keyword.debug":     {"fg": C["nebula"]},
    "@keyword.exception": {"fg": C["nebula"]},
    "@keyword.directive": {"fg": C["nebula"]},
    "@keyword.directive.define": {"fg": C["nebula"]},
    "@constant":         {"fg": C["ember"]},
    "@constant.builtin": {"fg": C["ember"]},
    "@constant.macro":   {"fg": C["nebula"]},
    "@constant.numeric": {"fg": C["ember"]},
    "@constant.volatile": {"fg": C["ember"]},
    "@string":           {"fg": C["green"]},
    "@string.documentation": {"fg": C["green"]},
    "@string.escape":    {"fg": C["cyan"]},
    "@string.special":   {"fg": C["cyan"]},
    "@string.regexp":    {"fg": C["cyan"]},
    "@character":        {"fg": C["green"]},
    "@character.special": {"fg": C["cyan"]},
    "@boolean":          {"fg": C["ember"]},
    "@number":           {"fg": C["ember"]},
    "@number.float":     {"fg": C["ember"]},
    "@type":             {"fg": C["gold"]},
    "@type.builtin":     {"fg": C["gold"]},
    "@type.definition":  {"fg": C["gold"]},
    "@type.qualifier":   {"fg": C["nebula"]},
    "@type.annotation":  {"fg": C["nebula"]},
    "@attribute":        {"fg": C["nebula"]},
    "@attribute.builtin": {"fg": C["nebula"]},
    "@property":         {"fg": C["gold"]},
    "@field":            {"fg": C["white"]},
    "@variable":         {"fg": C["white"]},
    "@variable.builtin": {"fg": C["blue"]},
    "@variable.parameter": {"fg": C["white"]},
    "@variable.parameter.builtin": {"fg": C["blue"]},
    "@variable.member":  {"fg": C["white"]},
    "@variable.static":  {"fg": C["white"]},
    "@variable.global":  {"fg": C["white"]},
    "@parameter":        {"fg": C["white"]},
    "@namespace":        {"fg": C["gold"]},
    "@module":           {"fg": C["gold"]},
    "@label":            {"fg": C["gold"]},
    "@operator":         {"fg": C["cyan"]},
    "@punctuation":      {"fg": C["cyan"]},
    "@punctuation.delimiter": {"fg": C["cyan"]},
    "@punctuation.bracket": {"fg": C["cyan"]},
    "@punctuation.special": {"fg": C["cyan"]},
    "@function":         {"fg": C["blue"], "bold": True},
    "@function.builtin": {"fg": C["blue"], "bold": True},
    "@function.call":    {"fg": C["blue"]},
    "@function.macro":   {"fg": C["nebula"]},
    "@function.method":  {"fg": C["blue"], "bold": True},
    "@method":           {"fg": C["blue"], "bold": True},
    "@method.call":      {"fg": C["blue"]},
    "@constructor":      {"fg": C["blue"]},
    "@tag":              {"fg": C["rose"]},
    "@tag.attribute":    {"fg": C["nebula"]},
    "@tag.delimiter":    {"fg": C["cyan"]},
    "@tag.builtin":      {"fg": C["rose"]},
    "@class":            {"fg": C["gold"], "bold": True},
    "@struct":           {"fg": C["gold"], "bold": True},
    "@enum":             {"fg": C["gold"], "bold": True},
    "@interface":        {"fg": C["gold"], "bold": True},
    "@enumMember":       {"fg": C["gold"]},
    "@event":            {"fg": C["nebula"]},
    "@modifier":         {"fg": C["nebula"]},
    "@storageclass":     {"fg": C["nebula"]},
    "@structure":        {"fg": C["gold"]},
    "@include":          {"fg": C["nebula"]},
    "@repeat":           {"fg": C["nebula"]},
    "@conditional":      {"fg": C["nebula"]},
    "@exception":        {"fg": C["nebula"]},
    "@debug":            {"fg": C["muted"]},
    "@macro":            {"fg": C["nebula"]},
    "@error":            {"fg": C["red"], "undercurl": True, "sp": C["red"]},
    "@warning":          {"fg": C["yellow"]},
    "@info":             {"fg": C["cyan"]},
    "@hint":             {"fg": C["nebula"]},
    "@deprecated":       {"fg": C["muted"], "strikethrough": True},
    "@diff.plus":        {"fg": C["green2"]},
    "@diff.minus":       {"fg": C["red"]},
    "@diff.delta":       {"fg": C["nebula"]},
}

# ---- LSP semantic tokens + diagnostics ----
lsp = {
    "@lsp.type.class":          {"fg": C["gold"], "bold": True},
    "@lsp.type.enum":           {"fg": C["gold"], "bold": True},
    "@lsp.type.interface":      {"fg": C["gold"], "bold": True},
    "@lsp.type.struct":         {"fg": C["gold"], "bold": True},
    "@lsp.type.type":           {"fg": C["gold"]},
    "@lsp.type.typeParameter":  {"fg": C["gold"]},
    "@lsp.type.namespace":      {"fg": C["gold"]},
    "@lsp.type.module":         {"fg": C["gold"]},
    "@lsp.type.function":       {"fg": C["blue"], "bold": True},
    "@lsp.type.method":         {"fg": C["blue"], "bold": True},
    "@lsp.type.macro":         {"fg": C["nebula"]},
    "@lsp.type.decorator":      {"fg": C["nebula"]},
    "@lsp.type.enumMember":     {"fg": C["gold"]},
    "@lsp.type.property":       {"fg": C["gold"]},
    "@lsp.type.field":         {"fg": C["white"]},
    "@lsp.type.variable":       {"fg": C["white"]},
    "@lsp.type.parameter":      {"fg": C["white"]},
    "@lsp.type.constant":       {"fg": C["ember"]},
    "@lsp.type.number":         {"fg": C["ember"]},
    "@lsp.type.string":         {"fg": C["green"]},
    "@lsp.type.boolean":        {"fg": C["ember"]},
    "@lsp.type.keyword":        {"fg": C["nebula"], "bold": True},
    "@lsp.type.modifier":       {"fg": C["nebula"]},
    "@lsp.type.operator":       {"fg": C["cyan"]},
    "@lsp.type.comment":        {"fg": C["comment"], "italic": True},
    "@lsp.type.label":          {"fg": C["gold"]},
    "@lsp.type.namespace":      {"fg": C["gold"]},
    "@lsp.type.generic":        {"fg": C["fg"]},
    "@lsp.type.builtinType":    {"fg": C["gold"]},
    "@lsp.type.selfKeyword":    {"fg": C["rose"], "italic": True},
    "@lsp.type.escapeSequence": {"fg": C["cyan"]},
    "@lsp.type.formatSpecifier": {"fg": C["cyan"]},
    "@lsp.type.macro":          {"fg": C["nebula"]},
    "DiagnosticError":          {"fg": C["red"]},
    "DiagnosticWarn":           {"fg": C["yellow"]},
    "DiagnosticInfo":           {"fg": C["cyan"]},
    "DiagnosticHint":           {"fg": C["nebula"]},
    "DiagnosticSignError":      {"fg": C["red"]},
    "DiagnosticSignWarn":       {"fg": C["yellow"]},
    "DiagnosticSignInfo":       {"fg": C["cyan"]},
    "DiagnosticSignHint":       {"fg": C["nebula"]},
    "DiagnosticUnderlineError": {"undercurl": True, "sp": C["red"]},
    "DiagnosticUnderlineWarn":  {"undercurl": True, "sp": C["yellow"]},
    "DiagnosticUnderlineInfo":  {"undercurl": True, "sp": C["cyan"]},
    "DiagnosticUnderlineHint":  {"undercurl": True, "sp": C["nebula"]},
    "DiagnosticVirtualTextError": {"fg": C["red"]},
    "DiagnosticVirtualTextWarn":  {"fg": C["yellow"]},
    "DiagnosticVirtualTextInfo":  {"fg": C["cyan"]},
    "DiagnosticVirtualTextHint":  {"fg": C["nebula"]},
    "DiagnosticFloatingError":   {"fg": C["red"]},
    "DiagnosticFloatingWarn":    {"fg": C["yellow"]},
    "DiagnosticFloatingInfo":    {"fg": C["cyan"]},
    "DiagnosticFloatingHint":    {"fg": C["nebula"]},
    "LspReferenceRead":   {"bg": C["bg_ui2"]},
    "LspReferenceText":   {"bg": C["bg_ui2"]},
    "LspReferenceWrite":  {"bg": C["sel"]},
    "LspCodeLens":        {"fg": C["muted"], "italic": True},
    "LspInlayHint":       {"fg": C["muted"], "bg": C["bg_ui"]},
    "LspSignatureActiveParameter": {"fg": C["ice"], "bold": True},
}

# ---- plugin groups (popular ones) ----
plugins = {
    # treesitter context
    "TreesitterContext":       {"bg": C["bg_alt"]},
    "TreesitterContextLineNumber": {"fg": C["muted"]},
    # gitsigns
    "GitSignsAdd":             {"fg": C["green2"]},
    "GitSignsChange":          {"fg": C["nebula"]},
    "GitSignsDelete":          {"fg": C["red"]},
    "GitSignsCurrentLineBlame": {"fg": C["muted"], "italic": True},
    "GitSignsAddLn":           {"bg": "#14331F"},
    "GitSignsChangeLn":        {"bg": "#2E1B33"},
    "GitSignsDeleteLn":        {"bg": "#33141C"},
    # telescope
    "TelescopeNormal":         {"fg": C["fg"], "bg": C["bg"]},
    "TelescopeBorder":         {"fg": C["ice"], "bg": C["bg"]},
    "TelescopePromptNormal":   {"fg": C["fg"], "bg": C["bg_ui"]},
    "TelescopePromptBorder":   {"fg": C["ice"], "bg": C["bg_ui"]},
    "TelescopePromptTitle":    {"fg": C["bg"], "bg": C["ice"], "bold": True},
    "TelescopeResultsTitle":   {"fg": C["bg"], "bg": C["nebula"], "bold": True},
    "TelescopePreviewTitle":   {"fg": C["bg"], "bg": C["green"], "bold": True},
    "TelescopeSelection":      {"fg": C["ice"], "bg": C["sel"]},
    "TelescopeMatching":       {"fg": C["ice"], "bold": True},
    "TelescopePromptPrefix":   {"fg": C["ice"]},
    # nvim-tree / neo-tree
    "NvimTreeNormal":          {"fg": C["fg"], "bg": C["bg"]},
    "NvimTreeFolderName":      {"fg": C["blue"]},
    "NvimTreeOpenedFolderName": {"fg": C["ice"]},
    "NvimTreeRootFolder":      {"fg": C["ice"], "bold": True},
    "NvimTreeFileIcon":        {"fg": C["muted"]},
    "NvimTreeSpecialFile":     {"fg": C["nebula"]},
    "NvimTreeGitDirty":        {"fg": C["nebula"]},
    "NvimTreeGitNew":          {"fg": C["green2"]},
    "NvimTreeGitDeleted":      {"fg": C["red"]},
    "NeoTreeNormal":           {"fg": C["fg"], "bg": C["bg"]},
    "NeoTreeDirectoryName":    {"fg": C["blue"]},
    "NeoTreeGitModified":      {"fg": C["nebula"]},
    "NeoTreeGitAdded":         {"fg": C["green2"]},
    "NeoTreeGitDeleted":       {"fg": C["red"]},
    # which-key
    "WhichKey":                {"fg": C["ice"], "bold": True},
    "WhichKeyGroup":           {"fg": C["nebula"]},
    "WhichKeyValue":           {"fg": C["green"]},
    "WhichKeyDesc":            {"fg": C["fg"]},
    "WhichKeySeparator":       {"fg": C["muted"]},
    # cmp
    "CmpItemAbbr":             {"fg": C["fg"]},
    "CmpItemAbbrMatch":        {"fg": C["ice"], "bold": True},
    "CmpItemAbbrDeprecated":   {"fg": C["muted"], "strikethrough": True},
    "CmpItemMenu":             {"fg": C["muted"]},
    "CmpItemKindText":         {"fg": C["fg"]},
    "CmpItemKindMethod":       {"fg": C["blue"]},
    "CmpItemKindFunction":     {"fg": C["blue"]},
    "CmpItemKindConstructor":  {"fg": C["blue"]},
    "CmpItemKindField":        {"fg": C["white"]},
    "CmpItemKindVariable":     {"fg": C["white"]},
    "CmpItemKindClass":        {"fg": C["gold"]},
    "CmpItemKindInterface":    {"fg": C["gold"]},
    "CmpItemKindModule":       {"fg": C["gold"]},
    "CmpItemKindProperty":     {"fg": C["gold"]},
    "CmpItemKindKeyword":      {"fg": C["nebula"]},
    "CmpItemKindSnippet":      {"fg": C["nebula"]},
    "CmpItemKindColor":        {"fg": C["cyan"]},
    "CmpItemKindFile":         {"fg": C["blue"]},
    "CmpItemKindReference":    {"fg": C["cyan"]},
    "CmpItemKindFolder":       {"fg": C["blue"]},
    "CmpItemKindEnum":         {"fg": C["gold"]},
    "CmpItemKindConstant":     {"fg": C["ember"]},
    "CmpItemKindStruct":       {"fg": C["gold"]},
    "CmpItemKindTypeParameter":{"fg": C["gold"]},
    # indent-blankline
    "IndentBlanklineChar":     {"fg": C["border"]},
    "IndentBlanklineContextChar": {"fg": C["line"]},
    "IndentBlanklineSpaceChar": {"fg": C["border"]},
    # lualine
    "lualine_a_normal":        {"fg": C["bg"], "bg": C["ice"], "bold": True},
    "lualine_b_normal":        {"fg": C["ice"], "bg": C["bg_ui"]},
    "lualine_c_normal":        {"fg": C["fg"], "bg": C["bg"]},
    "lualine_a_insert":        {"fg": C["bg"], "bg": C["green"], "bold": True},
    "lualine_a_visual":        {"fg": C["bg"], "bg": C["nebula"], "bold": True},
    "lualine_a_replace":       {"fg": C["bg"], "bg": C["ember"], "bold": True},
    "lualine_a_command":       {"fg": C["bg"], "bg": C["gold"], "bold": True},
    "lualine_a_inactive":      {"fg": C["muted"], "bg": C["bg_ui"]},
    "lualine_b_inactive":      {"fg": C["muted"], "bg": C["bg_ui"]},
    "lualine_c_inactive":      {"fg": C["muted"], "bg": C["bg"]},
    "lualine_z_normal":        {"fg": C["ice"], "bg": C["bg_ui"]},
    # notify
    "NotifyERRORBorder":       {"fg": C["red"]},
    "NotifyWARNBorder":        {"fg": C["yellow"]},
    "NotifyINFOBorder":        {"fg": C["cyan"]},
    "NotifyDEBUGBorder":       {"fg": C["muted"]},
    "NotifyTRACEBorder":       {"fg": C["nebula"]},
    "NotifyERRORIcon":         {"fg": C["red"]},
    "NotifyWARNIcon":          {"fg": C["yellow"]},
    "NotifyINFOIcon":          {"fg": C["cyan"]},
    "NotifyDEBUGIcon":         {"fg": C["muted"]},
    "NotifyTRACEIcon":         {"fg": C["nebula"]},
    "NotifyERRORTitle":        {"fg": C["red"]},
    "NotifyWARNTitle":         {"fg": C["yellow"]},
    "NotifyINFOTitle":         {"fg": C["cyan"]},
    "NotifyDEBUGTitle":        {"fg": C["muted"]},
    "NotifyTRACETitle":        {"fg": C["nebula"]},
    # diffview / diff
    "DiffAdd":                {"fg": C["green2"], "bg": "#14331F"},
    "DiffChange":             {"fg": C["nebula"], "bg": "#2E1B33"},
    "DiffDelete":             {"fg": C["red"], "bg": "#33141C"},
    "DiffText":               {"fg": C["white"], "bg": C["sel"]},
    "diffAdded":              {"fg": C["green2"]},
    "diffChanged":            {"fg": C["nebula"]},
    "diffRemoved":            {"fg": C["red"]},
    "DiffviewFilePanelTitle": {"fg": C["ice"], "bold": True},
    "DiffviewFilePanelCounter": {"fg": C["nebula"]},
    # markdown / render-markdown
    "RenderMarkdownCode":     {"fg": C["nebula"], "bg": C["bg_alt"]},
    "RenderMarkdownHeading":  {"fg": C["green"], "bold": True},
    "RenderMarkdownTableHead": {"fg": C["ice"]},
    "MarkdownCode":           {"fg": C["nebula"]},
    # bufferline
    "BufferLineFill":         {"bg": C["bg"]},
    "BufferLineBackground":    {"fg": C["muted"], "bg": C["bg"]},
    "BufferLineBufferSelected": {"fg": C["ice"], "bg": C["bg_alt"], "bold": True},
    "BufferLineIndicatorSelected": {"fg": C["ice"]},
    "BufferLineModified":     {"fg": C["nebula"]},
    "BufferLineSeparator":     {"fg": C["border"]},
    "BufferLineTabSelected":   {"fg": C["ice"], "bg": C["bg_alt"]},
    # noice
    "NoiceCmdlineIcon":       {"fg": C["ice"]},
    "NoiceCmdlinePopup":      {"fg": C["fg"], "bg": C["bg_ui"]},
    "NoiceCmdlinePopupBorder": {"fg": C["ice"], "bg": C["bg_ui"]},
    "NoiceConfirmation":       {"fg": C["fg"], "bg": C["bg_ui"]},
    # mini.nvim
    "MiniIndentscopeSymbol":  {"fg": C["line"]},
    "MiniPickNormal":         {"fg": C["fg"], "bg": C["bg"]},
    "MiniPickBorder":         {"fg": C["ice"]},
    "MiniPickTitle":          {"fg": C["bg"], "bg": C["ice"], "bold": True},
    "MiniStatuslineDevinfo":  {"fg": C["fg"], "bg": C["bg_ui"]},
    "MiniStatuslineFilename": {"fg": C["fg"], "bg": C["bg"]},
    "MiniStatuslineInactive": {"fg": C["muted"], "bg": C["bg_ui"]},
    "MiniStatuslineModeNormal": {"fg": C["bg"], "bg": C["ice"], "bold": True},
    "MiniStatuslineModeInsert": {"fg": C["bg"], "bg": C["green"], "bold": True},
    "MiniStatuslineModeVisual": {"fg": C["bg"], "bg": C["nebula"], "bold": True},
    "MiniSurround":           {"fg": C["ice"], "bg": C["sel"]},
    "MiniTablineCurrent":     {"fg": C["ice"], "bg": C["bg_alt"], "bold": True},
    "MiniTablineVisible":     {"fg": C["fg"], "bg": C["bg"]},
    "MiniTablineHidden":      {"fg": C["muted"], "bg": C["bg"]},
    "MiniTablineModifiedCurrent": {"fg": C["nebula"]},
    "MiniHint":               {"fg": C["cyan"], "bg": C["bg_ui"]},
    "MiniInfo":               {"fg": C["cyan"], "bg": C["bg_ui"]},
    "MiniWarn":               {"fg": C["yellow"], "bg": C["bg_ui"]},
    "MiniError":              {"fg": C["red"], "bg": C["bg_ui"]},
    # hop / leap
    "HopNextKey":             {"fg": C["ice"], "bold": True},
    "HopUnmatched":           {"fg": C["muted"]},
    "LeapLabelPrimary":       {"fg": C["ice"], "bold": True},
    "LeapLabelSecondary":     {"fg": C["nebula"], "bold": True},
}

def fmt_hl(d):
    """Render a highlight table to a Lua table literal of valid nvim_set_hl options."""
    parts = []
    for k, v in d.items():
        if v == "NONE":
            parts.append(f"    {k} = 'NONE'")
            continue
        opts = []
        if "fg" in v: opts.append(f"fg = '{v['fg']}'")
        if "bg" in v: opts.append(f"bg = '{v['bg']}'")
        if "sp" in v: opts.append(f"sp = '{v['sp']}'")
        if v.get("bold"): opts.append("bold = true")
        if v.get("italic"): opts.append("italic = true")
        if v.get("underline"): opts.append("underline = true")
        if v.get("undercurl"): opts.append("undercurl = true")
        if v.get("strikethrough"): opts.append("strikethrough = true")
        parts.append(f"    {k} = {{ {', '.join(opts)} }}")
    return "{\n" + ",\n".join(parts) + "\n  }"

all_groups = {}
all_groups.update(editor)
all_groups.update(syntax)
all_groups.update(treesitter)
all_groups.update(lsp)
all_groups.update(plugins)

root = os.path.dirname(os.path.abspath(__file__))

# palette.lua
palette_lua = """-- Aurora X — pure-AMOLED palette
-- Author: Ayoub Zulfiqar (https://ayoubzulfiqar.com)
local M = {
  none      = "NONE",
  black     = "#000000",
  bg        = "#000000",
  bg_alt    = "#0C0E19",
  bg_ui     = "#15182B",
  bg_ui2    = "#1C2138",
  fg        = "#C7D5FF",
  fg_dim    = "#9AA8D6",
  muted     = "#576DAF",
  comment   = "#546E7A",
  ice       = "#86A5FF",
  nebula    = "#C792EA",
  cyan      = "#89DDFF",
  green     = "#C3E88D",
  ember     = "#F78C6C",
  gold      = "#FFCB6B",
  rose      = "#F07178",
  magenta   = "#DD5074",
  red       = "#DD5074",
  green2    = "#63EB90",
  blue      = "#82AAFF",
  white     = "#EEFFFF",
  yellow    = "#FFCB6B",
  line      = "#262E47",
  sel       = "#262E47",
  line_nr   = "#3A4B6B",
  border    = "#15182B",
}
return M
"""

# groups.lua
groups_lua = f"""-- Aurora X — highlight groups
-- Author: Ayoub Zulfiqar (https://ayoubzulfiqar.com)
local M = {{}}

M.get = function()
  return {fmt_hl(all_groups)}
end

return M
"""

# init.lua
init_lua = """-- Aurora X — Neovim colorscheme (pure-AMOLED)
-- Author: Ayoub Zulfiqar (https://ayoubzulfiqar.com)
local M = {}

M.setup = function(opts)
  opts = opts or {}
  vim.g.aurora_x_loaded = true
  vim.g.colors_name = "aurora-x"
end

M.load = function()
  if vim.fn.has("nvim") == 0 then
    vim.api.nvim_err_writeln("aurora-x is a Neovim-only colorscheme")
    return
  end
  vim.g.colors_name = "aurora-x"

  -- reset existing highlights
  vim.cmd("hi clear")
  if vim.fn.exists("syntax_on") == 1 then
    vim.cmd("syntax reset")
  end

  local groups = require("aurora-x.groups").get()
  for name, attrs in pairs(groups) do
    vim.api.nvim_set_hl(0, name, attrs)
  end

  -- terminal colors (true-color ANSI ramp)
  vim.g.terminal_color_0  = "#000000"
  vim.g.terminal_color_1  = "#DD5074"
  vim.g.terminal_color_2  = "#63EB90"
  vim.g.terminal_color_3  = "#FFCB6B"
  vim.g.terminal_color_4  = "#82AAFF"
  vim.g.terminal_color_5  = "#C792EA"
  vim.g.terminal_color_6  = "#89DDFF"
  vim.g.terminal_color_7  = "#C7D5FF"
  vim.g.terminal_color_8  = "#576DAF"
  vim.g.terminal_color_9  = "#FF6E8A"
  vim.g.terminal_color_10 = "#8FF0B0"
  vim.g.terminal_color_11 = "#FFD98A"
  vim.g.terminal_color_12 = "#A8BEFF"
  vim.g.terminal_color_13 = "#E0A9F5"
  vim.g.terminal_color_14 = "#AEF2FF"
  vim.g.terminal_color_15 = "#FFFFFF"

  -- re-apply on colorscheme change (keeps overrides sticky)
  vim.api.nvim_create_autocmd("ColorScheme", {
    group = vim.api.nvim_create_augroup("aurora_x_reapply", { clear = true }),
    pattern = "aurora-x",
    callback = function()
      local g = require("aurora-x.groups").get()
      for name, attrs in pairs(g) do
        vim.api.nvim_set_hl(0, name, attrs)
      end
    end,
  })
end

return M
"""

# colors/aurora-x.lua (runtime entry point)
entry_lua = """-- Aurora X — :colorscheme aurora-x entry point
-- Author: Ayoub Zulfiqar (https://ayoubzulfiqar.com)
require("aurora-x").load()
"""

os.makedirs(os.path.join(root, "lua", "aurora-x"), exist_ok=True)
os.makedirs(os.path.join(root, "colors"), exist_ok=True)
with open(os.path.join(root, "lua", "aurora-x", "palette.lua"), "w") as f: f.write(palette_lua)
with open(os.path.join(root, "lua", "aurora-x", "groups.lua"), "w") as f: f.write(groups_lua)
with open(os.path.join(root, "lua", "aurora-x", "init.lua"), "w") as f: f.write(init_lua)
with open(os.path.join(root, "colors", "aurora-x.lua"), "w") as f: f.write(entry_lua)

print("Neovim files written. Groups:", len(all_groups),
      "(editor", len(editor), "syntax", len(syntax),
      "treesitter", len(treesitter), "lsp", len(lsp), "plugins", len(plugins), ")")
