"""API Manager Dialog - User Workflow Diagram"""

WORKFLOW = """

╔═══════════════════════════════════════════════════════════════════════════╗
║                    🔐 API MANAGER DIALOG WORKFLOW                         ║
╚═══════════════════════════════════════════════════════════════════════════╝

STEP 1: OPEN API MANAGER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Click "⚙️ MANAGE APIS" button in main window
           ↓
   Dialog opens showing provider tabs


STEP 2: SELECT PROVIDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ┌─────────────────────────────────────────────┐
   │  🔐 API KEY MANAGER                    ✕   │
   ├─────────────────────────────────────────────┤
   │                                             │
   │  Select provider aur API key enter karein:  │
   │                                             │
   │  [🔮 GEMINI] [⚡ GROQ] [🌐 OPENROUTER]   │
   │                                             │
   │  ─────────────────────────────────────────  │
   │                                             │
   │  🔮 GEMINI API KEY                          │
   │  ┌──────────────────────────────────────┐  │
   │  │ AIza•••••••••••••••••••••••••••••    │  │
   │  └──────────────────────────────────────┘  │
   │                                             │
   │  ✓ GEMINI: Saved key detected              │
   │                                             │
   │  ┌──────────────────┐  ┌──────────────────┐│
   │  │ 💾  SAVE         │  │ 🗑️  CLEAR       ││
   │  └──────────────────┘  └──────────────────┘│
   └─────────────────────────────────────────────┘


STEP 3: SWITCH PROVIDER (Click different tab)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   User clicks "⚡ GROQ" tab
           ↓
   Dialog shows only Groq input field
           ↓
   Gemini and OpenRouter inputs are hidden


STEP 4: SAVE OR CLEAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Option A: SAVE
   ├─ User enters API key
   ├─ Clicks 💾 SAVE button
   ├─ Key saved to config/api_keys.json
   ├─ Status: "✓ GROQ key saved successfully!"
   └─ System uses this key on next startup

   Option B: CLEAR
   ├─ User clicks 🗑️ CLEAR
   ├─ Current input cleared
   ├─ Status: "Cleared GROQ key"
   └─ Saved key remains (only input is cleared)


STEP 5: CLOSE DIALOG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   User clicks ✕ (close button)
           ↓
   Dialog hides
           ↓
   Saved keys remain active
           ↓
   System continues with available API keys


AUTO-POPUP ON FAILURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Primary API (Gemini) fails
           ↓
   System tries fallback #1 (Groq)
           ↓
   Groq also fails
           ↓
   System tries fallback #2 (OpenRouter)
           ↓
   All APIs exhausted
           ↓
   DIALOG AUTO-OPENS with message:
   "⚠️ All API keys have failed. Please add a new key."
           ↓
   User adds/updates API key
           ↓
   Dialog closes
           ↓
   System resumes operation


FALLBACK CHAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Config Example:
   {
     "primary_provider": "gemini",
     "fallback_providers": ["groq", "openrouter"],
     "providers": {
       "gemini": {"keys": ["AIza..."], "active_key_index": 0},
       "groq": {"keys": ["gsk_..."], "active_key_index": 0},
       "openrouter": {"keys": ["sk-or-..."], "active_key_index": 0}
     }
   }

   Try Order:
   1️⃣  Gemini (primary)
   2️⃣  Groq (fallback #1)
   3️⃣  OpenRouter (fallback #2)


VOICE COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   "Jarvis, popup open karo"
        → Opens API Manager dialog

   "Window open karo, mujhe API key enter karni hai"
        → Opens API Manager dialog

   "Manage APIs"
        → Opens API Manager dialog


STATUS INDICATORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ✓ GEMINI: Saved key detected
   ⚠️  GROQ: No key saved yet
   ❌ ERROR: Please enter an API key


╔═══════════════════════════════════════════════════════════════════════════╗
║                          KEY FEATURES SUMMARY                             ║
╠═══════════════════════════════════════════════════════════════════════════╣
║ ✓ Single provider shown at a time                                        ║
║ ✓ Auto-load existing API keys                                            ║
║ ✓ Tab-style provider switching                                           ║
║ ✓ Save/Clear/Close buttons                                               ║
║ ✓ Real-time status indicators                                            ║
║ ✓ Auto-popup on API failure                                              ║
║ ✓ Graceful fallback chain                                                ║
║ ✓ No app restart needed                                                  ║
╚═══════════════════════════════════════════════════════════════════════════╝

"""

if __name__ == "__main__":
    print(WORKFLOW)
