-- dfb-state.lua — leitura estruturada (JSON) do estado do jogo p/ agentes LLM.
-- Instalado automaticamente pelo df_bridge.py em <DF>/dfhack-config/scripts/.
-- Uso (console ou dfhack-run):  dfb-state <adventurer|threats|units|inventory|date|all> [raio]
-- Saída: UMA linha/bloco JSON em stdout (consumida por `df_bridge.py state ...`).
-- Licença: MIT (dwarf-fortress-agent-skills).

local json = require('json')

local args = {...}
local what = args[1] or 'all'
local radius = tonumber(args[2]) or 25
local Z_RADIUS = 5                       -- ameaças: poucos níveis acima/abaixo importam

local function utf(s)
  return s and dfhack.df2utf(s) or nil
end

-- ---------- data do mundo ----------
local MONTHS = { 'Granite','Slate','Felsite','Hematite','Malachite','Galena',
                 'Limestone','Sandstone','Timber','Moonstone','Opal','Obsidian' }
local SEASONS = { 'spring','spring','spring','summer','summer','summer',
                  'autumn','autumn','autumn','winter','winter','winter' }

local function state_date()
  local tick = df.global.cur_year_tick
  local month = math.floor(tick / 33600) + 1       -- 28 dias x 1200 ticks
  local day = math.floor((tick % 33600) / 1200) + 1
  return {
    year = df.global.cur_year,
    tick = tick,
    month = MONTHS[month] or month,
    day = day,
    season = SEASONS[month] or 'unknown',
  }
end

-- ---------- aventureiro ----------
local function adventurer_unit()
  local u = dfhack.world.getAdventurer and dfhack.world.getAdventurer()
  if not u then qerror('sem aventureiro (o jogo está em adventure mode?)') end
  return u
end

local function state_adventurer()
  local u = adventurer_unit()
  local c, c2 = u.counters, u.counters2
  return {
    name = utf(dfhack.units.getReadableName(u)),
    race = utf(dfhack.units.getRaceReadableName(u)),
    profession = utf(dfhack.units.getProfessionName(u)),
    pos = { x = u.pos.x, y = u.pos.y, z = u.pos.z },
    health = {
      blood = u.body.blood_count, blood_max = u.body.blood_max,
      wounds = #u.body.wounds,
      pain = c.pain, nausea = c.nausea, dizziness = c.dizziness,
      winded = c.winded, stunned = c.stunned, unconscious = c.unconscious,
      webbed = c.webbed, paralysis = c2.paralysis, fever = c2.fever,
      exhaustion = c2.exhaustion,
    },
    -- timers sobem com o tempo; rótulos pelos limiares clássicos dos anúncios
    needs = {
      hunger_timer = c2.hunger_timer,
      hungry = c2.hunger_timer >= 75000,
      starving = c2.hunger_timer >= 150000,
      thirst_timer = c2.thirst_timer,
      thirsty = c2.thirst_timer >= 25000,
      dehydrated = c2.thirst_timer >= 50000,
      sleepiness_timer = c2.sleepiness_timer,
      drowsy = c2.sleepiness_timer >= 57600,
    },
    kills = dfhack.units.getKillCount(u),
    stress_category = dfhack.units.getStressCategory(u),
  }
end

-- ---------- unidades / ameaças ao redor ----------
local function direction(dx, dy, dz)
  local d = ''
  if dy < 0 then d = 'N' elseif dy > 0 then d = 'S' end
  if dx > 0 then d = d .. 'E' elseif dx < 0 then d = d .. 'W' end
  if d == '' then d = 'aqui' end
  if dz > 0 then d = d .. ' +' .. dz .. 'z' elseif dz < 0 then d = d .. ' ' .. dz .. 'z' end
  return d
end

local function scan_units(only_threats)
  local adv = adventurer_unit()
  local ax, ay, az = adv.pos.x, adv.pos.y, adv.pos.z
  local out = {}
  for _, u in ipairs(df.global.world.units.active) do
    if u ~= adv and dfhack.units.isAlive(u) then
      local dx, dy, dz = u.pos.x - ax, u.pos.y - ay, u.pos.z - az
      local dist = math.max(math.abs(dx), math.abs(dy))
      if dist <= radius and math.abs(dz) <= Z_RADIUS then
        local danger = dfhack.units.isDanger(u)
        if not only_threats or danger then
          out[#out + 1] = {
            name = utf(dfhack.units.getReadableName(u)),
            race = utf(dfhack.units.getRaceReadableNameById(u.race)),
            dist = dist,
            dir = direction(dx, dy, dz),
            pos = { x = u.pos.x, y = u.pos.y, z = u.pos.z },
            danger = danger,
            great_danger = dfhack.units.isGreatDanger(u),
            invader = dfhack.units.isInvader(u),
            undead = dfhack.units.isUndead(u),
            agitated = dfhack.units.isAgitated(u),
            wildlife = dfhack.units.isWildlife(u),
            tame = dfhack.units.isTame(u),
            hidden = dfhack.units.isHidden(u),   -- info "armok": use com parcimônia
            crazed = dfhack.units.isCrazed(u),
          }
        end
      end
    end
  end
  table.sort(out, function(a, b) return a.dist < b.dist end)
  -- limita p/ não estourar o contexto do agente
  while #out > 20 do table.remove(out) end
  return out
end

-- ---------- inventário ----------
local function state_inventory()
  local u = adventurer_unit()
  local out = {}
  for _, e in ipairs(u.inventory) do
    out[#out + 1] = {
      mode = df.inv_item_role_type[e.mode] or tostring(e.mode),
      item = utf(dfhack.items.getReadableDescription(e.item)),
    }
  end
  return out
end

-- ---------- despacho ----------
local result
if what == 'adventurer' then
  result = state_adventurer()
elseif what == 'threats' then
  result = { radius = radius, threats = scan_units(true) }
elseif what == 'units' then
  result = { radius = radius, units = scan_units(false) }
elseif what == 'inventory' then
  result = state_inventory()
elseif what == 'date' then
  result = state_date()
elseif what == 'all' then
  result = {
    date = state_date(),
    adventurer = state_adventurer(),
    threats = scan_units(true),
  }
else
  qerror('uso: dfb-state <adventurer|threats|units|inventory|date|all> [raio]')
end

print(json.encode(result))
