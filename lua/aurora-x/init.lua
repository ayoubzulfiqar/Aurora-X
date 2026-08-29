-- Aurora X — Neovim colorscheme (pure-AMOLED)
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
